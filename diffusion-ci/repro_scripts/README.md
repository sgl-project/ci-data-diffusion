# Official Reproduction Scripts

These scripts map CI `case_id` values to the official-reference generation path
used by the report. `HF_TOKEN` is intentionally not stored here; set it in the
environment before running gated model cases.

## Files

- `gen_official_diffusion_gt.py`: SGLang helper for official Diffusers and Wan2.1 official-repo generation.
- `gen_official_wan22_ti2v.py`: Wan2.2 official repo TI2V investigation helper; not mapped to the current comparable GT set.
- `gen_official_ltx23.py`: LTX official repo generator for the covered LTX-2.3 CI cases; verified on H200 with fp8-cast and inference_mode.
- `run_official_*.sh`: command wrappers for each official source group.
- `official_repro_case_map.json`: machine-readable case_id -> script mapping.

## Case Map

| case_id | status | script | wrapper | notes |
|---|---|---|---|---|
| `fast_hunyuan_video` | `official_not_comparable` | `-` | `-` | CI uses the FastVideo path, so Diffusers output is not a comparable official reference. |
| `flux_2_image_t2i` | `official_comparable` | `gen_official_diffusion_gt.py` | `run_official_diffusers_cases.sh` | Official reference refreshed with current official Diffusers script. |
| `flux_2_image_t2i_upscaling_4x` | `native_only_excluded` | `-` | `-` | postprocess upscaling has no upstream official implementation |
| `flux_2_klein_image_t2i` | `official_comparable` | `gen_official_diffusion_gt.py` | `run_official_diffusers_cases.sh` | - |
| `flux_2_t2i_customized_vae_path` | `native_only_excluded` | `-` | `-` | custom VAE path is not reproduced by the official script; current artifact used default Flux2 VAE |
| `flux_2_ti2i` | `official_comparable` | `gen_official_diffusion_gt.py` | `run_official_diffusers_cases.sh` | - |
| `flux_2_ti2i_multi_image_cache_dit` | `native_only_excluded` | `-` | `-` | cache_dit has no upstream official implementation |
| `flux_image_t2i` | `official_comparable` | `gen_official_diffusion_gt.py` | `run_official_diffusers_cases.sh` | - |
| `layerwise_offload` | `native_only_excluded` | `-` | `-` | offload behavior has no upstream official implementation |
| `ltx_2.3_one_stage_ti2v` | `official_comparable` | `gen_official_ltx23.py` | `run_official_ltx23.sh` | Official GT regenerated successfully on H200; still below current strict thresholds. |
| `ltx_2.3_two_stage_t2v_2gpus` | `official_comparable` | `gen_official_ltx23.py` | `run_official_ltx23.sh` | Official GT restored; script path is comparable but native alignment is still poor. |
| `ltx_2_3_hq_pipeline` | `official_comparable` | `gen_official_ltx23.py` | `run_official_ltx23.sh` | Official HQ two-stage TI2V path: CI prompt, CI reference image, 1920x1088, 24 frames, 15 steps. |
| `qwen_image_edit_2509_ti2i` | `official_comparable` | `gen_official_diffusion_gt.py` | `run_official_diffusers_cases.sh` | Official reference refreshed with current official Diffusers script. |
| `qwen_image_edit_2511_ti2i` | `official_comparable` | `gen_official_diffusion_gt.py` | `run_official_diffusers_cases.sh` | - |
| `qwen_image_edit_ti2i` | `official_comparable` | `gen_official_diffusion_gt.py` | `run_official_diffusers_cases.sh` | - |
| `qwen_image_layered_i2i` | `official_comparable` | `gen_official_diffusion_gt.py` | `run_official_diffusers_cases.sh` | - |
| `qwen_image_t2i` | `official_comparable` | `gen_official_diffusion_gt.py` | `run_official_diffusers_cases.sh` | - |
| `qwen_image_t2i_cache_dit_enabled` | `native_only_excluded` | `-` | `-` | cache_dit has no upstream official implementation |
| `wan2_1_t2v_1.3b` | `official_comparable` | `gen_official_diffusion_gt.py` | `run_official_wan21.sh` | - |
| `wan2_1_t2v_1.3b_frame_interp_2x` | `native_only_excluded` | `-` | `-` | postprocess frame interpolation has no upstream official implementation |
| `wan2_1_t2v_1.3b_frame_interp_2x_upscaling_4x` | `native_only_excluded` | `-` | `-` | postprocess frame interpolation/upscaling has no upstream official implementation |
| `wan2_1_t2v_1.3b_teacache_enabled` | `native_only_excluded` | `-` | `-` | teacache/cache path has no upstream official implementation |
| `wan2_1_t2v_1.3b_text_encoder_cpu_offload` | `native_only_excluded` | `-` | `-` | offload behavior has no upstream official implementation |
| `wan2_1_t2v_1.3b_upscaling_4x` | `native_only_excluded` | `-` | `-` | postprocess upscaling has no upstream official implementation |
| `wan2_1_t2v_1_3b_lora_1gpu` | `native_only_excluded` | `-` | `-` | CI case is dynamic_lora_path/set_lora; current artifact used Diffusers load_lora_weights, not official Wan repo or dynamic-load semantics |
| `wan2_2_ti2v_5b` | `official_not_comparable` | `-` | `-` | Diffusers does not inject TI2V image input; attempted official-repo output is not retained as comparable GT. |
| `zimage_image_t2i` | `official_comparable` | `gen_official_diffusion_gt.py` | `run_official_diffusers_cases.sh` | - |
| `zimage_image_t2i_fp8` | `native_only_excluded` | `-` | `-` | CI uses --transformer-path MickJ/Z-Image-Turbo-fp8; current official script only reproduces base ZImage |
