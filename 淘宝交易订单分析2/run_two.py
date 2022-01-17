from   some_Functions import *


data=read_and_merge_lists()


pie_chart(data,"11月份淘宝交易情况")


total_price=total_price(data,2)
print("总消费"+str(total_price)+"元")   