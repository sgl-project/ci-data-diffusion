# SGLang-Diffusion Nightly Performance Dashboard

*Generated: Oct 25 | Commit: `a99c7d0`*

*Methodology `client-e2e-v1`: client-side latency through each framework's public API, from submit until the output is downloaded; 1 identical client warmup request(s) per case, discarded. First request = the first request after the server reports ready. Server perf dumps are telemetry only.*

*Excluded 14 historical run(s) from baselines and trends because their measurement methodology or warmup count differs. Missing metadata is not treated as matching explicit metadata.*

> [!WARNING]
> **Performance Regression Detected**
>
> - **ltx2.3_twostage_ti2v_2gpus** (sglang): 11.96s vs 5-run median 10.59s (+13.0%)


## SGLang-Diffusion Performance

| Model | Risk | Client samples | Server samples | First request (s) | sglang median (s) |
|-------|------|----------------|----------------|-------------------|---------|
| Anima-Base-v1.0-Diffusers | ✅ | 3 | 3/3 | 2.64 | **2.46** |
| FLUX.1-dev | ✅ | 3 | 3/3 | 4.09 | **4.11** |
| FLUX.2-dev | ✅ | 3 | 3/3 | 13.22 | **12.91** |
| Qwen-Image-2512 | ✅ | 3 | 3/3 | 7.72 | **7.68** |
| Qwen-Image-Edit-2511 | ✅ | 3 | 3/3 | 14.04 | **13.92** |
| Z-Image-Turbo | ✅ | 3 | 3/3 | 0.59 | **0.59** |
| Wan2.2-T2V-A14B-Diffusers | ✅ | 3 | 3/3 | 201.29 | **201.51** |
| Wan2.2-TI2V-5B-Diffusers | ✅ | 3 | 3/3 | 53.56 | **53.56** |
| LTX-2.3 | ⚠️ | 3 | 3/3 | 14.80 | **11.96** |
| ideogram-4-fp8 | ✅ | 3 | 3/3 | 3.74 | **3.72** |
| Cosmos3-Super | ✅ | 3 | 3/3 | 119.31 | **118.76** |
| Wan2.2-I2V-A14B-Diffusers | ✅ | 3 | 3/3 | 194.87 | **195.20** |
| MiniMax-H3 | ✅ | 3 | 3/3 | 74.35 | **74.60** |

## SGLang Server-Side Breakdown

| Model | Server total (s) | Text encode (s) | Denoise (s) | Decode (s) | Median denoise step (ms) |
|-------|------------------|-----------------|--------------|------------|---------------------------|
| Anima-Base-v1.0-Diffusers | 2.44 | 0.02 | 2.19 | 0.22 | 73.50 |
| FLUX.1-dev | 4.01 | 0.02 | 3.98 | 0.01 | 80.10 |
| FLUX.2-dev | 12.87 | 0.36 | 12.05 | 0.01 | 241.01 |
| Qwen-Image-2512 | 7.58 | 0.03 | 7.54 | 0.01 | 151.16 |
| Qwen-Image-Edit-2511 | 13.77 | N/A | 13.50 | 0.02 | 339.84 |
| Z-Image-Turbo | 0.49 | 0.04 | 0.44 | 0.01 | 55.74 |
| Wan2.2-T2V-A14B-Diffusers | 201.46 | 0.28 | 198.94 | 1.80 | 4981.74 |
| Wan2.2-TI2V-5B-Diffusers | 53.50 | 0.13 | 47.02 | 6.31 | 949.58 |
| LTX-2.3 | 11.90 | 0.40 | 9.48 | 0.66 | 313.23 |
| ideogram-4-fp8 | 3.57 | 0.13 | 3.41 | 0.03 | 172.98 |
| Cosmos3-Super | 118.70 | 0.00 | 115.55 | 2.50 | N/A |
| Wan2.2-I2V-A14B-Diffusers | 195.09 | 0.28 | 190.48 | 1.73 | 4752.83 |
| MiniMax-H3 | 74.54 | 0.06 | 72.16 | 1.33 | 1461.65 |

### Latency Trend: anima_base_t2i_1024

