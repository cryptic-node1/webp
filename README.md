# WebP Converter
[![Ask DeepWiki](https://devin.ai/assets/askdeepwiki.png)](https://deepwiki.com/cryptic-node1/webp)

A simple and interactive command-line tool for converting JPG and PNG images to the WebP format. The script supports converting a single file or batch-processing an entire folder of images.

## Features

*   **Two Conversion Modes**: Choose between converting a single image or batch-converting all supported images in a directory.
*   **Wide Support**: Converts `.jpg`, `.jpeg`, and `.png` files.
*   **Transparency Preservation**: Retains the alpha channel for PNG images during conversion.
*   **Adjustable Quality**: Set a custom quality level (0-100) for your conversions to balance file size and visual fidelity.
*   **User-Friendly CLI**: An interactive prompt guides you through the conversion process.

## Prerequisites

*   Python 3
*   Pillow, the Python Imaging Library fork

## Installation

1.  Clone the repository:
    ```sh
    git clone https://github.com/cryptic-node1/webp.git
    cd webp
    ```

2.  Install the required `Pillow` library:
    ```sh
    pip install Pillow
    ```

## Usage

Run the script from your terminal:

```sh
python tool.py
```

You will be presented with a menu to choose your conversion mode:

```
  WebP Converter

  [1] Single file
  [2] Batch folder

Select:
```

### Single File Conversion

1.  Choose option `1`.
2.  Enter the full path to the image file you want to convert.
3.  Enter a quality setting between 0 and 100 (or press Enter to use the default of 80).
4.  The converted file will be saved in the `webp_output` directory.

**Example:**
```
Select: 1
─
SINGLE FILE CONVERT
─
File path: /path/to/my/images/photo.jpg
Quality (0–100) [default: 80]: 90

Converting  →  photo.jpg  (quality=90)
  ✓ Saved: /path/to/repo/webp/webp_output/photo.webp
```

### Batch Folder Conversion

1.  Choose option `2`.
2.  Enter the path to the folder containing the images you want to convert.
3.  The script will list all supported images found in that folder.
4.  Enter a quality setting for the batch job.
5.  A new folder named `<original_folder_name>_webp` will be created alongside the original folder, and all converted images will be saved there.

**Example:**
```
Select: 2
─
BATCH CONVERT
─
Folder path: /path/to/my/images
Found 3 file(s):
    photo1.jpg
    photo2.png
    graphic.jpeg
Quality (0–100) [default: 80]:

Output folder: /path/to/my/images_webp
Quality: 80

  ✓ photo1.jpg  →  photo1.webp
  ✓ photo2.png  →  photo2.webp
  ✓ graphic.jpeg  →  graphic.webp
─
Done. 3 converted, 0 failed.
Output: /path/to/my/images_webp
```

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.
