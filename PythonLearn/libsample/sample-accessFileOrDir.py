#! python3
# -*- coding:utf-8
import sys

#The pathlib module -- オブジェクト指向のファイルシステムパス。
if sys.version >= '3.4.0':
    from pathlib import Path
    p = Path("/home/puppy/pic/")
    print("inputed path:" + str(p.absolute()))
    
    for i,subPath in enumerate(p.iterdir()) :
        print("path" + str(i+1) + ":" + str(subPath))

#file pattern matching for Unix OS
import glob
print(glob.glob("/home/puppy/*"))
#NG. not only recursive=True
print(glob.glob("/home/puppy/pic/*.jpg",recursive=True))
#OK. ** used into path fraver.
print(glob.glob("/home/puppy/pic/**/*.jpg",recursive=True))

