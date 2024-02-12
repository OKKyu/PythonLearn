#!python3
# -*- coding:utf-8 -*-
import traceback
import subprocess as subp
from subprocess import SubprocessError, TimeoutExpired

try:
    result = subp.run(args=["ls", "-l"])
    print(result.returncode)

    # if you want to get result of command, set stdout to python.
    result = subp.run(args=["uname"], stdout=subp.PIPE, stderr=subp.PIPE, encoding="utf-8")
    print("Result of uname is... " + result.stdout)

    result = subp.run(args=["firefox", "https://www.google.com"], shell=True)
    print(result.returncode)

except SubprocessError as se:
    print(se.with_traceback())
except TimeoutExpired as te:
    pass
finally:
    pass

