#! python3
# -*- coding: utf-8 -*-

print('packageSample/sample1 is runned')


def method1(args1='method1 multiple', val1=1, val2=1):
    print(args1 + " is runned")
    print("val1:" + str(val1))
    print("val2:" + str(val2))
    print("val1 * val2 = " + str(val1 * val2))
    print("")


def method2(args1='method2 minus', val1=1, val2=1):
    print(args1 + " is runned")
    print("val1:" + str(val1))
    print("val2:" + str(val2))
    print("val1 - val2 = " + str(val1 - val2))
    print("")


def method3(args1='method3 hello'):
    print(args1 + " is runned")
    print("hello")
    print("")
