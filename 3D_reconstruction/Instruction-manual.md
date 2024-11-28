# **This document is used to demonstrate the 3D reconstruction of the 2D NME Segmentation (Lesion Detection) algorithm prediction mask image.**

pip install SimpleITK nibabel pynrrd

python PNG_to_NRRD_Converter.py --images "/path/to/png/folder" --output_nrrd "/path/to/output/file.nrrd" --reference_NifTI "/path/to/reference/file.nii"
