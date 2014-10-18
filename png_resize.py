#!/usr/bin/python
import os, sys
import Image
from sys import *

if (len(sys.argv) < 5):
    print "Usage: ./png_resize.py <input> <output> <size> <size>"
    exit(1)

size = int(argv[3]), int(argv[4])
try:
    im = Image.open(argv[1]).convert("RGBA")
    im.thumbnail(size, Image.ANTIALIAS)
    im.save(argv[2], "PNG")
except IOError:
    print "cannot create thumbnail for '%s'" % arvg[1]
