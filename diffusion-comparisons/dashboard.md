# SGLang-Diffusion Nightly Performance Dashboard

*Generated: Sep 21 | Commit: `50ec970`*

> [!WARNING]
> **Incomplete Server Telemetry**
>
> Client-side latency includes every measured request, but server-side stage medians use only the readable perf dumps.
> - **FLUX.2-dev**: 1/3 server samples available
> - **Wan2.2-T2V-A14B-Diffusers**: 1/3 server samples available
> - **Wan2.2-I2V-A14B-Diffusers**: 1/3 server samples available


## SGLang-Diffusion Performance

| Model | Risk | Client samples | Server samples | sglang median (s) |
|-------|------|----------------|----------------|---------|
| FLUX.1-dev | ✅ | 3 | 3/3 | **4.45** |
| FLUX.2-dev | ✅ | 3 | 1/3 | **13.25** |
| Qwen-Image-2512 | ✅ | 3 | 3/3 | **8.36** |
| Qwen-Image-Edit-2511 | ✅ | 3 | 3/3 | **14.84** |
| Z-Image-Turbo | ✅ | 3 | 3/3 | **0.78** |
| Wan2.2-T2V-A14B-Diffusers | ✅ | 3 | 1/3 | **207.61** |
| Wan2.2-TI2V-5B-Diffusers | ✅ | 3 | 3/3 | **55.17** |
| LTX-2.3 | ✅ | 3 | 3/3 | **14.05** |
| ideogram-4-fp8 | ✅ | 3 | 3/3 | **3.80** |
| Cosmos3-Super | ✅ | 3 | 3/3 | **118.39** |
| Wan2.2-I2V-A14B-Diffusers | ✅ | 3 | 1/3 | **201.65** |
| MiniMax-H3 | ✅ | 3 | 3/3 | **77.24** |

## SGLang Server-Side Breakdown

