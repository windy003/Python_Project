import os

文件路径=input("请输入文件路径:(注意首字母的大小写都会被记录!)")

文件名列表=os.listdir(文件路径)

字母列表=[]

for letter in range(65,91):
     字母列表.append(chr(letter))

名字字典={}
for b in 字母列表:
        名字字典["%s开头的文件或文件夹个数" % b] = 0

for a in 文件名列表:
    for b in 字母列表:
        if a.upper().startswith(b):
            名字字典["%s开头的文件或文件夹个数" % b]+=1

元组列表=zip(名字字典.values(),名字字典.keys())
# 元组列表是一个zip对象
print("共%s个"  % len(文件名列表))
print(sorted(元组列表,reverse=True))
#sorted 可以对所有可迭代的对象进行排序操作，返回的是一个列表
