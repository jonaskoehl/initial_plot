#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 09:51:34 2020

@author: jonas
"""

import os

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Ä', 'Ö', 'Ü']

initials = [i + j for j in letters for i in letters]

try:
    os.mkdir("plots")
except FileExistsError:
    pass

for i in initials:
    img = Image.open("sample.jpg")
    draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    font = ImageFont.truetype("arial.ttf", 1000)
    # draw.text((x, y),"Sample Text",(r,g,b))
    draw.text((40, 150),i,(0,0,0),font=font)
    img.save('plots/' +  i + '.jpg')