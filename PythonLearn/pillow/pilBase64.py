#!python3
# -*- coding:utf-8 -*-
from PIL import Image
import io
import numpy as np
from base64 import b64encode
from base64 import b64decode


# Open image file as bytes array and encode to base64.
with open("/home/puppy/pic/chessboard.png", "rb") as f:
    enc = b64encode(f.read())

# Save base64 encoded bytes to decode string due to be available on html.
with open("/home/puppy/pic/save_base64.txt", "w") as f:
    enc_str = "data:image/png;base64," + enc.decode()
    f.write(enc_str)

# Testing b64 string can convert to Image.
dec = b64decode(enc_str.split(",")[1].encode())
img = Image.open(io.BytesIO(dec))
img.show()
