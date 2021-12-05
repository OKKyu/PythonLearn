#! python3
# -*- coding: utf-8 -*-
'''
  sample4.py
    Importing from inner package.
'''


# Absoluted Import
import packageSample.sample2 as sam2
# Relative Import
from .. import sample3

print("packageSample.subpack1.sample4 was readed")


def method(args1='sample4 guten'):
    print(args1 + " is runned")
    print("guten morgen")
    print("")


def callSample2():
    sam2.method("CalledSample2Method")


def callSample3():
    sample3.method("CalledSample3Method")
