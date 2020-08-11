#! python3
import qrcode
import os, sys

if len(sys.argv) > 2 and sys.argv[1] != None and sys.argv[2] != None:
    """ argv[1]:embedded string, url. argv[2]:filename.
    """
    img = qrcode.make(sys.argv[1])
    img.save(os.environ["HOME"] + "/Downloads/sample_" + sys.argv[2] + "_qr.png")
    img.show()
else:
    #sample qrcode make google.
    img = qrcode.make("https://www.google.com")
    img.save(os.environ["HOME"] + "/Downloads/google_qr.png")
    img.show()