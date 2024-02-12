#!python3
# -*- coding:utf-8 -*-
'''
  This code is referred from https://pypi.org/project/qrcode/.
    version:  from 1 to 40  the smallest version 1 is a 21x21 module matrix
    box_size: module size. scale is pixel.
    border_size: width of border line. scale is pixel.
    
  If you want to know more qrcode, read below.
    https://www.qrcode.com/en/about/version.html
'''
import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('Some data')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("sav.png")
