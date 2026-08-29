# SGLang-Diffusion Nightly Performance Dashboard

*Generated: Aug 29 | Commit: `cdbfe90`*

## SGLang-Diffusion Performance

| Model | Risk | sglang (s) |
|-------|------|---------|
| FLUX.1-dev | ⚠️ | **5.13** |
| FLUX.2-dev | ✅ | **13.71** |
| Qwen-Image-2512 | ⚠️ | **10.59** |
| Qwen-Image-Edit-2511 | ✅ | **16.00** |
| Z-Image-Turbo | ✅ | **0.96** |
| Wan2.2-T2V-A14B-Diffusers | ✅ | **206.73** |
| Wan2.2-TI2V-5B-Diffusers | ✅ | **57.16** |
| LTX-2.3 | ⚠️ | **17.07** |
| ideogram-4-fp8 | ✅ | **4.15** |
| Cosmos3-Super | ✅ | **120.40** |
| Wan2.2-I2V-A14B-Diffusers | ✅ | **202.66** |
| MiniMax-H3 | ✅ | **77.23** |

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


### Latency Trend: minimax_h3_t2va_5s

![Latency Trend minimax_h3_t2va_5s](https://raw.githubusercontent.com/sgl-project/ci-data-diffusion/main/diffusion-comparisons/charts/latency_minimax_h3_t2va_5s.png)


## SGLang Performance Trend (Last 30 Runs)

| Date | Commit | flux1_dev_t2i_1024 (s) | flux2_dev_t2i_1024 (s) | qwen_image_2512_t2i_1024 (s) | qwen_image_edit_2511 (s) | zimage_turbo_t2i_1024 (s) | wan22_t2v_a14b_720p (s) | wan22_ti2v_5b_720p (s) | ltx2.3_twostage_ti2v_2gpus (s) | ideogram4_fp8_t2i_2gpu (s) | cosmos3_super_t2v_2gpu (s) | wan22_i2v_a14b_720p (s) | minimax_h3_t2va_5s (s) | Trend |
|------|--------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|-------|
| Aug 29 | `cdbfe90` | 5.13 | 13.71 | 10.59 | 16.00 | 0.96 | 206.73 | 57.16 | 17.07 | 4.15 | 120.40 | 202.66 | 77.23 |            |
|  | `?` | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |            |
| Aug 27 | `20a491d` | 4.58 | 13.49 | 8.90 | 15.26 | 0.95 | 206.73 | 56.17 | 14.06 | 4.12 | 119.41 | 200.67 | 77.26 | :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow: |
| Aug 25 | `46d9427` | 4.62 | 13.60 | 8.98 | 15.39 | 0.94 | 207.74 | 56.19 | 14.07 | 4.13 | 120.39 | 201.67 | 77.22 | :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :arrow_up:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow: |
| Aug 23 | `de6a1db` | 4.61 | 13.47 | 8.90 | 15.54 | 0.94 | 206.72 | 56.17 | 13.06 | 4.17 | 119.35 | 200.69 | 77.22 | :left_right_arrow:  :left_right_arrow:  :arrow_down:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow: |
| Aug 21 | `a41da99` | 4.70 | 13.55 | 10.33 | 15.86 | 0.95 | 207.72 | 56.22 | 17.07 | 4.19 | 119.38 | 201.54 | 77.22 | :arrow_up:  :left_right_arrow:  :arrow_up:  :left_right_arrow:  :arrow_up:  :left_right_arrow:  :left_right_arrow:  :arrow_up:  :arrow_up:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow: |
| Aug 19 | `23f2320` | 4.44 | 13.38 | 8.84 | 15.68 | 0.78 | 207.75 | 56.19 | 13.05 | 3.98 | 119.37 | 201.65 | 77.21 | :left_right_arrow:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow: |
| Aug 19 | `e0ae2e7` | 4.45 | 13.38 | 10.06 | 15.44 | 0.79 | 207.60 | 56.17 | 17.07 | 4.00 | 119.34 | 201.56 | 77.28 | :left_right_arrow:  :left_right_arrow:  :arrow_up:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :arrow_up:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow: |
| Aug 18 | `0111b29` | 4.44 | 13.39 | 8.88 | 15.46 | 0.84 | 206.69 | 56.20 | 13.06 | 3.98 | 119.39 | 201.65 | 78.24 | :left_right_arrow:  :left_right_arrow:  :arrow_down:  :arrow_down:  :arrow_up:  :left_right_arrow:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :arrow_down:  :left_right_arrow: |
| Aug 18 | `af74337` | 4.47 | 13.40 | 10.12 | 15.85 | 0.81 | 206.62 | 57.22 | 16.08 | 3.99 | 119.41 | 256.85 | 77.27 | :arrow_down:  :left_right_arrow:  :arrow_up:  :arrow_up:  :arrow_up:  :left_right_arrow:  :left_right_arrow:  :arrow_up:  :left_right_arrow:  :arrow_up:  :arrow_up:  :left_right_arrow: |
| Aug 15 | `e331baa` | 4.57 | 13.44 | 8.80 | 15.38 | 0.78 | 206.70 | 56.15 | 13.05 | 4.06 | 115.33 | 201.58 | 77.22 | :arrow_up:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow: |
| Aug 15 | `8720a72` | 4.44 | 13.30 | 9.81 | 15.39 | 0.78 | 206.64 | 56.16 | 16.06 | 4.08 | 115.32 | 200.62 | 77.19 | :arrow_down:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :arrow_down:  :left_right_arrow: |
| Aug 13 | `07821e9` | 5.57 | 15.73 | 9.81 | 15.38 | 0.78 | 206.72 | 56.17 | 16.07 | 4.08 | 115.34 | 206.69 | 77.26 | :left_right_arrow:  :arrow_down:  :arrow_up:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :arrow_down:  :arrow_up:  :left_right_arrow:  :left_right_arrow:  :arrow_up:  |
| Aug 12 | `9dbe519` | 5.58 | 16.76 | 8.80 | 15.61 | 0.77 | 207.69 | 64.19 | 14.06 | 4.11 | 115.41 | 201.76 | N/A | :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  |
| Aug 12 | `b20c375` | 5.58 | 16.60 | 8.74 | 15.53 | 0.77 | 206.73 | 63.24 | 14.06 | 4.09 | 115.37 | 200.69 | N/A | :arrow_up:  :arrow_up:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :arrow_down:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  |
| Aug 08 | `b839085` | 4.48 | 14.27 | 11.31 | 15.74 | 0.78 | 206.62 | 64.17 | 17.07 | 5.39 | 115.29 | 201.56 | N/A | :arrow_down:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  |
| Aug 08 | `3a5720d` | 4.71 | 14.65 | 11.42 | 15.77 | 0.79 | 286.79 | 64.19 | 17.08 | 5.40 | 115.29 | 201.74 | N/A | :arrow_down:  :left_right_arrow:  :arrow_up:  :arrow_up:  :arrow_down:  :arrow_up:  :left_right_arrow:  :arrow_up:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  |
| Aug 05 | `4e7209c` | 4.86 | 14.50 | 8.95 | 15.41 | 0.81 | 207.66 | 64.23 | 13.06 | 5.34 | 115.34 | 201.65 | N/A | :left_right_arrow:  :left_right_arrow:  :arrow_down:  :arrow_down:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :arrow_down:  |
| Aug 04 | `34af3ff` | 4.85 | 14.46 | 10.65 | 15.77 | 0.83 | 209.72 | 64.20 | 16.07 | 5.36 | 115.40 | 216.79 | N/A | :left_right_arrow:  :left_right_arrow:  :arrow_up:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :arrow_up:  :left_right_arrow:  :left_right_arrow:  :arrow_up:  |
| Aug 03 | `0ba46c8` | 4.85 | 14.47 | 8.86 | 15.65 | 0.81 | 208.68 | 65.22 | 14.07 | 5.33 | 115.34 | 202.65 | N/A | :left_right_arrow:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  |
| Aug 01 | `ae84811` | 4.85 | 14.47 | 11.06 | 15.42 | 0.96 | 208.76 | 64.22 | 16.07 | 5.36 | 115.41 | 204.69 | N/A | :left_right_arrow:  :left_right_arrow:  :arrow_up:  :left_right_arrow:  :arrow_up:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  |
| Jul 31 | `5f9b0db` | 4.86 | 14.72 | 10.74 | 15.52 | 0.82 | 208.70 | 65.24 | 16.08 | 5.34 | 115.41 | 202.77 | N/A | :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  |
| Jul 29 | `e1f2f9d` | 4.87 | 14.49 | 10.53 | 15.42 | 0.82 | 210.65 | 64.21 | 16.07 | 5.37 | 115.32 | 203.71 | N/A | :left_right_arrow:  :left_right_arrow:  :arrow_up:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :arrow_up:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  |
| Jul 27 | `8d6549b` | 4.84 | 14.36 | 8.75 | 15.30 | 0.81 | 210.75 | 64.24 | 13.06 | 5.40 | 115.34 | 204.72 | N/A | :arrow_down:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  |
| Jul 25 | `e943e60` | 4.95 | 14.46 | 10.50 | 15.44 | 0.83 | 211.76 | 65.23 | 16.08 | 5.35 | 116.35 | 205.66 | N/A | :arrow_down:  :left_right_arrow:  :arrow_up:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :arrow_up:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  |
| Jul 23 | `b98a577` | 5.27 | 14.51 | 8.82 | 15.41 | 0.83 | 210.72 | 65.23 | 13.06 | 5.33 | 116.40 | 205.68 | N/A | :arrow_up:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :arrow_up:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  |
| Jul 20 | `b3570a4` | 4.83 | 14.33 | 8.80 | 15.26 | 0.81 | 210.73 | 65.25 | 13.06 | 5.31 | 115.38 | 203.68 | N/A | :left_right_arrow:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  |
| Jul 19 | `99f5a6f` | 4.85 | 14.43 | 10.96 | 15.41 | 0.86 | 210.72 | 65.21 | 16.07 | 5.35 | 115.39 | 203.71 | N/A | :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :arrow_up:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:   :left_right_arrow:  :left_right_arrow:  |
| Jul 18 | `e48eabb` | 4.86 | 14.41 | 10.86 | 15.41 | 0.83 | 210.72 | 65.23 | 16.08 | N/A | 115.29 | 203.68 | N/A | :left_right_arrow:  :left_right_arrow:  :arrow_up:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :arrow_up:   :left_right_arrow:  :left_right_arrow:  |
| Jul 17 | `dc0b3eb` | 4.85 | 14.48 | 9.02 | 15.41 | 0.83 | 210.69 | 65.20 | 13.05 | 5.31 | 115.32 | 204.58 | N/A | -- |

> [!CAUTION]
> **Action Required — Performance Alert**
>
> The following cases need attention:
> - flux1_dev_t2i_1024: SGLang regression +11.4% vs 3-run avg (5.13s vs 4.60s)
> - qwen_image_2512_t2i_1024: SGLang regression +18.5% vs 3-run avg (10.59s vs 8.94s)
> - ltx2.3_twostage_ti2v_2gpus: SGLang regression +21.4% vs 3-run avg (17.07s vs 14.06s)


---
*Generated by `generate_diffusion_dashboard.py` in SGLang nightly CI.*
