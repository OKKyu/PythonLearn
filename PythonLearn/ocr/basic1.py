#!python3
# -*- coding:utf-8 -*-
import pyocr
import pyocr.builders
import platform
import sys
from PIL import Image

# Setting pyocr
# If environment is windows os, we needs to add path of Tesseract into  "PATH" environment variable.
# If you want to add path with python script, you can write as below.
if platform.system().lower() in 'windows':
    path_tesseract = "C:" + os.sep + "Program Files" + os.sep + "Tesseract-OCR" + os.sep
    if path_tesseract not in os.environ["PATH"].split(os.pathsep):
        os.environ["PATH"] += os.pathsep + path_tesseract

# Getting available tools list.
ocrtools = pyocr.get_available_tools()
if ocrtools is None:
    print("No OcrTool. Please Install pyocr and tesseract.")
    sys.exit(1)
# Getting one of available tool.
ocrtool = ocrtools[0]

#  WordBoxBuilder : 単語単位（画像内の位置座標付き）
#  LineBoxBuilder : 行単位（画像内の位置座標付き）
#  DigitBuilder : 数字のみ  tesseract4.0以降では機能しない？らしい
#  DigitLineBoxBuilder : 数字のみで行単位  tesseract4.0以降では機能しない？らしい

# Reading image.
pdimg = Image.open(sys.argv[1])

# Get builders and Scanning from image to texts.
# TextBuilder
textbuilder = pyocr.builders.TextBuilder()
result = ocrtool.image_to_string(pdimg, lang="jpn", builder=textbuilder)
print("-----result of TextBuilder-----")
print(result)

# WordBoxBuilder
wordbuilder = pyocr.builders.WordBoxBuilder()
result = ocrtool.image_to_string(pdimg, lang="jpn", builder=wordbuilder)
print("-----result of WordBoxBuilder-----")
for box in result:
    print("word:{} confidence:{} location:{}".format(box.content, box.confidence, box.position))

# LineBoxBuilder
print("-----result of LineBoxBuilder-----")
lineboxbuilder = pyocr.builders.LineBoxBuilder()
result = ocrtool.image_to_string(pdimg, lang="jpn", builder=lineboxbuilder)
for linebox in result:
    print("word:{} location:{}".format(linebox.content, linebox.position))
    