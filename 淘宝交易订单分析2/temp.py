import re



# 导入文件
with open('./source_Code_01.html','r',encoding='utf-8') as f:
    f_r=f.read()



# 选出需要检索的循环代码块txt
txt=re.findall  (r'class="index-mod__order-container___1ur4- js-order-container"(.*?)</tr></tbody></table></div>',f_r,re.S)



# 初始化3个列表
time_whole=[] 
title_whole=[]
price_whole=[]
status_whole=[]

for t in txt:
    time=re.search('<span class="bought-wrapper-mod__create-time___yNWVS" data-reactid=".0.7:.*?">(.*?)</span>',t,re.S).group(1)
    time_whole.append(time)
    title=re.search('</span><span style="line-height:16px;" data-reactid=".0.7:.*?">(.*?)</span>',t,re.S).group(1)
    title_whole.append(title)
    price=re.search(r'"><strong data-reactid="(.*?)><span data-reactid="(.*?)>￥</span><span data-reactid=(.*?)>(.*?)</span></strong></p></div><p style="color',t,re.S).group(4)
    price_whole.append(price)    
    status=re.search(r'<span class="text-mod__link___1rXmw"(.*?)">(.*?)</span>',t,re.S).group(2)
    status_whole.append(status)



