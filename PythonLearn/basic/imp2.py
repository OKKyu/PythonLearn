#!python3
# -*- coding:utf-8 -*-
'''
重複したインポートについて
  実体は同じモジュールであっても、import句で異なる読み取り方をすると、異なるモジュールとして名前空間に登録される？。
  以下でそれを検証する。
  
  まとめ：
  sys.pathにモジュール取り込む時の問題？らしい。
'''


def test1():
    import packageSample.sampleclass1
    from packageSample import sampleclass1

    print("test1 ")
    i1 = packageSample.sampleclass1.TestClass()
    i2 = sampleclass1.TestClass()

    print("isinstance i1 == sampleclass1.TestClass " + str(isinstance(i1, sampleclass1.TestClass)))
    print("isinstance i2 == sampleclass1.TestClass  " + str(isinstance(i2, sampleclass1.TestClass)))
    print("isinstance i1 == packageSample.sampleclass1.TestClass " + str(isinstance(i1, packageSample.sampleclass1.TestClass)))
    print("isinstance i2 == packageSample.sampleclass1.TestClass  " + str(isinstance(i2, packageSample.sampleclass1.TestClass)))


if __name__ == "__main__":
    test1()
