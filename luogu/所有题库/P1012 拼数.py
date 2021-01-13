# -*- coding: utf-8 -*-
n=int(input())
num=[str(x) for x in input().split()]

# 此处要更改sorted中的32和321的顺序,但有难度
# num=sorted(num,reverse=True)
# go=''
# for i in num:
#     go+=i
# print(go)

# 此处直接用组合暴力解决
import itertools
go=[]
go_num=[]
for i in itertools.permutations(num,n):
    go.append(list(i))
for i in go:
    temp=''
    for j in i:
        temp+=j
    go_num.append(temp)
print(max(go_num))