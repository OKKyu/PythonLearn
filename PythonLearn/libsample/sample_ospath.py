#! python3
# -*- coding:utf-8 -*-
import os
import os.path as path

target = "./sample_ospath.py"

#get absolute path
print(path.abspath(target))

#check path is absolute
print(path.isabs(target))
print(path.isabs(path.abspath(target)))

#get relative path from current directory
print(path.relpath(target))

#get relative path from 2nd args to 1st args
print(target, path.relpath("/home"))

#get basename
print(path.basename(path.abspath(target)))
#get dirname
print(path.dirname(path.abspath(target)))

#get both basename and dirname
print(path.split(path.abspath(target)))

#get separated dir names
print(path.abspath(target).split(os.sep))

#get filesize. scale of size is byte
print(path.getsize(target))

#get filelist in indicated directory.
print(os.listdir(path.dirname(target)))

#check the target is exists
print(path.exists(target))

#check the target is dir
print(path.isdir(target))

#check the target is file
print(path.isfile(target))

#check the target is file
print(path.isfile(target))
