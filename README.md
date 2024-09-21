Watermark Image Flask Application
This is a Flask web application that allows users to upload an image and receive a version of the image with a watermark. The application saves the watermarked image and provides a link for users to download it.

Features
Upload image files (in formats like .png, .jpg, etc.).
Apply a custom watermark to the image.
Download and view the watermarked image.
Technologies Used
Python: Backend logic.
Flask: Web framework used to manage routes, form handling, and rendering templates.
WTForms: Flask extension for form handling.
Pillow (PIL): Python library used to manipulate and edit images (adding watermarks).
HTML/CSS: Used for front-end user interface (via Flask templates).
Werkzeug: For secure filename handling.
Project Structure
php
Copy code
.
├── app.py                    # Main application file
├── static/                   # Directory for static files (e.g., uploaded images)
│   ├── image/                # Folder to store uploaded images
│   └── watermarked/          # Folder to store watermarked images
├── templates/                # HTML templates for rendering views
│   ├── index.html            # Main upload page
│   └── download_page.html    # Page for displaying the watermarked image
└── README.md                 # Project documentation
How It Works
Users visit the homepage where they can upload an image.
The uploaded image is saved in the static/image/ directory.
The application applies a predefined watermark text to the uploaded image using Pillow (PIL).
The watermarked image is saved in the static/watermarked/ directory with the same file name prefixed with watermarked_.
Users are redirected to a page where they can view and download the watermarked image.
Installation
Prerequisites
Python 3.x
Flask
Pillow (PIL)
Steps to Install
Clone the repository:
bash
Copy code
git clone https://github.com/your-username/watermark-app.git
cd watermark-app
Install required dependencies:
bash
Copy code
pip install flask pillow flask-wtf
Run the Flask app:
bash
Copy code
python app.py
Open your web browser and go to:
arduino
Copy code
http://127.0.0.1:5001/
Configuration
Image Uploads: Uploaded images are stored in the static/image directory.
Watermarked Images: Watermarked images are saved in the static/watermarked directory.
Usage
Upload an image via the form on the homepage.
Once the image is uploaded, the watermark will be applied automatically.
You'll be redirected to a new page with a link to view and download the watermarked image.
Customizing the Watermark
You can customize the watermark text and font in the add_watermark function inside app.py.
The font used for the watermark (.ttf file) should be stored in a valid path that you define.
python
Copy code
text_img = 'Custom Watermark Text'
font_img = ImageFont.truetype("path_to_font_file.ttf", 50)
