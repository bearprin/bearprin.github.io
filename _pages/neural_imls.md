---
layout: page
title: "Neural-IMLS: Self-supervised Implicit Moving Least-Squares Network for Surface Reconstruction"
permalink: /publications/neural-imls/
description: ""
nav: false
---

<div style="text-align: center; margin: 0.5em 0 2em 0;">
  <p style="font-size: 0.98em; line-height: 1.7; margin: 0 auto 1.2em auto; max-width: 760px; color: var(--global-text-color);">
    <strong style="color: var(--global-theme-color);">Zixiong Wang</strong>, Pengfei Wang, Pengshuai Wang, Qiujie Dong, Junjie Gao, Shuangmin Chen, Shiqing Xin, Changhe Tu, Wenping Wang
  </p>

  <p style="margin-bottom: 1.1em;">
    <a href="https://doi.org/10.1109/TVCG.2023.3284233" class="btn btn-sm btn-outline-primary mr-2"><i class="fa-solid fa-file-pdf"></i> Paper</a>
    <a href="https://arxiv.org/abs/2109.04398" class="btn btn-sm btn-outline-primary mr-2"><i class="fa-solid fa-file-lines"></i> arXiv</a>
    <a href="https://github.com/bearprin/Neural-IMLS" class="btn btn-sm btn-outline-primary"><i class="fa-brands fa-github"></i> Code</a>
  </p>

  <div style="display: inline-block; padding: 0.45em 1.2em; border-radius: 999px; background: rgba(0,128,128,0.1); border: 1px solid var(--global-theme-color); color: var(--global-theme-color); font-weight: 600; font-size: 0.95em; letter-spacing: 0.02em;">
    <i class="fa-solid fa-book-open fa-sm" style="margin-right: 0.45em;"></i>IEEE Transactions on Visualization and Computer Graphics &middot; 2023
  </div>
</div>

<div style="text-align: center; margin: 1.5em 0;">
  <img src="/assets/img/publications/neural_imls/teaser.png" alt="Neural-IMLS teaser" class="img-fluid rounded" />
</div>

## Abstract

Surface reconstruction is a challenging task when input point clouds, especially real scans, are noisy and lack normals. Observing that the Multilayer Perceptron (MLP) and the implicit moving least-square function (IMLS) provide a dual representation of the underlying surface, we introduce Neural-IMLS, a novel approach that directly learns a noise-resistant signed distance function (SDF) from unoriented raw point clouds in a self-supervised manner. In particular, IMLS regularizes MLP by providing estimated SDFs near the surface and helps enhance its ability to represent geometric details and sharp features, while MLP regularizes IMLS by providing estimated normals. We prove that at convergence, our neural network produces a faithful SDF whose zero-level set approximates the underlying surface due to the mutual learning mechanism between the MLP and the IMLS. Extensive experiments on various benchmarks, including synthetic and real scans, show that Neural-IMLS can reconstruct faithful shapes even with noise and missing parts. The source code can be found at [URL](https://github.com/bearprin/Neural-IMLS).

## Citation

```bibtex
@article{wang2023neuralimls,
  title={Neural-IMLS: Self-supervised Implicit Moving Least-Squares Network for Surface Reconstruction},
  author={Wang, Zixiong and Wang, Pengfei and Wang, Pengshuai and Dong, Qiujie and Gao, Junjie and Chen, Shuangmin and Xin, Shiqing and Tu, Changhe and Wang, Wenping},
  journal={IEEE Transactions on Visualization and Computer Graphics},
  year={2023},
  pages={1--16},
  doi={10.1109/TVCG.2023.3284233}
}
```
