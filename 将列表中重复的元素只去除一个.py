import numpy as np

#声明一个列表变量
列表=[1,1,1,2,2,2,3,3,]


#计算出重复元素的位置
重复元素的位置=[]
for 循环变量 in 列表:
    if 列表.count(循环变量)>=2:
        重复元素的位置.append(列表.index(循环变量))

print(重复元素的位置)

#将重复元素的位置去重
重复元素第一次出现的位置=np.unique(重复元素的位置)
print(重复元素第一次出现的位置)

#将去重后的变量转为列表类型
重复元素第一次出现的位置转为列表类型=重复元素第一次出现的位置.tolist()
print(重复元素第一次出现的位置转为列表类型)



#将列表中第一个重复元素去掉，因为位置每删除一个就会变,所以引入 
# 循环变量 调整
循环变量=0
for 循环参数 in 重复元素第一次出现的位置转为列表类型:
    循环参数-=循环变量
    列表.pop(循环参数)
    循环变量+=1

#打印结果
print(列表)
