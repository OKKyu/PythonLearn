#! python3
# -*- coding:utf-8 -*-

class Player:
    __charactor_count = 0
    def __init__(self, name):
        self.name = name
        Player.__charactor_count +=1
        print(str(Player.__charactor_count) + "番目のプレーヤー" + self.name + "が登場した。")

    def attack(self, enemy):
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

#プロパティをプライベート化する場合は、名称の前に"__"を付与する。

#クラスメソッド作成方法
# 1)def クラス名 (cls): と宣言する
# 2-1)クラス内で プロパティ = classmethod(クラス名) として代入する
# 2-2)@classmethodデコレータをdefの上に付ける
