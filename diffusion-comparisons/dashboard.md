# SGLang-Diffusion Nightly Performance Dashboard

*Generated: Aug 03 | Commit: `0ba46c8`*

## SGLang-Diffusion Performance

| Model | Risk | sglang (s) |
|-------|------|---------|
| FLUX.1-dev | ✅ | **4.85** |
| FLUX.2-dev | ✅ | **14.47** |
| Qwen-Image-2512 | ✅ | **8.86** |
| Qwen-Image-Edit-2511 | ✅ | **15.65** |
| Z-Image-Turbo | ✅ | **0.81** |
| Wan2.2-T2V-A14B-Diffusers | ✅ | **208.68** |
| Wan2.2-TI2V-5B-Diffusers | ✅ | **65.22** |
| LTX-2.3 | ✅ | **14.07** |
| ideogram-4-fp8 | ✅ | **5.33** |
| Cosmos3-Super | ✅ | **115.34** |
| Wan2.2-I2V-A14B-Diffusers | ✅ | **202.65** |

### Latency Trend: flux1_dev_t2i_1024

![Latency Trend flux1_dev_t2i_1024](https://raw.githubusercontent.com/sgl-project/ci-data-diffusion/main/diffusion-comparisons/charts/latency_flux1_dev_t2i_1024.png)


### Latency Trend: flux2_dev_t2i_1024

![Latency Trend flux2_dev_t2i_1024](https://raw.githubusercontent.com/sgl-project/ci-data-diffusion/main/diffusion-comparisons/charts/latency_flux2_dev_t2i_1024.png)


### Latency Trend: qwen_image_2512_t2i_1024

![Latency Trend qwen_image_2512_t2i_1024](https://raw.githubusercontent.com/sgl-project/ci-data-diffusion/main/diffusion-comparisons/charts/latency_qwen_image_2512_t2i_1024.png)


### Latency Trend: qwen_image_edit_2511

![Latency Trend qwen_image_edit_2511](https://raw.githubusercontent.com/sgl-project/ci-data-diffusion/main/diffusion-comparisons/charts/latency_qwen_image_edit_2511.png)


### Latency Trend: zimage_turbo_t2i_1024

![Latency Trend zimage_turbo_t2i_1024](https://raw.githubusercontent.com/sgl-project/ci-data-diffusion/main/diffusion-comparisons/charts/latency_zimage_turbo_t2i_1024.png)


### Latency Trend: wan22_t2v_a14b_720p

![Latency Trend wan22_t2v_a14b_720p](https://raw.githubusercontent.com/sgl-project/ci-data-diffusion/main/diffusion-comparisons/charts/latency_wan22_t2v_a14b_720p.png)


### Latency Trend: wan22_ti2v_5b_720p

![Latency Trend wan22_ti2v_5b_720p](https://raw.githubusercontent.com/sgl-project/ci-data-diffusion/main/diffusion-comparisons/charts/latency_wan22_ti2v_5b_720p.png)


### Latency Trend: ltx2.3_twostage_ti2v_2gpus

![Latency Trend ltx2.3_twostage_ti2v_2gpus](https://raw.githubusercontent.com/sgl-project/ci-data-diffusion/main/diffusion-comparisons/charts/latency_ltx2.3_twostage_ti2v_2gpus.png)


### Latency Trend: ideogram4_fp8_t2i_2gpu

![Latency Trend ideogram4_fp8_t2i_2gpu](https://raw.githubusercontent.com/sgl-project/ci-data-diffusion/main/diffusion-comparisons/charts/latency_ideogram4_fp8_t2i_2gpu.png)


### Latency Trend: cosmos3_super_t2v_2gpu

![Latency Trend cosmos3_super_t2v_2gpu](https://raw.githubusercontent.com/sgl-project/ci-data-diffusion/main/diffusion-comparisons/charts/latency_cosmos3_super_t2v_2gpu.png)


### Latency Trend: wan22_i2v_a14b_720p

![Latency Trend wan22_i2v_a14b_720p](https://raw.githubusercontent.com/sgl-project/ci-data-diffusion/main/diffusion-comparisons/charts/latency_wan22_i2v_a14b_720p.png)


## SGLang Performance Trend (Last 30 Runs)

| Date | Commit | flux1_dev_t2i_1024 (s) | flux2_dev_t2i_1024 (s) | qwen_image_2512_t2i_1024 (s) | qwen_image_edit_2511 (s) | zimage_turbo_t2i_1024 (s) | wan22_t2v_a14b_720p (s) | wan22_ti2v_5b_720p (s) | ltx2.3_twostage_ti2v_2gpus (s) | ideogram4_fp8_t2i_2gpu (s) | cosmos3_super_t2v_2gpu (s) | wan22_i2v_a14b_720p (s) | Trend |
|------|--------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|-------|
| Aug 03 | `0ba46c8` | 4.85 | 14.47 | 8.86 | 15.65 | 0.81 | 208.68 | 65.22 | 14.07 | 5.33 | 115.34 | 202.65 | :left_right_arrow:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow: |
| Aug 01 | `ae84811` | 4.85 | 14.47 | 11.06 | 15.42 | 0.96 | 208.76 | 64.22 | 16.07 | 5.36 | 115.41 | 204.69 | :left_right_arrow:  :left_right_arrow:  :arrow_up:  :left_right_arrow:  :arrow_up:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow: |
| Jul 31 | `5f9b0db` | 4.86 | 14.72 | 10.74 | 15.52 | 0.82 | 208.70 | 65.24 | 16.08 | 5.34 | 115.41 | 202.77 | :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow: |
| Jul 29 | `e1f2f9d` | 4.87 | 14.49 | 10.53 | 15.42 | 0.82 | 210.65 | 64.21 | 16.07 | 5.37 | 115.32 | 203.71 | :left_right_arrow:  :left_right_arrow:  :arrow_up:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :arrow_up:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow: |
| Jul 27 | `8d6549b` | 4.84 | 14.36 | 8.75 | 15.30 | 0.81 | 210.75 | 64.24 | 13.06 | 5.40 | 115.34 | 204.72 | :arrow_down:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow: |
| Jul 25 | `e943e60` | 4.95 | 14.46 | 10.50 | 15.44 | 0.83 | 211.76 | 65.23 | 16.08 | 5.35 | 116.35 | 205.66 | :arrow_down:  :left_right_arrow:  :arrow_up:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :arrow_up:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow: |
| Jul 23 | `b98a577` | 5.27 | 14.51 | 8.82 | 15.41 | 0.83 | 210.72 | 65.23 | 13.06 | 5.33 | 116.40 | 205.68 | :arrow_up:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :arrow_up:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow: |
| Jul 20 | `b3570a4` | 4.83 | 14.33 | 8.80 | 15.26 | 0.81 | 210.73 | 65.25 | 13.06 | 5.31 | 115.38 | 203.68 | :left_right_arrow:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow: |
| Jul 19 | `99f5a6f` | 4.85 | 14.43 | 10.96 | 15.41 | 0.86 | 210.72 | 65.21 | 16.07 | 5.35 | 115.39 | 203.71 | :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :arrow_up:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:   :left_right_arrow:  :left_right_arrow: |
| Jul 18 | `e48eabb` | 4.86 | 14.41 | 10.86 | 15.41 | 0.83 | 210.72 | 65.23 | 16.08 | N/A | 115.29 | 203.68 | :left_right_arrow:  :left_right_arrow:  :arrow_up:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :arrow_up:   :left_right_arrow:  :left_right_arrow: |
| Jul 17 | `dc0b3eb` | 4.85 | 14.48 | 9.02 | 15.41 | 0.83 | 210.69 | 65.20 | 13.05 | 5.31 | 115.32 | 204.58 | :left_right_arrow:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow: |
| Jul 16 | `b0b2dfb` | 4.87 | 14.41 | 10.80 | 15.41 | 0.83 | 210.62 | 65.24 | 16.06 | 5.35 | 115.35 | 204.68 | :left_right_arrow:  :left_right_arrow:  :arrow_up:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :arrow_up:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow: |
| Jul 15 | `50d1eda` | 4.83 | 14.32 | 8.82 | 15.32 | 0.82 | 209.74 | 64.24 | 13.06 | 5.44 | 114.33 | 203.70 | :left_right_arrow:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow: |
| Jul 14 | `cfe4eef` | 4.87 | 14.47 | 10.73 | 15.40 | 0.84 | 210.71 | 65.23 | 17.08 | 5.36 | 115.38 | 204.63 | :left_right_arrow:  :left_right_arrow:  :arrow_up:  :left_right_arrow:  :arrow_up:  :left_right_arrow:  :left_right_arrow:  :arrow_up:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow: |
| Jul 13 | `7da30f4` | 4.83 | 14.38 | 8.77 | 15.27 | 0.81 | 209.59 | 64.19 | 13.05 | 5.31 | 115.36 | 204.64 | :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow: |
| Jul 12 | `a358abd` | 4.84 | 14.35 | 8.75 | 15.28 | 0.81 | 209.68 | 64.18 | 13.06 | 5.32 | 114.39 | 203.71 | :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :arrow_down:  :left_right_arrow: |
| Jul 11 | `7de33ce` | 4.85 | 14.49 | 8.81 | 15.38 | 0.81 | 210.63 | 65.23 | 13.06 | 5.34 | 118.39 | 204.69 | :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :arrow_down:  :left_right_arrow: |
| Jul 10 | `295f85d` | 4.88 | 14.46 | 8.98 | 15.44 | 0.82 | 210.72 | 65.23 | 13.05 | 5.38 | 128.45 | 205.69 | :left_right_arrow:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :arrow_up:  :left_right_arrow: |
| Jul 09 | `074bb92` | 4.87 | 14.45 | 10.74 | 15.41 | 0.83 | 210.74 | 65.24 | 17.07 | 5.34 | 116.33 | 204.68 | :left_right_arrow:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :arrow_up:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow: |
| Jul 08 | `d7dcdf3` | 4.85 | 14.45 | 11.00 | 15.45 | 0.82 | 210.76 | 65.22 | 16.06 | 5.34 | 116.39 | 204.66 | :left_right_arrow:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow: |
| Jul 08 | `9a6f8e5` | 4.86 | 14.44 | 11.60 | 15.46 | 0.83 | 210.71 | 65.20 | 16.07 | 5.34 | 116.37 | 204.71 | :left_right_arrow:  :left_right_arrow:  :arrow_up:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :arrow_up:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow: |
| Jul 07 | `9a6f8e5` | 4.82 | 14.36 | 8.77 | 15.25 | 2.13 | 210.69 | 64.24 | 13.07 | 5.27 | 115.38 | 203.70 | :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :arrow_up:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow: |
| Jul 07 | `6c1fb8a` | 4.81 | 14.36 | 8.78 | 15.28 | 0.80 | 210.67 | 64.22 | 13.06 | 5.31 | 115.39 | 203.73 | :arrow_down:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow: |
| Jul 06 | `8673e85` | 5.12 | 14.46 | 9.34 | 15.43 | 0.80 | 210.67 | 65.18 | 13.05 | 5.33 | 116.32 | 205.76 | :arrow_up:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow: |
| Jul 05 | `754524d` | 4.87 | 14.57 | 10.80 | 15.44 | 0.82 | 210.75 | 65.23 | 16.07 | 5.34 | 115.38 | 204.67 | :left_right_arrow:  :left_right_arrow:  :arrow_up:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :arrow_up:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow: |
| Jul 04 | `b28bc10` | 4.82 | 14.38 | 8.93 | 15.31 | 0.81 | 210.68 | 64.19 | 13.05 | 5.32 | 115.38 | 204.62 | :left_right_arrow:  :left_right_arrow:  :arrow_down:  :arrow_down:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow: |
| Jul 03 | `75cdaf4` | 4.88 | 14.47 | 29.73 | 24.46 | 0.98 | 210.69 | 65.21 | 17.07 | 5.33 | 116.34 | 204.64 | :left_right_arrow:  :left_right_arrow:  :arrow_up:  :arrow_down:  :arrow_up:  :left_right_arrow:  :left_right_arrow:  :arrow_up:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow: |
| Jul 02 | `a3f6680` | 4.82 | 14.39 | 12.81 | 25.32 | 0.81 | 210.68 | 65.19 | 13.05 | 5.31 | 115.39 | 204.68 | :left_right_arrow:  :arrow_down:  :left_right_arrow:  :arrow_up:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow: |
| Jul 01 | `5b76f55` | 4.85 | 15.09 | 12.91 | 23.97 | 1.45 | 210.75 | 65.19 | 16.07 | 5.35 | 115.37 | 204.71 | :left_right_arrow:  :arrow_up:  :left_right_arrow:  :left_right_arrow:  :arrow_up:  :left_right_arrow:  :left_right_arrow:  :arrow_up:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow: |
| Jun 30 | `bc8b3ab` | 4.89 | 14.49 | 12.90 | 23.80 | 0.82 | 210.72 | 65.25 | 13.06 | 5.33 | 115.36 | 205.74 | -- |

---
*Generated by `generate_diffusion_dashboard.py` in SGLang nightly CI.*
