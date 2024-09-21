import os
from flask import Flask, render_template, redirect, url_for, send_from_directory
from flask_wtf import FlaskForm
from werkzeug.utils import secure_filename
from wtforms import FileField, SubmitField, StringField, PasswordField
from PIL import Image, ImageDraw, ImageFont
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'U are a Piece of sheet'
app.config["IMAGE_UPLOADS"] = "static/image"
app.config["WATERMARKED_IMAGES"] = "static/watermarked"

# Ensure directories exist
os.makedirs(app.config["IMAGE_UPLOADS"], exist_ok=True)
os.makedirs(app.config["WATERMARKED_IMAGES"], exist_ok=True)


class UploadFile(FlaskForm):
    file = FileField('File')
    submit = SubmitField('Upload')


@app.route('/', methods=['POST', 'GET'])
def home():
    form = UploadFile()
    if form.validate_on_submit():
        # Handle file upload
        image_file = form.file.data
        filename = secure_filename(image_file.filename)
        filepath = os.path.join(app.config["IMAGE_UPLOADS"], filename)
        image_file.save(filepath)

        # Add watermark
        watermarked_filepath = add_watermark(filepath, filename)

        # Redirect to the watermarked image
        return redirect(url_for('display_image', filename=os.path.basename(watermarked_filepath)))

    return render_template('index.html', form=form)


def add_watermark(image_path, original_filename):
    img = Image.open(image_path)
    img_width, img_height = img.size
    draw_img = ImageDraw.Draw(img, )
    text_img = 'haha'
    font_img = ImageFont.truetype("/Users/user/Desktop/python_file/Water Mark/k22_plural_6918816/K22 Plural.ttf", 50, )

    # Calculate text size using textbbox()
    text_bbox = draw_img.textbbox((0, 0), text_img, font=font_img)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    font_margin = 10
    x = img_width - text_width - font_margin
    y = img_height - text_height - font_margin
    font_color = (255, 0, 0, 128)

    draw_img.text((x, y), text=text_img, font=font_img, fill=font_color)

    # Save the watermarked image with a unique name based on the original filename
    watermarked_image_path = os.path.join(app.config["WATERMARKED_IMAGES"], f"watermarked_{original_filename}")
    img.save(watermarked_image_path)

    # Return the path to the saved watermarked image
    return watermarked_image_path


@app.route('/image/<filename>')
def display_image(filename):
    return render_template('download_page.html', watermarked_filepath=filename)


# Route to display the watermarked image
@app.route('/serve_watermarked_image/<filename>')
def serve_watermarked_image(filename):
    return send_from_directory(app.config["WATERMARKED_IMAGES"], filename)


if __name__ == '__main__':
    app.run(debug=True, port=5001)