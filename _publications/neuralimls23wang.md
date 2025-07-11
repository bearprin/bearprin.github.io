---
uid: 3
layout: publication
collection: publications
title: "Neural-IMLS: Self-supervised Implicit Moving Least-Squares Network for Surface Reconstruction"
authors: <b>Zixiong Wang</b>, Pengfei Wang, <a href="https://wang-ps.github.io/" target="_blank">Pengshuai Wang</a>, <a href="https://qiujiedong.github.io/" target="_blank">Qiujie Dong</a>, Junjie Gao, Shuangmin Chen, <a href="http://irc.cs.sdu.edu.cn/~shiqing/index.html" target="_blank">Shiqing Xin</a>, <a href="http://irc.cs.sdu.edu.cn/~chtu/index.html" target="_blank">Changhe Tu</a>, <a href="https://engineering.tamu.edu/cse/profiles/Wang-Wenping.html" target="_blank">Wenping Wang</a>

publication: IEEE Transactions on Visualization and Computer Graphics (TVCG), 2023
pages: true
doi: 
arxiv: https://arxiv.org/abs/2109.04398
paper: https://ieeexplore.ieee.org/document/10146518
code: https://github.com/bearprin/Neural-IMLS
slides:
presentation_slides_video:
supplementary:
supplemental_video:
---

## Abstract

Surface reconstruction is a challenging task when input point clouds, especially real scans, are noisy and lack normals. Observing that the Multilayer Perceptron (MLP) and the implicit moving least-square function (IMLS) provide a dual representation of the underlying surface, we introduce Neural-IMLS , a novel approach that directly learns a noise-resistant signed distance function (SDF) from unoriented raw point clouds in a self-supervised manner. In particular, IMLS regularizes MLP by providing estimated SDFs near the surface and helps enhance its ability to represent geometric details and sharp features, while MLP regularizes IMLS by providing estimated normals. We prove that at convergence, our neural network produces a faithful SDF whose zero-level set approximates the underlying surface due to the mutual learning mechanism between the MLP and the IMLS. Extensive experiments on various benchmarks, including synthetic and real scans, show that Neural-IMLS can reconstruct faithful shapes even with noise and missing parts. The source code can be found at [URL](https://github.com/bearprin/Neural-IMLS).


## Cite

```bib
@ARTICLE{neuralimls2023wang,
  author={Wang, Zixiong and Wang, Pengfei and Wang, Pengshuai and Dong, Qiujie and Gao, Junjie and Chen, Shuangmin and Xin, Shiqing and Tu, Changhe and Wang, Wenping},
  journal={IEEE Transactions on Visualization and Computer Graphics}, 
  title={Neural-IMLS: Self-supervised Implicit Moving Least-Squares Network for Surface Reconstruction}, 
  year={2023},
  volume={},
  number={},
  pages={1-16},
  doi={10.1109/TVCG.2023.3284233}
 }
```

[//]: # (## Copyright Disclaimer)

[//]: # (© The Author&#40;s&#41;. This is the author’s version of the work. It is posted here for your personal use. Not forredistribution. The definitive Version of Record is available at <a href="{{page.doi}}">DOI</a>.)