| Model | Server total (s) | Text encode (s) | Denoise (s) | Decode (s) | Median denoise step (ms) |
|-------|------------------|-----------------|--------------|------------|---------------------------|
| FLUX.1-dev | 4.30 | 0.04 | 4.10 | 0.02 | 82.62 |
| FLUX.2-dev | 13.11 | 0.37 | 12.27 | 0.02 | 245.09 |
| Qwen-Image-2512 | 8.27 | 0.23 | 7.97 | 0.06 | 160.19 |
| Qwen-Image-Edit-2511 | 14.76 | N/A | 14.00 | 0.10 | 351.36 |
| Z-Image-Turbo | 0.63 | 0.13 | 0.49 | 0.01 | 56.30 |
| Wan2.2-T2V-A14B-Diffusers | 206.10 | 0.06 | 203.46 | 2.25 | 5075.92 |
| Wan2.2-TI2V-5B-Diffusers | 53.79 | 0.33 | 47.93 | 5.47 | 966.58 |
| LTX-2.3 | 11.83 | 0.40 | 8.50 | 0.96 | 281.20 |
| ideogram-4-fp8 | 3.70 | 0.13 | 3.49 | 0.08 | 177.90 |
| Cosmos3-Super | 117.78 | 0.00 | 114.84 | 2.38 | N/A |
| Wan2.2-I2V-A14B-Diffusers | 201.09 | 0.19 | 194.84 | 2.35 | 4859.80 |
| MiniMax-H3 | 76.57 | 0.05 | 73.91 | 1.30 | 1533.78 |

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
| Sep 21 | `50ec970` | 4.45 | 13.25 | 8.36 | 14.84 | 0.78 | 207.61 | 55.17 | 14.05 | 3.80 | 118.39 | 201.65 | 77.24 |            |
|  | `?` | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |            |
| Sep 19 | `76f9213` | 4.47 | 13.37 | 9.04 | 14.93 | 0.76 | 207.69 | 56.18 | 17.07 | 3.82 | 119.38 | 201.66 | 77.24 | :left_right_arrow:  :left_right_arrow:  :arrow_up:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :arrow_up:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow: |
| Sep 17 | `7ccbf5f` | 4.50 | 13.34 | 8.39 | 14.93 | 0.80 | 206.79 | 56.23 | 13.06 | 3.87 | 119.47 | 201.57 | 78.22 | :left_right_arrow:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :arrow_up:  :left_right_arrow:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow: |
| Sep 15 | `832ec39` | 4.44 | 13.36 | 9.35 | 14.94 | 0.77 | 207.68 | 56.18 | 16.06 | 3.85 | 119.41 | 201.67 | 78.24 | :left_right_arrow:  :left_right_arrow:  :arrow_up:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :arrow_up:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow: |
| Sep 13 | `7f1f8c7` | 4.48 | 13.37 | 8.39 | 14.92 | 0.77 | 207.72 | 56.19 | 13.06 | 3.84 | 119.41 | 202.63 | 78.24 | :left_right_arrow:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow: |
| Sep 11 | `ab9750f` | 4.44 | 13.34 | 10.26 | 15.18 | 0.77 | 207.62 | 56.19 | 29.11 | 3.84 | 119.41 | 201.67 | 78.24 | :left_right_arrow:  :left_right_arrow:  :arrow_up:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :arrow_up:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow: |
| Sep 09 | `ffe98a4` | 4.42 | 13.29 | 8.48 | 15.17 | 0.76 | 206.71 | 55.20 | 14.06 | 3.82 | 118.42 | 201.67 | 77.26 | :left_right_arrow:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow: |
| Sep 09 | `0ee8e41` | 4.43 | 13.34 | 10.03 | 15.18 | 0.80 | 207.69 | 56.20 | 16.07 | 3.83 | 120.38 | 201.67 | 78.25 | :left_right_arrow:  :left_right_arrow:  :arrow_up:  :left_right_arrow:  :arrow_up:   :left_right_arrow:   :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow: |
| Sep 07 | `b5c9b68` | 4.48 | 13.36 | 8.54 | 15.39 | 0.76 | N/A | 56.18 | N/A | 3.83 | 119.39 | 201.68 | 78.25 | :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:   :left_right_arrow:   :left_right_arrow:  :left_right_arrow:   :left_right_arrow: |
| Sep 05 | `dc28438` | 4.52 | 13.32 | 8.51 | 15.13 | 0.77 | 207.69 | 56.16 | N/A | 3.84 | 119.39 | N/A | 78.22 | :arrow_down:  :arrow_down:  :arrow_down:  :arrow_down:  :arrow_down:  :left_right_arrow:  :left_right_arrow:   :arrow_down:  :left_right_arrow:   :left_right_arrow: |
| Sep 01 | `00689c0` | 4.65 | 13.70 | 9.95 | 16.95 | 0.97 | 206.71 | 57.21 | 17.09 | 4.06 | 121.35 | 201.69 | 77.27 | :left_right_arrow:  :left_right_arrow:  :arrow_up:  :left_right_arrow:  :arrow_up:  :left_right_arrow:  :left_right_arrow:  :arrow_up:  :arrow_down:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow: |
| Aug 31 | `52e1c24` | 4.63 | 13.59 | 8.74 | 16.81 | 0.95 | 207.67 | 57.17 | 14.06 | 4.25 | 120.38 | 201.71 | 77.24 | :arrow_down:  :left_right_arrow:  :arrow_down:  :arrow_up:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :arrow_down:  :arrow_up:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow: |
| Aug 29 | `cdbfe90` | 5.13 | 13.71 | 10.59 | 16.00 | 0.96 | 206.73 | 57.16 | 17.07 | 4.15 | 120.40 | 202.66 | 77.23 | :arrow_up:  :left_right_arrow:  :arrow_up:  :arrow_up:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :arrow_up:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow:  :left_right_arrow: |
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
| Aug 05 | `4e7209c` | 4.86 | 14.50 | 8.95 | 15.41 | 0.81 | 207.66 | 64.23 | 13.06 | 5.34 | 115.34 | 201.65 | N/A | -- |

---
*Generated by `generate_diffusion_dashboard.py` in SGLang nightly CI.*
