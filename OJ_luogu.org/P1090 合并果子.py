# -*- coding:utf-8 -*-
n=int(input())
list0=[int(x) for x in input().split()]
import time
a=time.clock()
sum_all=0
list0.sort()
while len(list0)!=1 :
    temp=list0.pop(0)
    temp+=list0.pop(0)
    sum_all+=temp   # temp为当前两个最小值和
    # list0.append(temp)
    for j in range(len(list0)-1):
        if temp<=list0[j]:
            list0.insert(j,temp)
            break
    # print(sum_all)
    # print(list0)
sum_all+=(list0[0]+temp)
print(sum_all)
print(time.clock()-a)