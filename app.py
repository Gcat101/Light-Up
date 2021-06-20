from PIL import Image
from shutil import copyfile
import os

orgfile = input('File name (without .jpeg or .png): ')
orgfile = os.path.dirname(os.path.abspath(__file__)) + '/' + orgfile
mode = ''

try:
    file = orgfile + '.png'
    outputfile = copyfile(file, 'output.png')
    mode = 'png'
except FileNotFoundError:
    try:
        file = orgfile + '.jpeg'
        outputfile = copyfile(file, 'output.jpeg')
        mode = 'jpg'
    except FileNotFoundError:
        try:
            file = orgfile + '.jpg'
            outputfile = copyfile(file, 'output.jpg')
            mode = 'jpg'
        except FileNotFoundError:
            print("File not supported (check if you've written the right file name)")
            exit()

img = Image.open(outputfile)

firstpix = img.getpixel((0,0))

for y in range(img.height):
    for x in range(img.width):
        if img.getpixel((x,y)) != firstpix:
            if (mode == 'jpg'):
                img.putpixel((x,y), (255,255,255))
            if (mode == 'png'):
                img.putpixel((x,y), (255))

img.save(outputfile)