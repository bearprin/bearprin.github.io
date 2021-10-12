---
uid: 0
layout: publication
title: Denoising Stochastic Progressive Photon Mapping Renderings Using a Multi-Residual Network
authors: <b>Zheng Zeng</b>, <a href="http://vr.sdu.edu.cn/info/1010/1060.htm" target="_blank">Lu Wang</a>, <a href="https://wangningbei.github.io/" target="_blank">Beibei Wang</a>, Chun-Meng Kang, <a href="http://vr.sdu.edu.cn/info/1010/1062.htm" target="_blank"> Yanning Xu</a>

publication: Journal of Computer Science and Technology (CVM2020)
doi: https://doi.org/10.1007/s11390-020-0264-1
paper: /assets/files/jcst2020-sppm-denoiser.pdf
code:
slides: /assets/files/jcst2020-sppm-denoiser-pre.pdf
presentation_slides_video: https://drive.google.com/file/d/1JxJqaM7F3ZnxtAe_Vlsp3cgRRY6fM_kC/view?usp=sharing
supplementary:
supplemental_video:
---

## Abstract

Stochastic progressive photon mapping (SPPM) is one of the important global illumination methods in computer graphics. It can simulate caustics and specular-diffuse-specular lighting effects efficiently. However, as a biased method, it always suffers from both bias and variance with limited iterations, and the bias and the variance bring multi-scale noises into SPPM renderings. Recent learning-based methods have shown great advantages on denoising unbiased Monte Carlo (MC) methods, but have not been leveraged for biased ones. In this paper, we present the first learning-based method specially designed for denoising-biased SPPM renderings. Firstly, to avoid conflicting denoising constraints, the radiance of final images is decomposed into two components: caustic and global. These two components are then denoised separately via a two-network framework. In each network, we employ a novel multi-residual block with two sizes of filters, which significantly improves the model’s capabilities, and makes it more suitable for multi-scale noises on both low-frequency and high-frequency areas. We also present a series of photon-related auxiliary features, to better handle noises while preserving illumination details, especially caustics. Compared with other state-of-the-art learning-based denoising methods that we apply to this problem, our method shows a higher denoising quality, which could efficiently denoise multi-scale noises while keeping sharp illuminations.

## Downloads

[Paper (5MB)](page.paper){: .btn .btn--primary}
[Slides (6MB)]({{page.slides}}){: .btn .btn--primary}
[Presentation slides video (400MB)]({{page.presentation_slides_video}}){: .btn .btn--primary}


## Videos
**Presentation slides video**
{% include video provider="google-drive" id="1JxJqaM7F3ZnxtAe_Vlsp3cgRRY6fM_kC" %}

## Cite

```bib
@article{zeng2020denoising,
  title={Denoising stochastic progressive photon mapping renderings using a multi-residual network},
  author={Zeng, Zheng and Wang, Lu and Wang, Bei-Bei and Kang, Chun-Meng and Xu, Yan-Ning},
  journal={Journal of Computer Science and Technology},
  volume={35},
  pages={506--521},
  year={2020},
  publisher={Springer}
}
```
## Copyright Disclaimer
© The Author(s). This is the author’s version of the work. It is posted here for your personal use. Not forredistribution. The definitive Version of Record is available at <a href="{{page.doi}}">DOI</a>.
