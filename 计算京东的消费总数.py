from bs4 import BeautifulSoup
import re

def  获得当前页面总金额数(网页源码):
    
    #获得所有span标签
    with open (网页源码,'r',encoding='ISO-8859-1') as 源文件变量:
        源文件数据=源文件变量.read()
    bs4解析出来的数据 = BeautifulSoup(源文件数据, "html.parser")
    筛选后的数据=bs4解析出来的数据.find_all('span')
    
    # print(筛选后的数据)
    # print(len(筛选后的数据))

    #获得所有金额数
    金额数列表=[]
    # for 循环参数 in 筛选后的数据:
    金额数列表.append([循环参数.string for 循环参数 in 
    筛选后的数据 if bool(re.search("￥", str(循环参数.string)))])

    #获得金额数列表
    # print(金额数列表)
    金额数列表=金额数列表[0]
    # print(金额数列表)
    # print(len(金额数列表))


    #获得存金额数
    金额数列表2=[]
    for 循环参数 in 金额数列表:
        if 循环参数.startswith('总额'):
            循环参数=循环参数[3:]
        金额数列表2.append(循环参数)

    # print(金额数列表2)

    最终金额数列表=[]
    for 循环参数 in 金额数列表2:
        循环参数=循环参数[1:]
        最终金额数列表.append(循环参数)

    print("最终金额数列表为"+str(最终金额数列表))
    print("共有"+str(len(最终金额数列表))+"个")

    # 获得总金额
    总金额=0
    for 循环参数 in 最终金额数列表:
        总金额+=float(循环参数)

    print("总金额为:"+str(总金额))

    # 生成字典
    位置列表=[]
    值列表=[]
    for 位置,值  in enumerate(最终金额数列表):
        位置列表.append(位置)   
        值列表.append(值)
    
    字典=dict(zip(位置列表,值列表))
    # print(位置列表)
    # print(值列表)
    print("最终金额数字典为:"+str(字典))


    # 计算几位前的元素之和
    几位=input('请输入你要计算前几位的和:')
    指定位数的总金额=0
    for 循环参数 in range(int(几位)):
        指定位数的总金额+=float(最终金额数列表[循环参数])
        
    print("指定位数的总金额为:"+str(指定位数的总金额))
    

if   __name__ == '__main__':
    获得当前页面总金额数("D:\\temp\\网页源码.html")   