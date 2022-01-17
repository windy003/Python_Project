from   some_Functions import *


sorted_tuple_list=get_sorted_zipped_tuple_list_from_a_given_file()
# print(len(sorted_tuple_list))

# single_lined_result=single_lined(sorted_tuple_list)
# print(single_lined_result)

# required_column_result=get_required_column(sorted_tuple_list,3)
# print(required_column_result)


# single_lined_single_list=single_lined(required_column_result)
# print(single_lined_single_list)

required_month_data=get_sorted_tupled_list_with_required_month_from_sorted_tuple_list_data(sorted_tuple_list)
print(required_month_data)

pie_chart(required_month_data,"12月份淘宝交易情况")


total_price=total_price(required_month_data,2)
print("总消费"+str(total_price)+"元")   