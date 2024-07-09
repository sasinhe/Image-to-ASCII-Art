from PIL import Image
import numpy as np
import argparse
import os

CHARACTERS = ".:-=+*≡#@" 

def getCharacter(brightness_value: float, brightness_interval: list[float, float]) -> str:
    step = (brightness_interval[1] - brightness_interval[0]) / len(CHARACTERS)
    index = int((brightness_value - brightness_interval[0]) / step)
    return CHARACTERS[min(index, len(CHARACTERS) - 1)]

def main():
    parser = argparse.ArgumentParser(prog='Text to ASCII CLI', description='Convert images to ASCII art')
    parser.add_argument('image', type=str, help='The image to be converted to ASCII art')
    parser.add_argument('--output', type=str, help='The output file to save the ASCII art')
    parser.add_argument('--size', type=int, nargs=2, default=[100, 100], help='Size of the ASCII art in characters (width height)')
    parser.add_argument('--text', type=str, help='The text to be converted to ASCII art')

    args = parser.parse_args()

    if not os.path.exists(args.image):
        print(f"Error: The file {args.image} does not exist.")
        return

    with Image.open(args.image) as img:
        img = img.convert('L')  # Convert to grayscale
        img.thumbnail(args.size)
        px = np.array(img)

        brightArray = np.interp(px, (px.min(), px.max()), (0, len(CHARACTERS)-1)).astype(int)
        ascii_art = "\n".join("".join(CHARACTERS[val] for val in row) for row in brightArray)

        if args.output:
            with open(args.output, 'w') as f:
                f.write(ascii_art)
        else:
            print(ascii_art)

if __name__ == "__main__":
    main()