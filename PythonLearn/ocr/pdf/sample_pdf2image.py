#!python3
# -*- coding:utf-8 -*-
'''
   CAUTION!
     Pdf2image library depends on pdftoppm and pdftocairo.
     If you want to use this library, you have to install poppler-utils that including pdftoppm and pdftocairo.
     Reference is...
       https://pypi.org/project/pdf2image/
'''
# import basical modules.
import sys
from pdf2image import convert_from_path
from pdf2image import convert_from_bytes

# import exceptions
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

# convert from pdf file to PIL images.
# Each pages in pdf will be convert to list of images.
images = convert_from_path(sys.argv[1])
# or
#images = convert_from_bytes(open('/home/belval/example.pdf', 'rb').read())

images[0].show()

'''
  full definitions.
  convert_from_path(pdf_path, dpi=200, output_folder=None, first_page=None, last_page=None, fmt='ppm',
                    jpegopt=None, thread_count=1, userpw=None, use_cropbox=False, strict=False, transparent=False,
                    single_file=False, output_file=str(uuid.uuid4()), poppler_path=None, grayscale=False, size=None,
                    paths_only=False, use_pdftocairo=False, timeout=600)
'''
