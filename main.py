from PIL import Image
import numpy as np

CHARACTERS = ".:-=+*≡#@" # The reference array for substituting pixels with characters, in decreasing brightness (. = lightest pixel, @ = darkest pixel)


def getCharacter(brightness_value: float, brightness_interval: list[float, float] ) -> str:
    # This function is a little tricky, but since the intervals are all the same size and we know the minimum and maximum values of x, we can use a more efficient approach by calculating the interval index and then mapping this index to the corresponding discrete value.



    interval_size = brightness_interval[1] - brightness_interval[0]
    step = interval_size / len(CHARACTERS)

    # This is bad practice!! But there is a problem when the brightness_value = max brightness, so that it's mapped outside of the array. This is the best solution I could think at the moment.
    if brightness_value == brightness_interval[1]:
        return CHARACTERS[-1]
    else:
        index = int((brightness_value - brightness_interval[0]) / step)


    return CHARACTERS[index] 





def main():
    # The idea here is to crop the original image into a square of 100x100 pixels, which is the number of characters we are using to display the ASCII art. S
    with Image.open('cat.jpg') as img:
        img.thumbnail([100, 100])
        px = img.load()

        brightArray = np.zeros([100,100])
        for i in range(100):
            for j in range(100):
                pixelRGB = img.getpixel((i,j))
                R,G,B = pixelRGB
                brightness = sum([R,G,B])/3
                brightArray[i,j] = brightness

    
    Output = ''
    brightInterval = [np.min(brightArray), np.max(brightArray)]
    
    for line in brightArray:
        for val in line:
            Output += getCharacter(val, brightInterval)
        Output += '\n'

    f = open("output.txt", "w")
    f.write("////////////////////////////////////////////////////////////////////////////\n")
    f.write(Output)
    f.close()
    print("Output written into output.txt. Check out your newest art!")







if __name__ == '__main__':
    main()