![Latency Trend anima_base_t2i_1024](https://raw.githubusercontent.com/sgl-project/ci-data-diffusion/main/diffusion-comparisons/charts/latency_anima_base_t2i_1024.png)


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


## SGLang Performance Trend (Last 16 Runs)

| Date | Commit | anima_base_t2i_1024 (s) | flux1_dev_t2i_1024 (s) | flux2_dev_t2i_1024 (s) | qwen_image_2512_t2i_1024 (s) | qwen_image_edit_2511 (s) | zimage_turbo_t2i_1024 (s) | wan22_t2v_a14b_720p (s) | wan22_ti2v_5b_720p (s) | ltx2.3_twostage_ti2v_2gpus (s) | ideogram4_fp8_t2i_2gpu (s) | cosmos3_super_t2v_2gpu (s) | wan22_i2v_a14b_720p (s) | minimax_h3_t2va_5s (s) | Trend |
|------|--------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|-------|
| Oct 25 | `a99c7d0` | 2.46 | 4.11 | 12.91 | 7.68 | 13.92 | 0.59 | 201.51 | 53.56 | 11.96 | 3.72 | 118.76 | 195.20 | 74.60 | :left_right_arrow:  :arrow_down:  :left_right_arrow:  :arrow_down:  :arrow_down:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :arrow_up:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow: |
| Oct 23 | `02b9836` | 2.43 | 4.25 | 12.94 | 7.87 | 14.22 | 0.68 | 202.65 | 54.06 | 9.86 | 3.81 | 118.59 | 197.76 | 74.55 | :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow: |
| Oct 21 | `8e3e298` | 2.45 | 4.28 | 13.00 | 7.89 | 14.31 | 0.68 | 202.61 | 54.42 | 10.35 | 3.83 | 119.29 | 197.40 | 74.68 | :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow: |
| Oct 21 | `62cee1b` | 2.47 | 4.28 | 12.99 | 8.00 | 14.33 | 0.68 | 202.42 | 54.45 | 11.85 | 3.82 | 119.18 | 196.89 | 74.60 | :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :arrow_up:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow: |
| Oct 19 | `62cee1b` | 2.43 | 4.25 | 12.97 | 7.86 | 14.23 | 0.68 | 203.61 | 54.01 | 10.59 | 3.80 | 118.43 | 197.66 | 74.49 | :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow: |
| Oct 17 | `4eb606b` | 2.47 | 4.25 | 13.05 | 8.14 | 14.36 | 0.68 | 202.61 | 54.38 | 13.19 | 3.82 | 119.47 | 197.38 | 74.75 | :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :arrow_up:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :arrow_up:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow: |
| Oct 15 | `c4870d9` | 2.42 | 4.26 | 12.93 | 7.86 | 14.26 | 0.68 | 202.83 | 54.01 | 10.24 | 3.80 | 118.31 | 197.52 | 74.50 | :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow: |
| Oct 14 | `684fea8` | 2.45 | 4.27 | 13.03 | 8.27 | 14.35 | 0.69 | 203.06 | 54.64 | 10.68 | 3.83 | 119.73 | 197.32 | 74.66 | :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :arrow_up:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow: |
| Oct 13 | `27b6830` | 2.44 | 4.29 | 13.00 | 7.91 | 14.32 | 0.69 | 203.50 | 54.73 | 10.55 | 3.83 | 119.53 | 197.63 | 74.62 | :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow: |
| Oct 11 | `11bfd86` | 2.45 | 4.28 | 13.04 | 8.12 | 14.60 | 0.70 | 203.29 | 54.76 | 11.40 | 3.84 | 119.63 | 197.92 | 74.77 | :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow: |
| Oct 11 | `89e24e7` | 2.45 | 4.29 | 13.06 | 8.12 | 14.56 | 0.69 | 203.14 | 54.75 | 11.91 | 3.83 | 119.53 | 197.82 | 74.69 | :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow: |
| Oct 09 | `1203eb9` | 2.44 | 4.29 | 13.01 | 8.12 | 14.57 | 0.69 | 207.26 | 54.70 | 11.71 | 3.84 | 119.45 | 201.08 | 74.89 | :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :arrow_down: |
| Oct 07 | `1e86143` | 2.47 | 4.30 | 13.02 | 8.52 | 14.53 | 0.69 | 206.71 | 54.90 | 19.00 | 3.82 | 119.17 | 201.00 | 77.23 | :arrow_down:  :arrow_down:  :left_right_arrow:  :arrow_up:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :arrow_up:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow: |
| Oct 05 | `a977e3b` | 3.25 | 4.44 | 13.05 | 8.35 | 14.81 | 0.76 | 206.51 | 55.51 | 13.53 | 3.81 | 118.43 | 200.87 | 77.07 | :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow: |
| Oct 03 | `5b5d721` | 3.26 | 4.47 | 13.02 | 8.37 | 14.83 | 0.76 | 206.80 | 54.51 | 14.73 | 3.81 | 118.51 | 201.10 | 77.44 | :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow: |
| Oct 01 | `41cbe65` | 3.31 | 4.46 | 13.12 | 9.02 | 14.92 | 0.77 | 207.96 | 55.06 | 17.30 | 3.83 | 119.24 | 201.70 | 77.45 | -- |

> [!CAUTION]
> **Action Required — Performance Alert**
>
> The following cases need attention:
> - ltx2.3_twostage_ti2v_2gpus: SGLang regression +13.0% vs 5-run median (11.96s vs 10.59s)


---
*Generated by `generate_diffusion_dashboard.py` in SGLang nightly CI.*
