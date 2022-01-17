import re

# 将元组列表排序
def  sort_tuple_list(tuple_list):
    return sorted(tuple_list)





# 单行显示函数single_lined()
def single_lined(list_of_tuple):
    single_lined_lists=("\n".join(repr(x) for x in list_of_tuple))
    return single_lined_lists



# 输入文件路径获得排序的元组列表
def get_sorted_zipped_tuple_list_from_a_given_file():
    
    required_file=input("请输入源代码文件路径:")
    print(type(required_file))

    # 导入文件
    with open(required_file,'r',encoding='utf-8') as f:
        f_r=f.read()

    # 选出需要检索的循环代码块txt
    txt=re.findall  (r'class="index-mod__order-container___1ur4- js-order-container"(.*?)</tr></tbody></table></div>',f_r,re.S)



    # 初始化4个列表
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




    # 将4个列表zip一下
    zipped=zip(time_whole,title_whole,price_whole,status_whole)
    listed_zip=list(zipped)


    sorted_tuple_list=sort_tuple_list(listed_zip)
    return sorted_tuple_list
    


def  read_and_merge_lists():

    sorted_tuple_list_01= get_sorted_zipped_tuple_list_from_a_given_file()
    sorted_tuple_list_02= get_sorted_zipped_tuple_list_from_a_given_file()


    required_month_data_01=get_sorted_tupled_list_with_required_month_from_sorted_tuple_list_data(sorted_tuple_list_01)
    required_month_data_02=get_sorted_tupled_list_with_required_month_from_sorted_tuple_list_data(sorted_tuple_list_02)

    merged_list=required_month_data_01 + required_month_data_02
    
    return merged_list



# 根据所要求的月份筛选出数据
def   get_sorted_tupled_list_with_required_month_from_sorted_tuple_list_data(sorted_tuple_list_data):

    required_month=input("请输入你要获取的月份:")

    # for循环找出匹配的项目列表:list_Of_under_number
    list_Of_required=[]
    for i in sorted_tuple_list_data:
        j=(i[0].split("-")[1])
        if  j==required_month:
          list_Of_required.append(i)

    return  list_Of_required







#pie图表
def pie_chart(sorted_tuple_list,title):

    from  pyecharts.charts import Pie
    from  pyecharts import  options as opts


    # 获取每个元素的列表
    titles_list=[]
    price_list=[]
    for i in sorted_tuple_list:
        titles_list.append(i[1])
        price_list.append(i[2])


    # 获取title,price两个列表的元组列表
    tuple_list=list(zip(titles_list,price_list))




    pie=Pie()
    pie.add("",tuple_list)
    pie.set_global_opts(
        title_opts=opts.TitleOpts(title=title),
        legend_opts=opts.LegendOpts(pos_right="right")
    )
    pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{c}:{d}%"))
    pie.render("1.html")



# 计算总价格
def  total_price(data_list,column):
    total_price=0
    for i in data_list:
        total_price += float(i[column])


    return   total_price

# 根据说要求的列打印出数据
def get_required_column(data,column):
    required_column=[]
    for i in data:
        required_column.append(i[column])

    return  required_column


 