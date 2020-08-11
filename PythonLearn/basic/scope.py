#!python3
# -*- coding:utf-8 -*-

def scope():
    loc = "init"
    def do_local():
        #no direction: loc is local member of method.
        loc = "local"
    def do_nonlocal():
        #nonlocal direction: loc is binded external loc (under "def scope():").
        #but this is not global.
        nonlocal loc
        loc = "nonlocal"
    def do_global():
        #global direction: loc is created most external space (global), not in methods.
        global loc
        loc = "global"
        
    do_local()
    print("A:", loc)
    do_nonlocal()
    print("B:", loc)
    do_global()
    print("C:", loc)

scope()
print("D:", loc)

'''
  caution: nonlocal is only supported by python3.
           if version is before 3, nonlocal can't work.
'''