#!/usr/bin/env python3

"""Generate the Pi0.5 action GT with the official OpenPI PyTorch model."""

from __future__ import annotations

import argparse
import dataclasses
import json
from pathlib import Path

import jax
import numpy as np
import torch
from huggingface_hub import snapshot_download

from openpi.models import model as openpi_model
from openpi.models import tokenizer as openpi_tokenizer
from openpi.policies import policy_config
from openpi.shared import download, image_tools
from openpi.training import checkpoints as openpi_checkpoints
from openpi.training import config as openpi_config


OPENPI_REVISION = "15a9616a00943ada6c20a0f158e3adb39df2ccac"
CHECKPOINT_REPO = "lerobot/pi05_base"
CHECKPOINT_REVISION = "b211f3d44c36b6acfcf7ae94a64e8e96f75a64ba"
CAMERA_ORDER = ("base_0_rgb", "left_wrist_0_rgb", "right_wrist_0_rgb")
PROMPT = "pick up the blue block"
ACTION_HORIZON = 50
ACTION_DIM = 32
NUM_STEPS = 2


def make_image(camera_index: int, size: int = 64) -> np.ndarray:
    y = np.arange(size, dtype=np.uint16)[:, None]
    x = np.arange(size, dtype=np.uint16)[None, :]
    return np.stack(
        (
            (x + camera_index * 17) % 256 + np.zeros_like(y),
            (y + camera_index * 29) % 256 + np.zeros_like(x),
            (x + y + camera_index * 41) % 256,
        ),
        axis=-1,
    ).astype(np.uint8)


def build_model_observation(device: str) -> openpi_model.Observation:
    state = np.linspace(-0.5, 0.5, 14, dtype=np.float32)
    tokenizer = openpi_tokenizer.PaligemmaTokenizer(max_len=200)
    tokens, token_masks = tokenizer.tokenize(PROMPT, state)
    images = {
        name: np.asarray(image_tools.resize_with_pad(make_image(index), 224, 224))
        for index, name in enumerate(CAMERA_ORDER)
    }
    inputs = {
        "image": images,
        "image_mask": {name: np.asarray(True) for name in CAMERA_ORDER},
        "state": np.pad(state, (0, ACTION_DIM - state.shape[0])),
        "tokenized_prompt": tokens,
        "tokenized_prompt_mask": token_masks,
    }
    torch_inputs = jax.tree.map(
        lambda value: torch.from_numpy(np.array(value, copy=True)).to(device)[
            None, ...
        ],
        inputs,
    )
    return openpi_model.Observation.from_dict(torch_inputs)


def load_policy(device: str):
    checkpoint = snapshot_download(
        repo_id=CHECKPOINT_REPO,
        revision=CHECKPOINT_REVISION,
    )
    assets = download.maybe_download(
        "gs://openpi-assets/checkpoints/pi05_base/assets"
    )
    train_config = openpi_config.get_config("pi05_aloha")
    train_config = dataclasses.replace(
        train_config,
        model=dataclasses.replace(train_config.model, pytorch_compile_mode=None),
    )
    return policy_config.create_trained_policy(
        train_config,
        checkpoint,
        sample_kwargs={"num_steps": NUM_STEPS},
        norm_stats=openpi_checkpoints.load_norm_stats(assets, "trossen"),
        pytorch_device=device,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("pi05_action_http_1gpu.json"),
    )
    parser.add_argument("--device", default="cuda")
    args = parser.parse_args()

    policy = load_policy(args.device)
    observation = build_model_observation(args.device)
    noise = np.random.default_rng(0).standard_normal(
        (ACTION_HORIZON, ACTION_DIM)
    ).astype(np.float32)
    actions = policy._sample_actions(
        args.device,
        observation,
        noise=torch.from_numpy(noise).to(args.device)[None, ...],
        **policy._sample_kwargs,
    )[0].detach().float().cpu().numpy()

    payload = {
        "id": "official-openpi-pi05",
        "object": "action.generation",
        "model": CHECKPOINT_REPO,
        "data": [
            {
                "index": 0,
                "action": {
                    "dtype": "float32",
                    "shape": [ACTION_HORIZON, ACTION_DIM],
                    "values": actions.tolist(),
                },
            }
        ],
        "provenance": {
            "source": "OpenPI PyTorch",
            "openpi_revision": OPENPI_REVISION,
            "checkpoint_repo": CHECKPOINT_REPO,
            "checkpoint_revision": CHECKPOINT_REVISION,
            "model_space": True,
            "noise_seed": 0,
            "num_inference_steps": NUM_STEPS,
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
