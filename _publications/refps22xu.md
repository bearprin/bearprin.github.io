---
uid: 1
layout: publication
title: "RFEPS: Reconstructing Feature-line Equipped Polygonal Surface"
authors: <a href="https://xrvitd.github.io/" target="_blank">Rui Xu</a>, <b>Zixiong Wang</b>, <a href="https://frank-zy-dou.github.io/" target="_blank">Zhiyang Dou</a>, Chen Zong, <a href="http://irc.cs.sdu.edu.cn/~shiqing/index.html" target="_blank">Shiqing Xin</a>, Mingyan Jiang, <a href="https://www.cs.wustl.edu/~taoju/" target="_blank">Tao Ju</a>, <a href="http://irc.cs.sdu.edu.cn/~chtu/index.html" target="_blank">Changhe Tu</a>


publication: ACM Transactions on Graphics (TOG), SIGGRAPH Asia 2022
pages: https://xrvitd.github.io/Projects/RFEPS/index.html
doi: 
paper: https://arxiv.org/abs/2212.03600
code: https://github.com/Xrvitd/RFEPS
slides:
presentation_slides_video:
supplementary:
supplemental_video: https://www.youtube.com/watch?v=iRP5z-JOCEc
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
