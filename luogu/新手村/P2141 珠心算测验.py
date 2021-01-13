# -*- coding: utf -8 -*-
n = int(input())

# list0为原输入的集合
list0 = [int(x) for x in input().split()]

# list_ok为存储符合题意的正整数
list_ok = []

for i in list0 :
    for j in list0 :
        for k in list0 :
            if i==(j+k) and j!=k :
                list_ok.append(i)

print(len(set(list_ok)))