#!python3
# -*- coding:utf-8 -*-
import traceback
import subprocess as subp
from subprocess import SubprocessError, TimeoutExpired

try:
    result = subp.run(args=["ls", "-l"])
    print(result.returncode)

    result = subp.run(args=["firefox", "https://www.google.com"], shell=True)
    print(result.returncode)

except SubprocessError as se:
    print(se.with_traceback())
except TimeoutExpired as te:
    pass
finally:
    pass

