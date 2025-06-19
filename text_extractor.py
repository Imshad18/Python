#usage: python3 text_extractor.py image.png

import pytesseract  #pip install pytesseract
from PIL import Image #pip install pillow defusedxml olefile
import PIL.ImageEnhance
import sys

pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'

im = sys.argv[1]

image=Image.open(im)
image=image.convert('L')
enhancer=PIL.ImageEnhance.Contrast(image)
image=enhancer.enhance(2.0)
text= pytesseract.image_to_string(image)

print(text)
