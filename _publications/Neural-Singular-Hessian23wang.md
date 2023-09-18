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


[//]: # ([Arxiv &#40;23MB&#41;]&#40;{{page.arxiv}}&#41;{: .btn .btn--primary})
[//]: # ([Code &#40;22MB&#41;]&#40;{{page.code}}&#41;{: .btn .btn--primary})

## Abstract

[//]: # (Neural implicit representation is a promising approach for reconstructing surfaces from point clouds. Existing methods combine various regularization terms, such as the Eikonal and Laplacian energy terms, to enforce the learned neural function to possess the properties of a Signed Distance Function (SDF). However, inferring the actual topology and geometry of the underlying surface from poor-quality unoriented point clouds remains challenging. In accordance with Differential Geometry, the Hessian of the SDF is singular for points within the differential thin-shell space surrounding the surface. Our approach enforces the Hessian of the neural implicit function to have a zero determinant for points near the surface. This technique aligns the gradients for a near-surface point and its on-surface projection point, producing a rough but faithful shape within just a few iterations. By annealing the weight of the singular-Hessian term, our approach ultimately produces a high-fidelity reconstruction result. Extensive experimental results demonstrate that our approach effectively suppresses ghost geometry and recovers details from unoriented point clouds with better expressiveness than existing fitting-based methods.)

<div style="text-align: center;">
<h2>Video</h2>
</div>

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
