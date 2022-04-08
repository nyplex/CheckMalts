from pathlib import Path
from PIL import Image


def convert_to_webp(source):

    destination = source.with_suffix(".webp")

    image = Image.open(source)  # Open image
    MAX_SIZE = (2200, 2200)
    image.thumbnail(MAX_SIZE)
    
    image.save(destination, format="webp", quality=85)  # Convert image to webp

    return destination


def main():
    paths = Path("home/static/home/images/jagerFrame").glob("**/*.jpg")
    for path in paths:
        webp_path = convert_to_webp(path)
        print(webp_path)


main()