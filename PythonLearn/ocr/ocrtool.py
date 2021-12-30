#!python3
# -*- coding:utf-8 -*-
import os
import sys
from pathlib import Path
from PIL import Image
from pdf2image import convert_from_path
import pytesseract as tesseract

'''
  Declear Section
'''
target_name = Path(sys.argv[1])
output_name = Path(sys.argv[2])

if platform.system().lower() in 'windows':
    path_tesseract = "C:" + os.sep + "Program Files" + os.sep + "Tesseract-OCR" + os.sep
    if path_tesseract not in os.environ["PATH"].split(os.pathsep):
        os.environ["PATH"] += os.pathsep + path_tesseract


def ocr(image):
    text = tesseract.image_to_string(image, lang="jpn")
    return text


'''
  Validate Section
'''

if target_name.exists() is False or target_name.is_file() is False:
    print("target file isn\'t set. please input filename(pdf, png, or jpg) to first args.")
    sys.exit(1)

if output_name.is_file() is True:
    print("target output name must be directory. please input output-file-name(pdf, png, or jpg) to 2nd args.")
    sys.exit(2)

'''
  Main Section
'''
if target_name.suffix.lower() == ".pdf":
    images = convert_from_path(str(target_name), 600)
    with open(output_name, "a") as f:
        for image in images:
            text = ocr(image)
            f.writelines(text)

elif target_name.suffix.lower() in [".jpg", ".png"]:
    image = Image.open(str(target_name))
    text = ocr(image)
    with open(output_name, "a") as f:
        f.writelines(text)

