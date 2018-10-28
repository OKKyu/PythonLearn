#! python3
# coding: utf-8
# Your code here!

# 引数のデフォルト値
def introduce1(greeting, name="村人"):
	print(  "私は" + name + "です。" + greeting )

introduce1("こんにちは","勇者")
introduce1("こんにちは")

#可変長引数の使用
def introduce2(greeting, *names):
    for name in names:
        print(  "私は" + name + "です。" + greeting )
    
introduce2("こんにちは", "勇者","村人","兵士")

#辞書の使用
def introduce3(**greeter):
	for name, greeting in greeter.items():
		 print("私は" + name + "です。" + greeting)
		
introduce3(hero="はじめまして",villager="こんにちは",soldier="よろしくお願いします")
