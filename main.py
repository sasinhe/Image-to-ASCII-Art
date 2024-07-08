from PIL import Image, ImageOps
from math import floor









def main():
    # The idea here is to crop the original image into a square of 100x100 pixels, which is the number of characters we are using to display the ASCII art. S
    with Image.open('cat.jpg') as img:
        img.thumbnail([100, 100])
        px = img.load()




if __name__ == '__main__':
    main()