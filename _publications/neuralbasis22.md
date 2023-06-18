---
uid: 4
layout: publication
title: Lightweight Neural Basis Functions for All-Frequency Shading
authors: <a href="https://starry316.github.io/" target="_blank">Zilin Xu</a>, <b>Zheng Zeng</b>, <a href="https://winmad.github.io/" target="_blank">Lifan Wu</a>, <a href="http://vr.sdu.edu.cn/info/1010/1060.htm" target="_blank">Lu Wang</a>, <a href="https://sites.cs.ucsb.edu/~lingqi/" target="_blank">Ling-Qi Yan</a>

publication: SIGGRAPH ASIA 2022
pages: true
doi: https://doi.org/10.1145/3550469.3555386
paper: http://sites.cs.ucsb.edu/~lingqi/publications/paper_neural_basis.pdf
code:
slides:
presentation_slides_video:
supplementary: http://sites.cs.ucsb.edu/~lingqi/publications/supplementary_neural_basis.pdf
supplemental_video:
---

## Abstract

Basis functions provide both the abilities for compact representation and the properties for efficient computation. Therefore, they are pervasively used in rendering to perform all-frequency shading. However, common basis functions, including spherical harmonics (SH), wavelets, and spherical Gaussians (SG) all have their own limitations, such as low-frequency for SH, not rotationally invariant for wavelets, and no multiple product support for SG. In this paper, we present neural basis functions, an implicit and data-driven set of basis functions that circumvents the limitations with all desired properties. We first introduce a representation neural network that takes any general 2D spherical function (e.g. environment lighting, BRDF, and visibility) as input and projects it onto the latent space as coefficients of our neural basis functions. Then, we design several lightweight neural networks that perform different types of computation, giving our basis functions different computational properties such as double/triple product integrals and rotations. We demonstrate the practicality of our neural basis functions by integrating them into all-frequency shading applications, showing that our method not only achieves a compression rate of 0.39% and 10×-40× better performance than wavelets at equal quality, but also renders all-frequency lighting effects in real-time without the aforementioned limitations from classic basis functions.

## Downloads

[Paper (23MB)]({{page.paper}}){: .btn .btn--primary}
[Supplementary (22MB)]({{page.supplemental_video}}){: .btn .btn--primary}

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
