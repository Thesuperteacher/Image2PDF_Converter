# **Image2PDF Converter**

Image2PDF Converter is a simple Python tool that converts a batch of images in a specified folder into a single PDF file. It’s ideal for users needing a quick way to compile images into a PDF document for presentations, portfolios, or archival purposes.

## **Features**

- Converts all images in a specified folder to a single PDF file.
- Supports JPG, JPEG, and PNG image formats.
- Customizable output PDF file name.
- Command-line usage for quick and easy operation.

---

## **Requirements**

- **Python 3.6+**
- **Pillow Library** (Python Imaging Library)

To install the Pillow library, run:
```bash
pip install pillow
```

---

## **Installation**

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Image2PDF_Converter.git
   cd Image2PDF_Converter
   ```

2. Install the required dependencies:
   ```bash
   pip install pillow
   ```

---

## **Usage**

You can run the script from the command line, specifying the folder containing the images and an optional output PDF file name.

```bash
python main.py "path/to/image_folder" output_file.pdf
```

### **Arguments**

- `folder_path` (required): The path to the folder containing images.
- `output_pdf` (optional): The name of the output PDF file. Defaults to `output.pdf` if not provided.

### **Example**

Convert all images in the folder `~/Pictures` to a PDF named `album.pdf`:

```bash
python main.py "C:/Users/eldri/Pictures" album.pdf
```

---

## **Troubleshooting**

- **No Images Found**: Ensure the folder path is correct and contains images with `.jpg`, `.jpeg`, or `.png` extensions.
- **Permission Issues**: If there are file access issues, try running the script with elevated permissions (administrator mode on Windows).
- **File Path Issues**: If there are spaces in the file path, make sure to wrap the path in quotes.

---

## **Contributing**

Feel free to open issues or submit pull requests to improve this tool. Contributions are welcome!

---

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **Contact**

For any questions or feedback, please contact me through GitHub.

---

This `README.md` provides a comprehensive overview of your project, including usage instructions, requirements, and troubleshooting tips. You can adjust the GitHub repository URL and contact section as needed.
