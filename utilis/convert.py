from PIL import Image
import PIL
import os
import glob


from pathlib import Path
from PIL import Image


def convert_to_webp(source):

    destination = source.with_suffix(".webp")

    image = Image.open(source)  # Open image
    image.save(destination, format="webp")  # Convert image to webp

    return destination


def main():
    paths = Path("static/media/home_page").glob("**/*.png")
    for path in paths:
        webp_path = convert_to_webp(path)
        print(webp_path)


main()