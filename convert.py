#!/usr/bin/env python3

# The image file must be in the current directory, and must be named 'mypic.bmp'.
# The image dimensions cannot exceed 40 wide by 30 tall.

import sys
from PIL import Image

CONST = {
    'dbwidth': 40,
    'dbheight': 30,
    'dbxswitch': 30
}

# FIXME Tell the user the reason why the image is invalid.
try:
    myimg = Image.open('mypic.bmp')
    width, height = myimg.size
except:
    sys.exit()
if width > CONST['dbwidth'] or width < 1:
    sys.exit()
elif height > CONST['dbheight'] or height < 1:
    sys.exit()

# Define some helper functions.
def convertNumToHex(num, pad):
    output = hex(num).upper().lstrip('0X')
    while len(output) < pad:
        output = '0' + output
    return output
def convertRGBAtoHex(color):
    r = convertNumToHex(color[0], 2)
    g = convertNumToHex(color[1], 2)
    b = convertNumToHex(color[2], 2)
    return (r + g + b)
def writePixel(pixel):
    global content
    # If it's pure white, ignore it.
    if pixel == (255, 255, 255):
        return
    hexcode = convertRGBAtoHex(pixel)
    #alpha = int(pixel[3] * 100 / 255)
    content += str(pixelNumber) + ',' + hexcode + ',' + str(alpha) + ','

# Main loop.
content = ''
pixelNumber = 0
alpha = 100
for y in range(height):
    for x in range(width):
        if x == CONST['dbxswitch']:
            break
        pixel = myimg.getpixel((x, y))
        writePixel(pixel)
        pixelNumber += 1
for y in range(height):
    for x in range(CONST['dbxswitch'], width):
        pixel = myimg.getpixel((x, y))
        writePixel(pixel)
        pixelNumber += 1

content += 'END'
outputFile = open('DrawingBoard.txt', 'w')
outputFile.write(content)
outputFile.close()
