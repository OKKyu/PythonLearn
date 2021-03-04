#! python3
# -*- coding:utf-8 -*-
'''
  faker テストデータを自動生成するツール。生でない氏名や住所を生成するために使える。
'''
from faker import Faker

# インスタンス生成 ja_JPとすることで、氏名や住所のテストデータを日本用にすることができる。
fakegen = Faker('ja_JP')

# 氏名　１回目
print(fakegen.name())
# 社名
print(fakegen.company())
# 住所
print(fakegen.address())
# 市
print(fakegen.city())
# 日付
print(fakegen.date())
# メアド 引数に @XXX.comや @xxx.co.jpと入れることでドメイン部は固定にすることができる。
print(fakegen.email())
# 郵便番号
print(fakegen.zipcode())
# wordsのように複数のダミーデータを出力するメソッドの場合、引数で個数を指定できる。
# デフォルトは3つ
print(fakegen.words())
print(fakegen.words(2))
print(fakegen.words(10))
# 単語をリスト分割せず、１文字列として出したい場合はtext
print(fakegen.text(100))

# 他にも様々なダミーデータが生成できる。以下にリストがある。
# https://www.nblog09.com/w/2019/01/24/python-faker/