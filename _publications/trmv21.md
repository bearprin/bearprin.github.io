---
uid: 2
layout: publication
title: Temporally Reliable Motion Vectors for Real-time Ray Tracing
authors: <b>Zheng Zeng</b>, <a href="http://behindthepixels.io/" target="_blank">Shiqiu (Edward) Liu</a>, Jinglei Yang, <a href="http://vr.sdu.edu.cn/info/1010/1060.htm" target="_blank">Lu Wang</a>, <a href="https://sites.cs.ucsb.edu/~lingqi/" target="_blank">Ling-Qi Yan</a>

publication: Computer Graphics Forum (Proceedings of Eurographics 2021)
doi: https://doi.org/10.1111/cgf.142616
paper: https://sites.cs.ucsb.edu/~lingqi/publications/paper_trmv.pdf
code:
slides: /assets/files/TRMV_EG_2021.pptx
presentation_slides_video: https://drive.google.com/file/d/1KYr1M6VvAITp_PmoRZRk0wgqUIKcTeP5/view?usp=sharing
supplementary:
supplemental_video: https://sites.cs.ucsb.edu/~lingqi/publications/video_trmv.mp4
---

## Abstract

Real-time ray tracing (RTRT) is being pervasively applied. The key to RTRT is a reliable denoising scheme that reconstructs clean images from significantly undersampled noisy inputs, usually at 1 sample per pixel as limited by current hardware’s computing power. The state of the art reconstruction methods all rely on temporal filtering to find correspondences of current pixels in the previous frame, described using per-pixel screen-space motion vectors. While these approaches are demonstrated powerful, they suffer from a common issue that the temporal information cannot be used when the motion vectors are not valid, i.e. when temporal correspondences are not obviously available or do not exist in theory.
We introduce temporally reliable motion vectors that aim at deeper exploration of temporal coherence, especially for the generally-believed difficult applications on shadows, glossy reflections and occlusions, with the key idea to detect and track the cause of each effect. We show that our temporally reliable motion vectors produce significantly better temporal results on a variety of dynamic scenes when compared to the state of the art methods, but with negligible performance overhead.

## Downloads

[Paper (37MB)]({{page.paper}}){: .btn .btn--primary}
[Slides (PPT, 24MB)]({{page.slides}}){: .btn .btn--primary}
[Presentation slides video (45MB)]({{page.presentation_slides_video}}){: .btn .btn--primary}
[Supplemental video (629MB)]({{page.supplemental_video}}){: .btn .btn--primary}



## Videos
**Presentation slides video**
{% include video provider="google-drive" id="1KYr1M6VvAITp_PmoRZRk0wgqUIKcTeP5" %}

**Supplemental video**

{% include video provider="google-drive" id="1UkiWnzqS-3kgfQM8rFczyy1JW638jT87" %}

## Cite

```bib
@inproceedings{zeng2021temporally,
  title={Temporally Reliable Motion Vectors for Real-time Ray Tracing},
  author={Zeng, Zheng and Liu, Shiqiu and Yang, Jinglei and Wang, Lu and Yan, Ling-Qi},
  booktitle={Computer Graphics Forum},
  volume={40},
  number={2},
  pages={79--90},
  year={2021},
  organization={Wiley Online Library}
}
```
## Copyright Disclaimer
© The Author(s). This is the author’s version of the work. It is posted here for your personal use. Not forredistribution. The definitive Version of Record is available at <a href="{{page.doi}}">DOI</a>.
