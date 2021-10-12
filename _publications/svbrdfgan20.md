---
uid: 1
layout: publication
title: Joint SVBRDF Recovery and Synthesis From a Single Image using an Unsupervised Generative Adversarial Network
authors: Yezi Zhao, <a href="https://wangningbei.github.io/" target="_blank">Beibei Wang</a>, <a href="hhttp://vr.sdu.edu.cn/info/1010/1062.htm" target="_blank"> Yanning Xu</a>, <b>Zheng Zeng</b>, <a href="http://vr.sdu.edu.cn/info/1010/1062.htm" target="_blank"> Yanning Xu</a>, <a href="http://vr.sdu.edu.cn/info/1010/1060.htm" target="_blank"> Lu Wang</a>, <a href="http://maverick.inria.fr/Membres/Nicolas.Holzschuch/" target="_blank"> Nicolas Holzschuch</a>
publication: Eurographics Symposium on Rendering 2020
doi: https://doi.org/10.2312/sr.20201136
paper: /assets/files/egsr2020-svbrdf-gan.pdf
code: https://github.com/mengshu1996/SVBRDF-GAN
slides:
presentation_slides_video:
supplementary:
supplemental_video:
---

## Abstract

We want to recreate spatially-varying bi-directional reflectance distribution functions (SVBRDFs) from a single image. Pro-ducing these SVBRDFs from single images will allow designers to incorporate many new materials in their virtual scenes,increasing their realism. A single image contains incomplete information about the SVBRDF, making reconstruction difficult.Existing algorithms can produce high-quality SVBRDFs with single or few input photographs using supervised deep learning.The learning step relies on a huge dataset with both input photographs and the ground truth SVBRDF maps. This is a weaknessas ground truth maps are not easy to acquire. For practical use, it is also important to produce large SVBRDF maps. Existingalgorithms rely on a separate texture synthesis step to generate these large maps, which leads to the loss of consistency be-tween generated SVBRDF maps. In this paper, we address both issues simultaneously. We present an unsupervised generativeadversarial neural network that addresses both SVBRDF capture from a single image and synthesis at the same time. From alow-resolution input image, we generate a large resolution SVBRDF, much larger than the input images. We train a generativeadversarial network (GAN) to get SVBRDF maps, which have both a large spatial extent and detailed texels. We employ atwo-stream generator that divides the training of maps into two groups (normal and roughness as one, diffuse and specularas the other) to better optimize those four maps. In the end, our method is able to generate high-quality large scale SVBRDFmaps from a single input photograph with repetitive structures and provides higher quality rendering results with more detailscompared to the previous works. Each input for our method requires individual training, which costs about 3 hours.

## Downloads

[Paper (35MB)](page.paper){: .btn .btn--primary}
[Code](page.code){: .btn .btn--primary}

## Cite

```bib
@inproceedings{zhao2020joint,
  title={Joint SVBRDF Recovery and Synthesis From a Single Image using an Unsupervised Generative Adversarial Network.},
  author={Zhao, Yezi and Wang, Beibei and Xu, Yanning and Zeng, Zheng and Wang, Lu and Holzschuch, Nicolas},
  booktitle={EGSR (DL)},
  pages={53--66},
  year={2020}
}
```
## Copyright Disclaimer
© The Author(s). This is the author’s version of the work. It is posted here for your personal use. Not forredistribution. The definitive Version of Record is available at <a href="{{page.doi}}">DOI</a>.
