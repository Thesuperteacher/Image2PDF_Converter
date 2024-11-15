import os
import argparse
from PIL import Image

def images_to_pdf(folder_path, output_pdf):
    # Get list of all images in the folder
    image_files = sorted([f for f in os.listdir(folder_path) if f.endswith(('jpg', 'jpeg', 'png'))])

    # Check if there are images to convert
    if not image_files:
        print("No images found in the specified folder.")
        return

    # Open the first image as the base and convert others
    images = [Image.open(os.path.join(folder_path, img)).convert('RGB') for img in image_files]

    # Save all images to a single PDF
    images[0].save(output_pdf, save_all=True, append_images=images[1:])
    print(f"PDF created successfully: {output_pdf}")

if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Convert images in a folder to a PDF.")
    parser.add_argument("folder_path", type=str, help="Path to the folder containing images.")
    parser.add_argument("output_pdf", type=str, nargs="?", default="output.pdf", help="Name of the output PDF file (optional).")

    # Parse arguments
    args = parser.parse_args()

    # Run the function with provided arguments
    images_to_pdf(args.folder_path, args.output_pdf)
