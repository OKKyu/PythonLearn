#! python3
# -*- coding:utf-8 -*-
#Exceptionの基本

import sys
import traceback

def test_exception(number):
    try:
        return 100 / number

    except ZeroDivisionError as e:
        print("zero division has occured")
        raise e
    finally:
        print("処理が終了しました")


try:
    test_exception(0)

except ZeroDivisionError as e:
    sys.stderr.write('0で割り算できません')
    print(traceback.format_exc())

    
#処理の流れ
# ゼロ除算発生
# メソッド内のexcept句が実行される
# finallyが実行される
# raise eによって呼び出し元に委譲される
# 呼び出し元のexcept句が実行される
# raise eをしていない場合は関数を囲うtry句ではキャッチされない。