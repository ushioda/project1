# -*- coding: utf-8 -*-

import os
import glob
import Image
import ImageOps


# convert the face images to grayscale

os.mkdir("grayfaces")
os.chdir("faces")

for file in glob.glob('*.jpg'):    
    os.chdir("../faces")
    img1 = Image.open(file)
    img2 = ImageOps.grayscale(img1)
    os.chdir("../grayfaces")
    img2.save("gray" + file)
    
os.chdir("..")


# convert the non-face images to grayscale

os.mkdir("graybackground")
os.chdir("background")

for file in glob.glob('*.jpg'):    
    os.chdir("../background")
    img1 = Image.open(file)
    img2 = ImageOps.grayscale(img1)
    os.chdir("../graybackground")
    img2.save("gray" + file)
    
os.chdir("..")


# convert the class photo to grayscale

img1 = Image.open("class.jpg")
img2 = ImageOps.grayscale(img1)
img2.save("grayclass.jpg")