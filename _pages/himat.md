---
layout: page
title: "HiMat: DiT-based Ultra-High Resolution SVBRDF Generation"
permalink: /publications/himat/
description: ""
nav: false
---

<div style="text-align: center; margin: 0.5em 0 2em 0;">
  <p style="font-size: 0.98em; line-height: 1.7; margin: 0 auto 1.2em auto; max-width: 760px; color: var(--global-text-color);">
    <strong style="color: var(--global-theme-color);">Zixiong Wang</strong>, Jian Yang, Yiwei Hu, Milo&scaron; Ha&scaron;an, Beibei Wang
  </p>

  <p style="margin-bottom: 1.1em;">
    <a href="https://doi.org/10.1111/cgf.70343" class="btn btn-sm btn-outline-primary mr-2"><i class="fa-solid fa-file-pdf"></i> Paper</a>
    <a href="https://arxiv.org/abs/2508.07011" class="btn btn-sm btn-outline-primary"><i class="fa-solid fa-file-lines"></i> arXiv</a>
  </p>

  <div style="display: inline-block; padding: 0.45em 1.2em; border-radius: 999px; background: rgba(0,128,128,0.1); border: 1px solid var(--global-theme-color); color: var(--global-theme-color); font-weight: 600; font-size: 0.95em; letter-spacing: 0.02em;">
    <i class="fa-solid fa-book-open fa-sm" style="margin-right: 0.45em;"></i>Computer Graphics Forum (Proc. Eurographics) &middot; 2026
  </div>
</div>

<div style="text-align: center;">
  <img src="/assets/img/publications/himat/teaser.png" alt="HiMat teaser" class="img-fluid rounded" />
  <p style="font-size: 0.85em; color: var(--global-text-color-light, #888); margin-top: 0.5em;">
    Figure 1: We present HiMat, a diffusion-based framework generating ultra-high-resolution (4096 &times; 4096) SVBRDF materials from text prompts. Our approach achieves this resolution while preserving high-frequency details crucial for meso-structure components such as normal and height maps. We showcase a variety of materials within a single scene, highlighting the preserved fine-scale details and texture fidelity.
  </p>
</div>

## Abstract

Creating ultra-high-resolution spatially varying bidirectional reflectance functions (SVBRDFs) is critical for photorealistic 3D content creation, to faithfully represent fine-scale surface details required for close-up rendering. However, achieving 4K generation faces two key challenges: (1) the need to synthesize multiple reflectance maps at full resolution, which multiplies the pixel budget and imposes prohibitive memory and computational cost, and (2) the requirement to maintain strong pixel-level alignment across maps at 4K, which is particularly difficult when adapting pretrained models designed for the RGB image domain. We introduce HiMat, a diffusion-based framework tailored for efficient and diverse 4K SVBRDF generation. To address the first challenge, HiMat performs generation in a high-compression latent space via DC-AE, and employs a pretrained diffusion transformer with linear attention to improve per-map efficiency. To address the second challenge, we propose CrossStitch, a lightweight convolutional module that enforces cross-map consistency without incurring the cost of global attention. Our experiments show that HiMat achieves high-fidelity 4K SVBRDF generation with superior efficiency, structural consistency, and diversity compared to prior methods. Beyond materials, our framework also generalizes to related applications such as intrinsic decomposition.

## Method Overview

<div style="text-align: center;">
  <img src="/assets/img/publications/himat/pipeline.png" alt="HiMat pipeline" class="img-fluid rounded" />
  <p style="font-size: 0.85em; color: var(--global-text-color-light, #888); margin-top: 0.5em;">
    Figure 2: Overview. Left: Given text instructions, our framework generates 4K SVBRDF maps through a latent denoising pipeline based on linear DiT (Sec. 4.2), with outputs reconstructed by a deep compression autoencoder (DC-AE) (Sec. 4.2). CrossStitch layers (Sec. 4.3) are integrated into the linear DiT block after each linear attention layer. The combination of linear DiT and DC-AE enables efficient ultra-high-resolution generation, while the CrossStitch design ensures consistency across maps. Right: Architecture of our modified DiT block (cross-attention omitted for clarity). A lightweight convolutional CrossStitch module enables localized feature exchange across maps, ensuring pixel alignment.
  </p>
</div>

Our goal is to train a diffusion-based SVBRDF generator that produces 4K materials from text prompts. High-quality generation requires efficiency, diversity, and consistency across reflectance maps. The key challenges are twofold: (1) each map must be generated at full 4K resolution, and the presence of multiple maps multiplies the pixel budget, leading to prohibitive memory and computational cost, and (2) the maps are physically interdependent and must remain pixel-aligned at 4K, a requirement that is particularly difficult when adapting pretrained image models designed initially for 3-channel RGB inputs rather than multi-channel SVBRDFs.

To address these challenges, HiMat employs a high-compression autoencoder (DC-AE) and a linear-attention diffusion transformer to reduce the effective pixel budget for 4K SVBRDF, substantially lowering memory consumption and computational cost. To address the second issue, HiMat introduces the CrossStitch module: a lightweight convolutional layer integrated into each linear DiT block that enforces cross-map consistency without incurring the cost of global attention.

## Results

<div style="text-align: center;">
  <img src="/assets/img/publications/himat/results_gallery.png" alt="HiMat 4K SVBRDF results" class="img-fluid rounded" />
  <p style="font-size: 0.85em; color: var(--global-text-color-light, #888); margin-top: 0.5em;">
    Figure 7: Additional visual results from HiMat. These examples further demonstrate the diversity, realism, and fine structural details achieved by our method.
  </p>
</div>

## Comparison

<div style="text-align: center;">
  <img src="/assets/img/publications/himat/comparison.png" alt="Visual comparison vs ReflectanceFusion and MatFuse" class="img-fluid rounded" />
  <p style="font-size: 0.85em; color: var(--global-text-color-light, #888); margin-top: 0.5em;">
    Figure 5: Visual comparison between HiMat, ReflectanceFusion [Xue et al. 2024], and MatFuse [Sartor and Peers 2023]. ReflectanceFusion exhibits baked-in lighting artifacts and is limited to a resolution of 256 &times; 256. MatFuse suffers from reduced realism and diversity due to training exclusively on synthetic data at 512 &times; 512 resolution. In contrast, HiMat delivers high-quality 4K materials with fine detail. A slightly tilted camera view is employed in the rendering to visualize the details better.
  </p>
</div>

## Citation

```bibtex
@article{wang2026himat,
  title   = {HiMat: DiT-based Ultra-High Resolution SVBRDF Generation},
  author  = {Wang, Zixiong and Yang, Jian and Hu, Yiwei and Ha{\v{s}}an, Milo{\v{s}} and Wang, Beibei},
  journal = {Computer Graphics Forum (Proc. Eurographics)},
  year    = {2026},
  month   = mar,
  doi     = {10.1111/cgf.70343},
  publisher = {Wiley}
}
```
