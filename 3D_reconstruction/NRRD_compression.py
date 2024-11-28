import nrrd
import argparse

# Compress an NRRD file to .seg.nrrd format with gzip encoding
def compress_nrrd_to_seg(input_nrrd_file, output_seg_nrrd_file):

    # Read the NRRD file's data and header
    data, header = nrrd.read(input_nrrd_file)

    # Update the header to use gzip encoding
    header['encoding'] = 'gzip'

    # Save the data with the updated header to the output file
    nrrd.write(output_seg_nrrd_file, data, header)

    print(f"{input_nrrd_file} has been successfully compressed and saved as {output_seg_nrrd_file}")

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Compress an NRRD file to .seg.nrrd format.")
    parser.add_argument("--NRRD", required=True, help="Path to the input NRRD file.")
    parser.add_argument("--output", required=True, help="Path to save the compressed .seg.nrrd file.")
    args = parser.parse_args()

    # Call the compression function
    compress_nrrd_to_seg(args.NRRD, args.output)
