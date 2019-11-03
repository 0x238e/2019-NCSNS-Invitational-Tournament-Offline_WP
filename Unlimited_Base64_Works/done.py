#!/usr/bin/python3
# -*- coding: UTF-8 -*-
 
from PIL import Image
import pytesseract
 
text=pytesseract.image_to_string(Image.open('w.JPG'),lang='eng')
print(text)