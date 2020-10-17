from typing import List

class 解决方案:
    def 函数(self,数组:List[int],目标数值:int)-> List[int]:
        字典={}
        for 索引,值 in enumerate(数组):
            if 值 in 字典:
                return [字典[值],索引]
            else:
                字典[目标数值-值] =索引



案例一 = 解决方案()
print(案例一.函数([11,15,2,7],9))