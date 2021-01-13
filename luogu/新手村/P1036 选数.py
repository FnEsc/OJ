# -*- coding: utf-8 -*-
import itertools    # python内置排列组合函数https://www.cnblogs.com/aiguiling/p/8594023.html

[n,k] = [int(x) for x in input().split()]
list0 = [int(x) for x in input().split()]

list1 = []  # 存储加起来的数
for i in itertools.combinations(list0, k):
    temp = 0
    for j in i :
        temp += j
    list1.append(temp)

l = len(list1)
for i in list1 :
    for j in range(2,int(i/2)):
        if i%j == 0 :
            l -= 1
            break

print(l)
