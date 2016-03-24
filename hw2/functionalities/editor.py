__author__ = 'Suota'

import sys
from PIL import Image, ImageEnhance

filename = sys.argv[1]


def part():

    # dividing picture to 4 pieces and merging in different way

    image = Image.open(filename)
    xsize, ysize = image.size
    delta = xsize//4                                # width of one piece of image
    parts = []

    for i in range(4):
        # adding parts of image to a list
        parts.append(image.crop((i*delta, 0, (i+1) * delta, ysize)))

# reversing two of parts
    image.paste(parts[0], (2*delta , 0,3*delta, ysize))
    image.paste(parts[3], (0, 0,delta, ysize))

    out = image
    out.save('parted.gif', "GIF")
    out.show()


def whiten():

    # increasing each of RGB's value

    image = Image.open(filename)
    out = image.point(lambda i: i * 1.01)
    out.save('whitened.gif', "GIF")
    out.show()


def darken():

    # decreasing each of RGB's value

    image = Image.open(filename)
    out = image.point(lambda i: i * 0.9999)
    out.save('darkened.gif', "GIF")
    out.show()


def b_and_white():

    # weakening colors as much as possible

    image = Image.open(filename).convert('RGB')
    enh = ImageEnhance.Color(image)
    out = enh.enhance(0.0)
    out.show()


def edges():

    # weakening edges' sharpness

    image = Image.open(filename).convert('RGB')
    enh = ImageEnhance.Sharpness(image)
    out = enh.enhance(0.0)
    out.show()


def color():

    # weakening colors

    image = Image.open(filename).convert('RGB')
    enh = ImageEnhance.Color(image)
    out = enh.enhance(0.3)
    out.show()


