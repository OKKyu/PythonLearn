#! python3 
# -*- coding:utf-8 -*-

f = open("./rsample.txt", "r")
#reading that all texts in the file.
print(f.read())
f.close()

f = open("./rsample.txt", "r")
#reading that all texts in the file by list.
print(f.readlines())
f.close()

#open file writing mode with clear mode.
#if bacon.txt isn't exists, bacon.txt is automatically created.
f = open ("bacon.txt", "w")
f.write("Hello! World! Hello! Bacon!!\n")
f.close()

#open file with writing mode with added mode.
#if bacon.txt isn't exists, bacon.txt is automatically created.
f = open ("bacon.txt", "a")
f.write("bacon isn't vegetable. He is Philosophier...?\n")
f.close()

f = open("bacon.txt")
print(f.read())