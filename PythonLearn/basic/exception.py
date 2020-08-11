#! python3
# -*- coding:utf-8 -*-
#Exceptionの基本

import traceback, sys

print(1)
try:
    number = 0
    answer = 100 / number
    print(answer)
except Exception as e:
    print("予期せぬエラーが発生")
except ZeroDivisionError as e:
    print("0では割り算できません")
    #print(traceback.format_exc())
    sys.stderr.write(traceback.format_exc())
finally:
    print(2)


#その他のException
#NameError  未定義の変数、関数名がある
#TypeError  期待されない型が使用されている
#Exception  全てのエラーのスーパークラス

#Javaの場合は親Exceptionを子Exceptionより上に
#書くと"未到達のコードあり"エラーが出るが、
#pythonでは問題ないようである。

#raise Exception()