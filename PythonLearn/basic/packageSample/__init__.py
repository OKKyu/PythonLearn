# -*- coding: utf-8 -*-
# パッケージを import する際、 Python は sys.path 上のディレクトリを検索して、トップレベルのパッケージの入ったサブディレクトリを探します。
# あるディレクトリを、パッケージが入ったディレクトリとしてPython に扱わせるには、ファイル __init__.py が必要です。
# このファイルを置かなければならないのは、 string のようなよくある名前のディレクトリにより、モジュール検索パスの後の方で見つかる
# 正しいモジュールが意図せず隠蔽されてしまうのを防ぐためです。最も簡単なケースでは __init__.py はただの空ファイルで構いませんが、
# __init__.py ではパッケージのための初期化コードを実行したり、後述の __all__ 変数を設定してもかまいません。

# __all__リストに名前を列挙しておくことで、パッケージを外部から * でインポートした時にインポートされる名前を指定することができる。
# 以下の記載によってsample1,2が読み込まれるようにしている。
__all__ = ["sample1", "sample2"]

# __all__に指定されていないモジュールをインポートしようとすると、存在しないモジュールにアクセスした扱いでエラーとなる。
# Traceback (most recent call last):
#  File "pack.py", line 28, in <module>
#    sample3.method()
# NameError: name 'sample3' is not defined

# モジュールが持っていない名前を指定すると以下のように出る。
# Traceback (most recent call last):
#  File "pack.py", line 28, in <module>
#    sample3.method()
# AttributeError: module 'packageSample.sample3' has no attribute 'method'
