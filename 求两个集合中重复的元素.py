def 求交集(集合一, 集合二):
    return  [循环参数 for 循环参数 in 集合一 if 循环参数 in 集合二]




集合一=eval(input("请输如集合一:"))
集合二=eval(input("请输如集合二:"))


def 判断输入是否是单整形(参数):
    if (type(参数)  is tuple):
        return 参数
    else:
        return [参数]

集合一=判断输入是否是单整形(集合一)
集合二=判断输入是否是单整形(集合二)



求交集的结果=求交集(集合一,集合二)

print(set(求交集的结果))