字母列表=[]
for letter in range(65,91):
     字母列表.append(chr(letter))

import pathlib
for 字母循环 in 字母列表:
    文件名 = 字母循环+".txt"
    pathlib.Path(文件名).touch()
