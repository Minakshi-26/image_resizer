# Image Resizer Tool

This is a Python-based **Image Resizer Tool** that allows you to **resize and convert images in batch**. 
It is built using **Python and Pillow (PIL)**, making image processing easy and automated.

## Features
- Resize multiple images at once
- Maintain aspect ratio to prevent distortion
- Optional format conversion (JPG, PNG, JPEG)
- User-defined width and height
- Error handling for non-image or corrupted files
- Saves processed images in a separate `resized/` folder
- Shows progress for each image

## Technologies Used
- Python 3.x
- Pillow (Python Imaging Library)

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/username/image_resizer.git
````

2. Navigate to the project folder:

   ```bash
   cd image_resizer
   ```
3. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   venv\Scripts\activate  
   source venv/bin/activate  
4. Install required libraries:

   pip install Pillow

5. Place images you want to resize in the `images/` folder.

## Run Instructions

python image_resizer.py


* Follow prompts to enter desired width, height, and optional format.
* Resized images will be saved in the `resized/` folder.


 


