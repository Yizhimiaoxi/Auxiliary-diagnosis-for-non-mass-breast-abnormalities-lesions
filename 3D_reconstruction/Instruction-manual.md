## Instruction Manual

**_This document is used to demonstrate the 3D reconstruction of the 2D NME Segmentation (Lesion Detection) algorithm prediction mask image._**

_Import the python library that needs to be installed：_
```
pip install SimpleITK nibabel pynrrd
```

_Synthesizing a PNG-format prediction mask into NRRD format requires referencing the NIfTI header information, so a reference NIfTI address needs to be entered._
```
python PNG_to_NRRD_Converter.py --images "/path/to/png/folder" --output_nrrd "/path/to/output/file.nrrd" --reference_NifTI "/path/to/reference/file.nii"
```

_NRRD files are compressed to facilitate reading and saving, as they take up a lot of memory._
```
python NRRD_compression.py --NRRD "/path/to/input.nrrd" --output "/path/to/output.seg.nrrd"
```
