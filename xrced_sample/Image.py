#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx
from PIL import Image

def main():
    filename = "Image.jpg"

    image = Image.open(filename)
    size = width, height = image.size
    print str(width) + " : " + str(height)
    image.thumbnail((120, 80))
    print str(image.width) + " : " + str(image.height)
    image.show()

    del image

if __name__ == "__main__":
    main()

