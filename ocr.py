# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 12:31:59 2018

@author: DELL
"""


import pytesseract
from PIL import Image
m = Image.open("d1.jpg")

text = pytesseract.image_to_string(m, lang = 'eng')
text=pytesseract.image_to_string(m, config='-psm 6')
text
import matplotlib.image as mpimg
img = mpimg.imread('d1.jpg')
img = rgb2gray(imread('image.jpg'));



import numpy as np
import matplotlib.pyplot as plt
charlie = plt.imread('d1.jpg')
#  colormaps plt.cm.datad
# cmaps = set(plt.cm.datad.keys())
cmaps = {'afmhot', 'autumn', 'bone', 'binary', 'bwr', 'brg', 
         'CMRmap', 'cool', 'copper', 'cubehelix', 'Greens'}
X = [  (4,3,1, (1, 0, 0)), (4,3,2, (0.5, 0.5, 0)), (4,3,3, (0, 1, 0)), 
       (4,3,4, (0, 0.5, 0.5)),  (4,3,(5,8), (0, 0, 1)), (4,3,6, (1, 1, 0)), 
       (4,3,7, (0.5, 1, 0) ),               (4,3,9, (0, 0.5, 0.5)),
       (4,3,10, (0, 0.5, 1)), (4,3,11, (0, 1, 1)),    (4,3,12, (0.5, 1, 1))]
fig = plt.figure(figsize=(6, 5))
#fig.subplots_adjust(bottom=0, left=0, top = 0.975, right=1)
for nrows, ncols, plot_number, factor in X:
    sub = fig.add_subplot(nrows, ncols, plot_number)
    sub.set_xticks([])
    plt.colors()
    
    sub.imshow(charlie*0.0002, cmap=cmaps.pop())
    sub.set_yticks([])
#fig.show()
'''
Below is the list of psm options available:

pagesegmode values are: 0 = Orientation and script detection (OSD) only.

1 = Automatic page segmentation with OSD.

2 = Automatic page segmentation, but no OSD, or OCR

3 = Fully automatic page segmentation, but no OSD. (Default)

4 = Assume a single column of text of variable sizes.

5 = Assume a single uniform block of vertically aligned text.

6 = Assume a single uniform block of text.

7 = Treat the image as a single text line.

8 = Treat the image as a single word.

9 = Treat the image as a single word in a circle.

10 = Treat the image as a single character.'''


