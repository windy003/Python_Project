import re


# 导入文件
with open('source_Code.html','r',encoding='utf-8') as f:
    f_r=f.read()

# 选出需要检索的代码块txt
txt=re.findall(r'<table class="bought-table-mod(.*?)</td></tr></tbody></table>',f_r,re.S)

# 初始化3个列表
time_whole=[]
title_whole=[]
price_whole=[]

# for循环弄出数据
for t in txt:
    time=re.search('<span class="bought-wrapper-mod__create-time___yNWVS" data-reactid=".0.7:.*?">(.*?)</span>',t,re.S).group(1)
    time_whole.append(time)
    title=re.search('</span><span style="line-height:16px;" data-reactid=".0.7:.*?">(.*?)</span>',t,re.S).group(1)
    title_whole.append(title)
    price=re.search(r'￥(.*?)￥',"".join(re.findall('<span data-reactid=".0.7:.*?">(.*?)</span>',t,re.S)),re.S).group(1)
    price_whole.append(price)
    

# 将3个列表zip一下,并单独一行显示
zipped=zip(time_whole,title_whole,price_whole)
listed_zip=list(zipped)
sorted_list=sorted(listed_zip)
print(sorted_list)
print("["+"\n".join(repr(x) for x in sorted_list)+"]")
