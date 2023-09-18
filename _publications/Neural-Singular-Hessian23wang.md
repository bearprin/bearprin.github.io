---
uid: 5
layout: publication
title: "Neural-Singular-Hessian: Implicit Neural Representation of Unoriented Point Clouds by Enforcing Singular Hessian"
authors: <b>Zixiong Wang</b>, Yunxiao Zhang, <a href="https://xrvitd.github.io/" target="_blank">Rui Xu</a>, Fan Zhang, <a href="https://wang-ps.github.io/" target="_blank">Pengshuai Wang</a>, Shuangmin Chen, <a href="http://irc.cs.sdu.edu.cn/~shiqing/index.html" target="_blank">Shiqing Xin</a>, <a href="https://engineering.tamu.edu/cse/profiles/Wang-Wenping.html" target="_blank">Wenping Wang</a>, <a href="http://irc.cs.sdu.edu.cn/~chtu/index.html" target="_blank">Changhe Tu</a>

publication: ACM Transactions on Graphics (TOG), SIGGRAPH Asia 2023
arxiv: https://arxiv.org/abs/2309.01793
pages: true
doi: https://doi.org/10.1145/3618311
paper:
code: https://github.com/bearprin/Neural-Singular-Hessian
slides:
presentation_slides_video:
supplementary:
supplemental_video: https://youtu.be/dGHZjygGssY
---

## Abstract

[//]: # (Basis functions provide both the abilities for compact representation and the properties for efficient computation. Therefore, they are pervasively used in rendering to perform all-frequency shading. However, common basis functions, including spherical harmonics &#40;SH&#41;, wavelets, and spherical Gaussians &#40;SG&#41; all have their own limitations, such as low-frequency for SH, not rotationally invariant for wavelets, and no multiple product support for SG. In this paper, we present neural basis functions, an implicit and data-driven set of basis functions that circumvents the limitations with all desired properties. We first introduce a representation neural network that takes any general 2D spherical function &#40;e.g. environment lighting, BRDF, and visibility&#41; as input and projects it onto the latent space as coefficients of our neural basis functions. Then, we design several lightweight neural networks that perform different types of computation, giving our basis functions different computational properties such as double/triple product integrals and rotations. We demonstrate the practicality of our neural basis functions by integrating them into all-frequency shading applications, showing that our method not only achieves a compression rate of 0.39% and 10×-40× better performance than wavelets at equal quality, but also renders all-frequency lighting effects in real-time without the aforementioned limitations from classic basis functions.)

## Downloads

[//]: # ([Arxiv &#40;23MB&#41;]&#40;{{page.arxiv}}&#41;{: .btn .btn--primary})

[//]: # ([Code &#40;22MB&#41;]&#40;{{page.code}}&#41;{: .btn .btn--primary})

<div style="text-align: center;">
<h2>Video</h2>
<iframe width="448" height=252" src="https://www.youtube.com/embed/dGHZjygGssY?si=Oo1McRc_CYGK6Apz" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

## Comparison Results

### ABC dataset

### Thingi10K dataset

## Cite

```bib
@article{zixiong23neuralsingular,
author = {Zixiong Wang, Yunxiao Zhang, Rui Xu, Fan Zhang, Pengshuai Wang, Shuangmin Chen, Shiqing Xin, Wenping Wang, Changhe Tu},
title = {Neural-Singular-Hessian: Implicit Neural Representation of Unoriented Point Clouds by Enforcing Singular Hessian},
year = {2023},
journal = {ACM Transactions on Graphics (TOG)},
volume = {42},
number = {6},
doi = {10.1145/3618311},
publisher = {ACM}
}
```
