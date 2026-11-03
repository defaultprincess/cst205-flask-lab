import os
import random
import time

from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from PIL import Image

from data import planets

app = Flask(__name__)
bootstrap = Bootstrap5(app)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ORIGINALS_DIR = os.path.join(BASE_DIR, "static", "originals")
NEGATIVE_PATH = os.path.join(BASE_DIR, "static", "negative.png")


def load_images():
    images = []
    for filename in sorted(os.listdir(ORIGINALS_DIR)):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            image = Image.open(os.path.join(ORIGINALS_DIR, filename)).convert("RGB")
            image.thumbnail((800, 800))
            images.append(image)
    return images


def negative(image):
    width, height = image.size
    result = Image.new("RGB", (width, height))
    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            result.putpixel((x, y), (255 - r, 255 - g, 255 - b))
    return result


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/image")
def show_image():
    return render_template("image.html")


@app.route("/bootstrap")
def show_bootstrap_image():
    return render_template("bootstrap_image.html")


@app.route("/dictionary")
def show_dictionary():
    return render_template("dictionary.html", planets=planets)


@app.route("/random")
def random_negative():
    images = load_images()
    chosen = random.choice(images)
    negative(chosen).save(NEGATIVE_PATH)
    return render_template("random.html", version=time.time())


if __name__ == "__main__":
    app.run(debug=True)
