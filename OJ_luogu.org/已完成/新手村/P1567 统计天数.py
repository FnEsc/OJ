# -*- coding: utf-8 -*-
n = int(input())
list0 = [int(x) for x in input().split()]
total = 1
temp = 1
for i in range(1,len(list0)) :
    if list0[i]>list0[i-1] :
        temp += 1
        if temp > total :
            total = temp
    else :
        temp = 1
print(total)

