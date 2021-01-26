#! python3
# -*- coding:utf-8 -*-

class Player:
    __charactor_count = 0
    def __init__(self, name):
        self.name = name
        __charactor_count = 1
        Player.__charactor_count +=1
        print(str(Player.__charactor_count) + "番目のプレーヤー" + self.name + "が登場した。")

    def attack(self, enemy):
        print("キャラカウント:" + str(self.__charactor_count))
        print(self.__charactor_count is Player.__charactor_count)
        print(self.name + "は、" + enemy + "を攻撃した！")
    
    def summary(cls):
        print(str(Player.__charactor_count) + "人で、スライムを攻撃した")
    
    summary = classmethod(summary)

class Wizard(Player):
    def __init__(self):
        super().__init__("魔法使い")

    def attack(self, enemy):
        self.__spell()
        print(self.name + "は、" + enemy + "に炎を放った！")

    def __spell(self):
        print("ズバーン！")

print("=== パーティーでスライムと戦う ===")
hero = Player("勇者")
warrior = Player("戦士")
wizard = Wizard()

party = [hero, warrior, wizard]
for member in party:
    member.attack("スライム")

Player.summary()

#クラスメソッド作成方法
# 1)def 任意のメソッド名 (cls): と宣言する
# 2-1)クラス内で プロパティ = classmethod(クラス名) として代入する
# 2-2)@classmethodデコレータをdefの上に付ける
#変数についてはself.__XXXでも、 クラス名.__XXX でもいいらしい。。。

#クラス補足説明
#・プロパティをプライベート化する場合は、名称の前に"__"を付与する。 
#・メソッドの宣言時、第一引数には必ずselfを入れる。しかし呼び出し元では第二引数以降のみをセットする。
#　各メソッド内部でインスタンス変数（もしくはインスタンスメソッド）へアクセスする場合には"self.変数"、"self.メソッド"とする。
#・継承元メソッドの呼び出し方、オーバーライドの方法はJavaと同じ。
#・インスタンス変数は__init__で"self.AA = 0"として初期化すること。
#  selfを抜いてAA = 0 とするとスコープがメソッド内部のみとなる。
#・self.AAと指定した場合、まずはインスタンス変数があるか検索される。インスタンス変数がない場合は、
#  エラーとならずにクラス変数にAAがあるか検索される。ただしクラス外のスコープまでは検索せず、エラーとなる。