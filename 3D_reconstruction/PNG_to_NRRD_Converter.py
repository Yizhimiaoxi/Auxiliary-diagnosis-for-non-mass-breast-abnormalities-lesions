import os
import numpy as np
import SimpleITK as sitk
from PIL import Image
import nibabel as nib
import re
import argparse

def rotate_and_flip_image(image_array):
    """ Rotate image 90 degrees counterclockwise and flip horizontally. """
    return np.fliplr(np.rot90(image_array, k=3))  # Rotate 270 degrees and flip horizontally

def extract_number_from_filename(filename):
    """ Extract number from filename using regex. """
    match = re.search(r'(\d+)', filename)
    return int(match.group(1)) if match else -1

def png_folder_to_nrrd(png_folder, output_nrrd_path, nii_file_path):
    """ Convert PNG slices to NRRD file using NIfTI header information. """
    # Read NIfTI file to get header information
    nii_img = nib.load(nii_file_path)
    nii_header = nii_img.header
    nii_affine = nii_img.affine

    # Ensure voxel size is a list of 3 float values
    voxel_size = list(map(float, nii_header.get_zooms()))

    # Check if we have exactly 3 values in voxel_size (for 3D images)
    if len(voxel_size) != 3:
        raise ValueError(f"Expected 3 spacing values, but got {len(voxel_size)}")

    dimensions = nii_header.get_data_shape()

    # Get PNG files and sort them
    png_files = sorted([f for f in os.listdir(png_folder) if f.endswith('.png')], key=extract_number_from_filename)

    # Check if number of PNG files matches the expected number of slices
    if len(png_files) != dimensions[2]:
        raise ValueError(f"Number of PNG files ({len(png_files)}) does not match the number of slices in the NIfTI file ({dimensions[2]})")

    # Read and process each PNG file
    slices = []
    for png_file in png_files:
        img_path = os.path.join(png_folder, png_file)
        img_array = np.array(Image.open(img_path).convert('L'))

        # Rotate and flip image
        img_array = rotate_and_flip_image(img_array)

        # Convert image array to binary (0 or 1) if it is binary data
        img_array = (img_array > 128).astype(np.uint8)  # Assuming binary mask with threshold 128

        slices.append(img_array)

    # Convert list of slices to a 3D NumPy array and transpose to correct orientation
    volume = np.stack(slices, axis=-1)
    volume = np.transpose(volume, (2, 1, 0))  # (number_of_slices, height, width) to (depth, height, width)

    # Convert NumPy array to SimpleITK image
    itk_image = sitk.GetImageFromArray(volume)

    # Set spacing using voxel_size (which is a list of floats now)
    itk_image.SetSpacing(voxel_size)

    # Set origin from affine (translation part)
    itk_image.SetOrigin(nii_affine[:3, 3].tolist())

    # Set direction (no flip, use the rotation part directly)
    itk_image.SetDirection(nii_affine[:3, :3].flatten().tolist())

    # Write the image to NRRD format with no compression
    sitk.WriteImage(itk_image, output_nrrd_path, useCompression=False)

    print(f"Converted PNG slices to NRRD format and saved to {output_nrrd_path}")

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Convert PNG slices to NRRD format.")
    parser.add_argument("--images", required=True, help="Path to folder containing PNG slices.")
    parser.add_argument("--output_nrrd", required=True, help="Output path for the NRRD file.")
    parser.add_argument("--reference_NifTI", required=True, help="Path to reference NIfTI file.")
    args = parser.parse_args()

    # Call the function
    png_folder_to_nrrd(args.images, args.output_nrrd, args.reference_NifTI)
