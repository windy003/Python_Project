from bs4 import BeautifulSoup
import re
import time
import  datetime

def  获得当前页面总金额数(网页源码):
    

    # 获取文件数据并解析
    with open ('网页源码.html','r',encoding='UTF-8') as 源文件变量:
        源文件数据=源文件变量.read()
    bs4解析出来的数据 = BeautifulSoup(源文件数据, "html.parser")
    
    # ----------------计算金额部分开始 ------------------------------------------------------
    #获得所有金额数
    包含总额的金额数列表=[]
    筛选后的数据=bs4解析出来的数据.find_all('span')
    # print(筛选后的数据)
    # print(type(筛选后的数据))
    for 循环参数 in 筛选后的数据:
        if 循环参数.getText().startswith(("￥","总额")):
            包含总额的金额数列表.append(循环参数.getText())
        # print(循环参数.getText())
    # print(包含总额的金额数列表)
    # print(len(包含总额的金额数列表))


    纯金额数列表=[]
    for 循环参数 in 包含总额的金额数列表:
        if 循环参数.startswith("总额"):
            纯金额数列表.append(循环参数[4:])
        else:
            纯金额数列表.append(循环参数[1:])
    
    print(纯金额数列表)
    # print(len(纯金额数列表))


    # 几位=input("请输入你要计算前几位的合")


    # ----------------计算金额部分结束-----------------------------------

    # ----------------------计算时间部分开始-----------------

    时间列表=[]
    筛选后的数据=bs4解析出来的数据.find_all('span',{"class":"dealtime"})
    # print(筛选后的数据)
    # print(len(筛选后的数据))
    for 循环参数 in 筛选后的数据:
            时间列表.append(循环参数.getText())
    print(时间列表)
    print(len(时间列表))


    时间列表最早的一项=时间列表[len(时间列表)-1]
    时间列表最早的一项的时间戳=time.mktime(time.strptime(时间列表最早的一项, '%Y-%m-%d %H:%M:%S'))

    #    -----------------------时间部分结束---------------
    
    #------------------------计算部分----------------------
    开始日期=input("请输入你要查询的开始日期！格式为'YY-MM-DD HH:mm:ss'")
    结束日期=input("请输入你要查询的结束日期！格式为'YY-MM-DD HH:mm:ss'")

    

    开始日期时间戳=time.mktime(time.strptime(开始日期, '%Y-%m-%d %H:%M:%S'))
    结束日期时间戳=time.mktime(time.strptime(结束日期, '%Y-%m-%d %H:%M:%S'))

    global  开始位数
    if  开始日期时间戳  <  时间列表最早的一项的时间戳:
        开始位数=len(时间列表)-1


    for 循环参数 in 时间列表:
        循环参数时间戳=time.mktime(time.strptime(循环参数, '%Y-%m-%d %H:%M:%S'))
        if 循环参数时间戳< 开始日期时间戳:
            开始位数 = 时间列表.index(循环参数)-1
            break
        
        if 循环参数时间戳== 开始日期时间戳:
            开始位数 = 时间列表.index(循环参数)
            break
        

    for 循环参数 in 时间列表:
        循环参数时间戳=time.mktime(time.strptime(循环参数, '%Y-%m-%d %H:%M:%S'))
        global  结束位数
        if 循环参数时间戳<=结束日期时间戳:
            结束位数 = 时间列表.index(循环参数)
            break

        
    print(开始位数)
    print(时间列表[开始位数])

    print(结束位数)
    print(时间列表[结束位数])

    所求金额=sum(float(循环参数) for 循环参数 in 纯金额数列表[结束位数:开始位数])
    
    被计算的日期=[]
    for 循环参数 in 时间列表[结束位数:开始位数+1]:
        被计算的日期.append(循环参数)
    
    print(被计算的日期)

    所求日期的订单数=len(被计算的日期)

    print("你所输入的时间段是：%s 到 %s,  \n \
    被计算的日期是 %s, \n计算出得金额总和是 %f，  \
    \n 所求日期内的订单数是 %d  "     \
    % (开始日期,结束日期,被计算的日期,所求金额,所求日期的订单数))
    

    # -------------------------计算部分结束---------
        
        


    
if   __name__ == '__main__':
    获得当前页面总金额数("D:\\temp\\网页源码.html")   