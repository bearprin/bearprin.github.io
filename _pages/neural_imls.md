---
layout: page
title: Neural-IMLS
permalink: /publications/neural-imls/
description: Self-supervised Implicit Moving Least-Squares Network for Surface Reconstruction (IEEE TVCG 2023)
nav: false
---

<div class="row">
  <div class="col-12 text-center">
    <p>
      <a href="https://arxiv.org/abs/2109.04398" class="btn btn-sm btn-outline-primary mr-2">arXiv</a>
      <a href="https://doi.org/10.1109/TVCG.2023.3284233" class="btn btn-sm btn-outline-primary mr-2">DOI</a>
      <a href="https://ieeexplore.ieee.org/document/10146518" class="btn btn-sm btn-outline-primary mr-2">Paper</a>
      <a href="https://github.com/bearprin/Neural-IMLS" class="btn btn-sm btn-outline-primary">Code</a>
    </p>
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
