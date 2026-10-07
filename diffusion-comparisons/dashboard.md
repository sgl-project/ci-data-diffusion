# SGLang-Diffusion Nightly Performance Dashboard

*Generated: Oct 07 | Commit: `1e86143`*

*Methodology `client-e2e-v1`: client-side latency through each framework's public API, from submit until the output is downloaded; 1 identical client warmup request(s) per case, discarded. First request = the first request after the server reports ready. Server perf dumps are telemetry only.*

*Excluded 26 historical run(s) from baselines and trends because their measurement methodology or warmup count differs. Missing metadata is not treated as matching explicit metadata.*

> [!WARNING]
> **Performance Regression Detected**
>
> - **ltx2.3_twostage_ti2v_2gpus** (sglang): 19.00s vs 3-run median 14.73s (+29.0%)


## SGLang-Diffusion Performance

| Model | Risk | Client samples | Server samples | First request (s) | sglang median (s) |
|-------|------|----------------|----------------|-------------------|---------|
| Anima-Base-v1.0-Diffusers | ✅ | 3 | 3/3 | 2.67 | **2.47** |
| FLUX.1-dev | ✅ | 3 | 3/3 | 4.29 | **4.30** |
| FLUX.2-dev | ✅ | 3 | 3/3 | 13.23 | **13.02** |
| Qwen-Image-2512 | ✅ | 3 | 3/3 | 8.49 | **8.52** |
| Qwen-Image-Edit-2511 | ✅ | 3 | 3/3 | 14.53 | **14.53** |
| Z-Image-Turbo | ✅ | 3 | 3/3 | 0.71 | **0.69** |
| Wan2.2-T2V-A14B-Diffusers | ✅ | 3 | 3/3 | 206.55 | **206.71** |
| Wan2.2-TI2V-5B-Diffusers | ✅ | 3 | 3/3 | 55.60 | **54.90** |
| LTX-2.3 | ⚠️ | 3 | 3/3 | 19.42 | **19.00** |
| ideogram-4-fp8 | ✅ | 3 | 3/3 | 3.83 | **3.82** |
| Cosmos3-Super | ✅ | 3 | 3/3 | 119.86 | **119.17** |
| Wan2.2-I2V-A14B-Diffusers | ✅ | 3 | 3/3 | 200.96 | **201.00** |
| MiniMax-H3 | ✅ | 3 | 3/3 | 76.91 | **77.23** |

## SGLang Server-Side Breakdown

| Model | Server total (s) | Text encode (s) | Denoise (s) | Decode (s) | Median denoise step (ms) |
|-------|------------------|-----------------|--------------|------------|---------------------------|
| Anima-Base-v1.0-Diffusers | 2.46 | 0.02 | 2.19 | 0.24 | 73.41 |
| FLUX.1-dev | 4.21 | 0.04 | 4.01 | 0.01 | 80.55 |
| FLUX.2-dev | 12.98 | 0.36 | 12.16 | 0.01 | 243.20 |
| Qwen-Image-2512 | 8.46 | 0.23 | 8.21 | 0.01 | 163.51 |
| Qwen-Image-Edit-2511 | 14.46 | N/A | 13.69 | 0.11 | 344.86 |
| Z-Image-Turbo | 0.64 | 0.13 | 0.49 | 0.01 | 56.89 |
| Wan2.2-T2V-A14B-Diffusers | 206.13 | 0.27 | 203.43 | 2.16 | 5089.06 |
| Wan2.2-TI2V-5B-Diffusers | 52.92 | 0.33 | 47.52 | 5.01 | 958.64 |
| LTX-2.3 | 14.89 | 0.40 | 9.93 | 2.56 | 329.38 |
| ideogram-4-fp8 | 3.72 | 0.13 | 3.50 | 0.08 | 177.59 |
| Cosmos3-Super | 118.52 | 0.00 | 115.48 | 2.40 | N/A |
| Wan2.2-I2V-A14B-Diffusers | 200.54 | 0.28 | 194.86 | 2.11 | 4861.43 |
| MiniMax-H3 | 76.59 | 0.06 | 73.97 | 1.19 | 1534.70 |

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


## SGLang Performance Trend (Last 4 Runs)

| Date | Commit | anima_base_t2i_1024 (s) | flux1_dev_t2i_1024 (s) | flux2_dev_t2i_1024 (s) | qwen_image_2512_t2i_1024 (s) | qwen_image_edit_2511 (s) | zimage_turbo_t2i_1024 (s) | wan22_t2v_a14b_720p (s) | wan22_ti2v_5b_720p (s) | ltx2.3_twostage_ti2v_2gpus (s) | ideogram4_fp8_t2i_2gpu (s) | cosmos3_super_t2v_2gpu (s) | wan22_i2v_a14b_720p (s) | minimax_h3_t2va_5s (s) | Trend |
|------|--------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|-------|
| Oct 07 | `1e86143` | 2.47 | 4.30 | 13.02 | 8.52 | 14.53 | 0.69 | 206.71 | 54.90 | 19.00 | 3.82 | 119.17 | 201.00 | 77.23 | :arrow_down:  :arrow_down:  :left_right_arrow:  :arrow_up:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :arrow_up:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow: |
| Oct 05 | `a977e3b` | 3.25 | 4.44 | 13.05 | 8.35 | 14.81 | 0.76 | 206.51 | 55.51 | 13.53 | 3.81 | 118.43 | 200.87 | 77.07 | :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow: |
| Oct 03 | `5b5d721` | 3.26 | 4.47 | 13.02 | 8.37 | 14.83 | 0.76 | 206.80 | 54.51 | 14.73 | 3.81 | 118.51 | 201.10 | 77.44 | :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow: |
| Oct 01 | `41cbe65` | 3.31 | 4.46 | 13.12 | 9.02 | 14.92 | 0.77 | 207.96 | 55.06 | 17.30 | 3.83 | 119.24 | 201.70 | 77.45 | -- |

> [!CAUTION]
> **Action Required — Performance Alert**
>
> The following cases need attention:
> - ltx2.3_twostage_ti2v_2gpus: SGLang regression +29.0% vs 3-run median (19.00s vs 14.73s)


---
*Generated by `generate_diffusion_dashboard.py` in SGLang nightly CI.*
