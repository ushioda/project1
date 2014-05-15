# -*- coding: utf-8 -*-

import Image
import numpy as np
import os
import glob
from features import feat



##################################################### 
#
# convert images to grayscale 
#
#####################################################

run grayscale_loop.py 

# rename the photo files so that the photos are listed in order

os.chdir('grayfaces')
for f in os.listdir('.'):
    os.rename(f, f.replace('grayface', '')) 
for f in os.listdir('.'):
    if len(f) == 5:
        os.rename(f, '000' + f) 
    if len(f) == 6:
        os.rename(f, '00' + f) 
    if len(f) == 7:
        os.rename(f, '0' + f) 

os.chdir('../graybackground')
for f in os.listdir('.'):
    os.rename(f, f.replace('gray', '')) 
for f in os.listdir('.'):
    if len(f) == 5:
        os.rename(f, 'n000' + f) 
    if len(f) == 6:
        os.rename(f, 'n00' + f) 
    if len(f) == 7:
        os.rename(f, 'n0' + f) 
    if len(f) == 8:
        os.rename(f, 'n' + f) 
        
os.chdir('..')



##################################################### 
#
# extract the features from each photo and save as text
#
##################################################### 
    
# set the number of samples to use in each category 
        
N = 10

# set the width and length of training photos

l = 64

# for faces

os.mkdir('facefeatures')
os.chdir('grayfaces')

i = 0
for file in glob.glob('*.jpg'):
    img = Image.open(file)
    gf = np.array(img.getdata())
    feature = feat(gf, l, l, i)
    os.chdir("../facefeatures")
    np.savetxt(str(i) + '.txt', feature)
    os.chdir('../grayfaces')
    if i == N - 1:
        break
    else:
        i = i + 1
    
os.chdir("..")

# for non-faces

os.mkdir('backgroundfeatures')
os.chdir('graybackground')

i = 0
for file in glob.glob('*.jpg'):
    img = Image.open(file)
    gf = np.array(img.getdata())
    feature = feat(gf, l, l, i)
    os.chdir("../backgroundfeatures")
    np.savetxt('n' + str(i) + '.txt', feature)
    os.chdir('../graybackground')
    if i == N - 1:
        break
    else:
        i = i + 1
    
os.chdir("..")


##################################################### 
#
# find the best decision stumps across samples and features
#
##################################################### 


 
