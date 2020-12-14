import  numpy  as  np

列表=[1,1,1,2,2,33,33]


结果列表=[]
for 值一 in 列表:
    结果列表.append([位置 for 位置,值二 in enumerate(列表) if
     值二 == 值一 ])

# print(结果列表)

结果列表=np.unique(结果列表)

结果列表=结果列表.tolist()

print(结果列表)

