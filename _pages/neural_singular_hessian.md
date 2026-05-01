---
layout: page
title: "Neural-Singular-Hessian: Implicit Neural Representation of Unoriented Point Clouds by Enforcing Singular Hessian"
permalink: /publications/neural-singular-hessian/
description: ""
nav: false
---

<div style="text-align: center; margin: 0.5em 0 2em 0;">
  <p style="font-size: 0.98em; line-height: 1.7; margin: 0 auto 1.2em auto; max-width: 760px; color: var(--global-text-color);">
    <strong style="color: var(--global-theme-color);">Zixiong Wang</strong>, Yunxiao Zhang, <a href="https://xrvitd.github.io/">Rui Xu</a>, Fan Zhang, <a href="https://wang-ps.github.io/">Pengshuai Wang</a>, Shuangmin Chen, <a href="http://irc.cs.sdu.edu.cn/~shiqing/index.html">Shiqing Xin</a>, <a href="https://engineering.tamu.edu/cse/profiles/Wang-Wenping.html">Wenping Wang</a>, <a href="http://irc.cs.sdu.edu.cn/~chtu/index.html">Changhe Tu</a>
  </p>

  <p style="margin-bottom: 1.1em;">
    <a href="https://doi.org/10.1145/3618311" class="btn btn-sm btn-outline-primary mr-2"><i class="fa-solid fa-file-pdf"></i> Paper</a>
    <a href="https://arxiv.org/abs/2309.01793" class="btn btn-sm btn-outline-primary mr-2"><i class="fa-solid fa-file-lines"></i> arXiv</a>
    <a href="https://github.com/bearprin/Neural-Singular-Hessian" class="btn btn-sm btn-outline-primary mr-2"><i class="fa-brands fa-github"></i> Code</a>
    <a href="https://youtu.be/dGHZjygGssY" class="btn btn-sm btn-outline-primary"><i class="fa-brands fa-youtube"></i> Video</a>
  </p>

  <div style="display: inline-block; padding: 0.45em 1.2em; border-radius: 999px; background: rgba(0,128,128,0.1); border: 1px solid var(--global-theme-color); color: var(--global-theme-color); font-weight: 600; font-size: 0.95em; letter-spacing: 0.02em;">
    <i class="fa-solid fa-book-open fa-sm" style="margin-right: 0.45em;"></i>ACM Transactions on Graphics (Proc. SIGGRAPH Asia) &middot; 2023
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
