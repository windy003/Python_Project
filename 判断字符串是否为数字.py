def isnumber(str_number):  # 判断字符串是不是数字
    if type(str_number) is int or type(str_number) is float:  # 如果参数是数字型或浮点型，返回True
        return True
    if type(str_number) != str or len(str_number) < 1:  # 如果参数不是字符串型或长度小于1，返回False
        return False
    symbol1 = ('+', '-', '正', '负')  # 正负号
    symbol2 = ('.', '点')  # 小数点
    if str_number[0] in symbol1:  # 如果首字符是符号，那么整个字符串去除符号
        str_number = str_number[1:]
        if len(str_number) < 1:  # 如果去除符号后长度为0，判断不是数字
            return False
    elif str_number[0] in symbol2:  # 首字符不能为小数点
        return False
    number = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
              '零', '一', '二', '三', '四', '五', '六', '七', '八', '九')  # 匹配模板
    result = True  # 预设结果是True
    point_times = 0  # 小数点次数
    str_len = len(str_number)  # 计算整个字符串长度
    for i in range(str_len):   # 遍历整个字符串
        if str_number[i] in symbol2:  # 如果当前字符是小数点
            point_times += 1  # 小数点次数＋1
            if point_times > 1:  # 小数点出现次数多于1个
                result = False  # 判断字符串不是数字
                break
        elif str_number[i] not in number:  # 如果当前字符不在模板内
            result = False  # 判断字符串不是数字
            break
    return result


str_list1 = [1234, '134', '134.151', '-134', '一二三', '正三四五', '负四五六', '正三点一四一五']
str_list2 = ['-', '--13', '34..421', '.134']

for i in str_list1:
    print(f"当前参数{i}{'是数字！' if isnumber(i) else '不是数字！'}")
print('-'*50)
for i in str_list2:
    ret = '是数字！' if isnumber(i) else '不是数字！'
    print(f"当前参数{i}{'是数字！' if isnumber(i) else '不是数字！'}")

out:
当前参数1234是数字！
当前参数134是数字！
当前参数134.151是数字！
当前参数-134是数字！
当前参数一二三是数字！
当前参数正三四五是数字！
当前参数负四五六是数字！
当前参数正三点一四一五是数字！
--------------------------------------------------
当前参数-不是数字！
当前参数--13不是数字！
当前参数34..421不是数字！
当前参数.134不是数字！
