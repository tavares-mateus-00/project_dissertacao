### DISSERTAÇÃO

Hello, how are you? I hope you're doing well!

In this project, you will find my Master's in Computer Science.

**Author**: $\text{NoBoRy}$;
**Supervisor**: $\text{Franklin César Flores}$;
**Co-supervisor**: $\text{Yandre Maldonado e Gomes da Costa}$

**Title**: PROCESSING OF RAT LIVER PHOTOMICROGRAPHS THROUGH MATHEMATICAL MORPHOLOGY AND MACHINE LEARNING.

**University**: State University of Maringá - UEM

### $\text{Abstract}$

In this work, preliminary results for the automatic detection of cancer (Walker 256 tumor) and two segmenters enabling morphometry (extraction of geometric measures such as area and perimeter of cell nuclei) in preclinical rat liver tissue microphotograph images are described. In the proposed approach for the classifier, two different types of descriptors were explored to capture texture properties of the images. The first texture descriptor experimented is the Local Phase Quantization (LPQ). The second is the Granulometry technique, which is built by a family of morphological filters. For classification, the Support Vector Machine (SVM), k-Nearest Neighbor (k-NN), and Logistic Regression algorithms were used. In the proposed approach for segmentation, techniques using Digital Image Processing, Mathematical Morphology, and YOLO were explored. The first segmenter is built using Mathematical Morphology and Digital Image Processing to segment the nuclei, while YOLO is used to find the nuclei in the image. The second segmenter is built using the Alternating Sequence Filter (ASF) morphological filters to segment and find the nuclei. 

### $\text{Results}$

Experiments conducted on datasets developed by the Enteric Neural Plasticity Laboratory (LPNE) of the State University of Maringá (UEM) showed that both texture descriptors provide good results. In the classification process, accuracy rates obtained using the SVM classifier were **96.67%** for the Granulometry-based texture operator and **91.16%** for the LPQ operator. However, the best result is obtained by combining classifiers created with both descriptors in a Late Fusion strategy, achieving an accuracy of **99.16%**. The classification process was tested on the data_set_ dataset. In the segmentation process, the best result was obtained with the second segmenter achieving an IoU of **88.23%**. However, there are biases in the nucleus counting. The first segmenter obtained an IoU of **86.36%** and an exact nucleus count. The segmentation process was tested on the data_set dataset, but the segmenter works on both available datasets.

### $\text{LP}$

All codes were developed using the programming language Python. The Machine Learning (ML) and Digital Image Processing (DIP) algorithms were all taken from the websites [Sklearn](https://scikit-learn.org/stable/) and [Skimage](https://scikit-image.org/).

### $\text{DATA SET}$

The datasets used in this work were created by researchers from the LPNE at UEM. To do this, adult male Wistar rats were used. All procedures involving animals were previously approved by the *Permanent Commission on Ethics in Animal Experimentation* at UEM.

* The dataset (`data_set`) consists of **120** microphotographs with dimensions of 1024 by 768 pixels captured from rat liver tissue samples. The images are divided into two classes: *Control* (C) and *Walker 256 Tumor* (TW). Each class consists of 60 microphotographs from six rats, 10 from each rat.

* The dataset (`data_set_`) consists of **240** microphotographs with dimensions of 1024 by 768 pixels captured from rat liver tissue samples. The images are divided into four classes: *Control* (C), *Treated Control* (CTG), *Walker 256 Tumor* (TW), and *Treated Walker 256 Tumor* (TWGT). Each class consists of 60 microphotographs from six rats, 10 from each rat.

### $\text{RESULTING IMAGE}$

![Resultado do método 1](https://github.com/mafta-00/project_dissertacao/blob/main/image_results/ct-seg-primeira.png)

$\text{Enjoy!!!}$ 😁

