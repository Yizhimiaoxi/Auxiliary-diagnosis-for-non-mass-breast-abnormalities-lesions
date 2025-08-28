# _Improved Diagnostic Performance of non-mass enhancement lesions through 3D CNN-Transformer Integrated Network: A Multi-center Study with Multimodal MRI_

## _Abstract_
_**Background:** Due to variations in the interpretation of MRI images by different radiologists, the diagnostic accuracy and consistency of non-mass-enhancement (NME) lesions remains poor, with problems such as false-positive results, over-reliance on physician experience, and poor sensitivity for small or occult lesions. It is therefore essential to improve the differential diagnosis of NME lesions._

_**Purpose:** Aims to find a deep learning modal to help doctors segment and classify the breast NME lesions on MRI automatically with higher diagnostic accuracy._

_**Materials and Methods:** The retrospective study utilizing multimodal MRI data from 569 female patients (January 2021-March 2024) encompassing 633 NME lesions was conducted. The Fusion-Aware Network (FANet) was developed and validated to enhance the differential diagnosis of benign and malignant NME lesions by integrating multimodal MRI data (early enhancement, late enhancement, and ADC map) from multiple institutions. FANet adopts a two-stage framework, employing YOLOv8 for lesion localization followed by U-Net3+ for segmentation, effectively mitigating sample imbalance. Additionally, a 3D CNN-Transformer architecture with self-attention mechanisms is incorporated to enhance spatial feature representation._

_**Results:** Experimental results demonstrate that FANet outperforms existing models, achieving an AUC of 0.97 (95% CI: [0.96, 0.98]), with superior sensitivity (94%) and specificity (96%). Compared to conventional deep learning models that rely solely on 2D feature extraction or single-modality data, FANet integrates multimodal MRI data, alongside lesion segmentation masks, to incorporate shape, texture, and size information into the classification process. Meanwhile, the integration of the YOLOv8 lesion detection algorithm with Unet 3+ has shown higher accuracy (DSC=0.92; p<.05) in lesion segmentation than algorithms of the same type, which can reduce the need for postoperative biopsies._

_**Conclusion:** An accurate auxiliary diagnosis algorithm for NME lesions in the breast was established by integrating multimodal data and automatically segmenting the features of NME lesions in dynamic contrast-enhanced magnetic resonance imaging (DCE-MRI)._

## _Summary statement_
_FANet integrates CNN-Transformer and spatial self-attention, and adopts a two-stage network structure to improve the accuracy of MRI classification of benign and malignant NME lesions and reduce unnecessary biopsies._

_**Key Results:**_

_·The researchers created a Transformer-based Fusion Aware Net (FANet) by integrating multimodal feature inputs with a spatial self-attention module._

_·The model was trained using multimodal data inputs (EEI, LEI, ADC, mask) and attained an  area under the subject-work characteristic curve (AUC) of 0.97, with a sensitivity of 94% (88/94) and a specificity of 96% (74/ 77)._

_·In terms of NME lesion segmentation, a two-stage approach was used with significant results (DSC=0.9879, IoU=0.9760, Precision=0.9842)._

