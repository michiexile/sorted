#!/usr/bin/env python

import Image, sys, colorsys

allPixels = []

filenames = sys.argv[1:]
for filename in filenames:
    im = Image.open(filename)
    px = list(im.getdata())
    px = map(lambda (r,g,b): (r/255.0, g/255.0, b/255.0), px)
    px = map(lambda p: colorsys.rgb_to_yiq(*p), px)
    px = sorted(px)
    px = map(lambda p: colorsys.yiq_to_rgb(*p), px)
    px = map(lambda (r,g,b): (int(r*255.0), int(g*255.0), int(b*255.0)), px)
    allPixels.extend(px)
    print "Sorted image: %s" % filename

size = (im.size[0]*im.size[1], len(filenames))
im = Image.new("RGB", size)
im.putdata(allPixels)
im.save("sorted.png")
