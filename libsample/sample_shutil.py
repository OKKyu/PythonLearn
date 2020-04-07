#! python3
# -*- coding:utf-8 -*-
import shutil,os
saveCur = os.path.abspath(os.path.curdir)

#copy 1file. 1st args is copied file, 2nd args is target folder (or renamed filename).
#if already exists same name file, it's overwrited.
shutil.copy("rsample.txt", "/tmp")

#move 1file. 1st args is copied file, 2nd args is target folder (or renamed filename).
#if already exists same name file, this method failuer.
shutil.move("bacon.txt", "/tmp")

#copy 1 directory.
#2nd directory is maked by the copytree method.
#if already exists 2nd args directory, then exception has occured.
shutil.copytree("./", "/tmp/backup")

os.chdir("/tmp")
f = open("./rsample.txt")
print(f.read())
f.close()


os.chdir(saveCur)
#remove 1file.
os.unlink("/tmp/bacon.txt")

#remove 1 directory.
#if target directory have least 1 file or directory, this method failuer.
#os.rmdir("/tmp/backup")

#remove 1 directory within files and directory together.
shutil.rmtree("/tmp/backup")