---
uid: 0
layout: publication
title: Restricted Delaunay Triangulation for Explicit Surface Reconstruction
authors: Pengfei Wang, <b>Zixiong Wang</b>, <a href="http://irc.cs.sdu.edu.cn/~shiqing/index.html" target="_blank">Shiqing Xin</a>, <a href="https://gaoxifeng.github.io" target="_blank">Xifeng Gao</a>, <a href="https://engineering.tamu.edu/cse/profiles/Wang-Wenping.html" target="_blank">Wenping Wang</a>, <a href="http://irc.cs.sdu.edu.cn/~chtu/index.html" target="_blank">Changhe Tu</a>

publication: ACM Transactions on Graphics (TOG), 2022
pages:
doi:
paper: https://doi.org/10.1145/3533768
code:
slides:
presentation_slides_video:
supplementary:
supplemental_video:
---

## Abstract

[//]: # (Basis functions provide both the abilities for compact representation and the properties for efficient computation. Therefore, they are pervasively used in rendering to perform all-frequency shading. However, common basis functions, including spherical harmonics &#40;SH&#41;, wavelets, and spherical Gaussians &#40;SG&#41; all have their own limitations, such as low-frequency for SH, not rotationally invariant for wavelets, and no multiple product support for SG. In this paper, we present neural basis functions, an implicit and data-driven set of basis functions that circumvents the limitations with all desired properties. We first introduce a representation neural network that takes any general 2D spherical function &#40;e.g. environment lighting, BRDF, and visibility&#41; as input and projects it onto the latent space as coefficients of our neural basis functions. Then, we design several lightweight neural networks that perform different types of computation, giving our basis functions different computational properties such as double/triple product integrals and rotations. We demonstrate the practicality of our neural basis functions by integrating them into all-frequency shading applications, showing that our method not only achieves a compression rate of 0.39% and 10×-40× better performance than wavelets at equal quality, but also renders all-frequency lighting effects in real-time without the aforementioned limitations from classic basis functions.)

## Downloads

[//]: # ([Paper &#40;23MB&#41;]&#40;{{page.paper}}&#41;{: .btn .btn--primary})
[//]: # ([Supplementary &#40;22MB&#41;]&#40;{{page.supplemental_video}}&#41;{: .btn .btn--primary})

## Cite

```bib
@inproceedings{xu2022lightweight,
  title={Lightweight Neural Basis Functions for All-Frequency Shading},
  author={Xu, Zilin and Zeng, Zheng and Wu, Lifan and Wang, Lu and Yan, Ling-Qi},
  booktitle={SIGGRAPH Asia 2022 Conference Papers},
  pages={1--9},
  year={2022}
}
```
## Copyright Disclaimer
© The Author(s). This is the author’s version of the work. It is posted here for your personal use. Not forredistribution. The definitive Version of Record is available at <a href="{{page.doi}}">DOI</a>.
