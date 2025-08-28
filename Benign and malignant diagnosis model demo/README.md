# _Statement_

Because this product has been commercially available, this document provides a demo of the algorithm (which differs slightly from the actual model in terms of parameters, training sample size, and network, but achieves the same effect).

# _Method to run demo_

## _Introduction_

This project implements a 3D Transformer network based on PyTorch to predict the benign or malignant nature of tumors using multimodal medical images (such as DWI, ADC, etc.) and corresponding lesion masks (NRRD) input.

## _Environment setting_
Please install the following dependencies first
```
pip install torch torchvision torchaudio
pip install nibabel pynrrd scipy tqdm numpy
```
## _Example project structure_

```
Demo-project/
│
├── model/
│   └── model.pth                 # Trained model weights
│
├── Sample/
│   └── Sample_data/
│       ├── Benign/               # Benign samples
│       │   ├── case_001/
│       │   │   ├── 1.nii
│       │   │   ├── 7.nii
│       │   │   ├── ADC.nii
│       │   │   └── reference_mask.nrrd
│       │   └── case_002/ ...
│       └── Malignant/            # Malignant samples
│           └── case_101/ ...
│
└── dataset/                      
```
Each case folder should contain three imaging modalities (1.nii, 7.nii, ADC.nii) and an NRRD mask file.

The runtime automatically preprocesses the data into a (4, 64, 64, 28) tensor and caches it as a .npz file.

## _Model Description_

**Model Architecture:** TumorTransformer3D

**Input:** 4-channel 3D image (3 modalities + mask).

**Feature Extraction:** Convolutional layer + Spatial Attention module.

**Sequence Modeling:** Transformer encoder-decoder architecture.

**Output:** Binary classification (benign/malignant).

**Spatial Attention Module:** Learns important regions in spatial dimensions to improve lesion discrimination.

**Data Preprocessing:** Automatically resamples to (64, 64, 28). Normalizes to [0, 1].

**Prediction Process:** Traverses the cases in the specified folder. Preprocesses/loads each case.Inputs the model and outputs the category and confidence score.

## _How to use_

Specify the model path and data path in the code:
```
model_path = "../model/model.pth"
data_dir = "../Sample/Sample_data/Benign"
main(model_path, data_dir)
```
After running, the output will be similar to:

```
Loading preprocessed data from /Demo_project/Sample/Sample_data/case001.npz
Prediction for case case001: Benign with confidence 0.9926
Loading preprocessed data from /Demo_project/Sample/Sample_data/case002.npz
Prediction for case case002: Benign with confidence 0.9984
```

## _Notes_

**Preprocessing Cache**

If you change target_size, you must manually clear the dataset/ directory; otherwise, old .npz files will be loaded.

**GPU Issues**

Due to the large number of Transformer parameters, it is recommended to run on a GPU (Colab Pro or a local CUDA environment).

**Class Label**

0 → Benign

1 → Malignant
