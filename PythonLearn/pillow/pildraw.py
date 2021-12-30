#!python3
# -*- coding:utf-8 -*-
from PIL import Image, ImageDraw, ImageFont

im = Image.new("RGB", (300, 300), "blue")  # Imageインスタンスを作る
draw = ImageDraw.Draw(im)  # im上のImageDrawインスタンスを作る
fnt = ImageFont.truetype('./Kokoro.otf', 30)  # ImageFontインスタンスを作る
draw.text((0, 0), "日本語の\n文字だよ", font=fnt)  # fontを指定
im.save("./test.png")
