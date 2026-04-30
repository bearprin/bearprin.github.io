---
layout: page
title: Neural-Singular-Hessian
permalink: /publications/neural-singular-hessian/
description: Implicit Neural Representation of Unoriented Point Clouds by Enforcing Singular Hessian (SIGGRAPH Asia 2023)
nav: false
---

<div class="row">
  <div class="col-12 text-center">
    <p>
      <a href="https://arxiv.org/abs/2309.01793" class="btn btn-sm btn-outline-primary mr-2">arXiv</a>
      <a href="https://doi.org/10.1145/3618311" class="btn btn-sm btn-outline-primary mr-2">DOI</a>
      <a href="https://github.com/bearprin/Neural-Singular-Hessian" class="btn btn-sm btn-outline-primary mr-2">Code</a>
      <a href="https://youtu.be/dGHZjygGssY" class="btn btn-sm btn-outline-primary">Video</a>
    </p>
  </div>
</div>

## Abstract

Neural implicit representation is a promising approach for reconstructing surfaces from point clouds. Existing methods combine various regularization terms, such as the Eikonal and Laplacian energy terms, to enforce the learned neural function to possess the properties of a Signed Distance Function (SDF). However, inferring the actual topology and geometry of the underlying surface from poor-quality unoriented point clouds remains challenging. In accordance with Differential Geometry, the Hessian of the SDF is singular for points within the differential thin-shell space surrounding the surface. Our approach enforces the Hessian of the neural implicit function to have a zero determinant for points near the surface. This technique aligns the gradients for a near-surface point and its on-surface projection point, producing a rough but faithful shape within just a few iterations. By annealing the weight of the singular-Hessian term, our approach ultimately produces a high-fidelity reconstruction result. Extensive experimental results demonstrate that our approach effectively suppresses ghost geometry and recovers details from unoriented point clouds with better expressiveness than existing fitting-based methods.

## Video

<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; margin: 1.5em 0;">
  <iframe style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"
    src="https://www.youtube.com/embed/dGHZjygGssY?si=Oo1McRc_CYGK6Apz"
    title="Neural-Singular-Hessian video"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    allowfullscreen></iframe>
</div>

## Comparison Results

### SRB dataset

<div style="text-align: center;">
  <img src="/assets/img/publications/neural_singular_hessian/srb_supp.png" alt="SRB dataset comparison" class="img-fluid rounded" />
</div>

### ABC dataset

<div style="text-align: center;">
  <img src="/assets/img/publications/neural_singular_hessian/abc_main.png" alt="ABC dataset comparison" class="img-fluid rounded" />
</div>

### Thingi10K dataset

<div style="text-align: center;">
  <img src="/assets/img/publications/neural_singular_hessian/thingi_main.png" alt="Thingi10K dataset comparison" class="img-fluid rounded" />
</div>

<!-- The original MM page included a commented-out 3D model-viewer embed (Three D Scans / Reconstruction Results) which is not migrated here. -->

## Citation

```bibtex
@article{wang2023neuralsingularhessian,
  title={Neural-Singular-Hessian: Implicit Neural Representation of Unoriented Point Clouds by Enforcing Singular Hessian},
  author={Wang, Zixiong and Zhang, Yunxiao and Xu, Rui and Zhang, Fan and Wang, Pengshuai and Chen, Shuangmin and Xin, Shiqing and Wang, Wenping and Tu, Changhe},
  journal={ACM Transactions on Graphics (Proc. SIGGRAPH Asia)},
  volume={42},
  number={6},
  year={2023},
  publisher={ACM},
  doi={10.1145/3618311}
}
```
