import itertools
m,lst,n=[input().split() for _ in range(3)]
lst_com=itertools.combinations(lst, int(n[0]))
go=0
total=0
for i in lst_com:
    total+=1
    if 'a' in i:
        go+=1
print(round(go/total,4))

# 参考答案
# import itertools
# m,lst,n=[input().split() for _ in range(3)]
# lst_com=itertools.combinations(lst, int(n[0]))
# go=0
# total=0
# for i in lst_com:
#     total+=1
#     if 'a' in i:
#         go+=1
# print(round(go/total,4))