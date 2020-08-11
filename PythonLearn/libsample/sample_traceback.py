#! python3
# -*- coding:utf-8 -*-
import traceback

try:
    raise Exception("error test")
except Exception as ex:
    f = open("traceback.log", "w")
    #f.write(traceback.format_exc())
    f.write(str(ex) + "\n" + traceback.format_exc())
    f.close()
    print(traceback.format_exc())