# -*- coding: utf-8 -*-
n = int(input())

list_need = [6,2,5,5,4,5,6,3,7,6]
for i in range(10,3000):
    temp = 0
    for j in str(i):
        temp += list_need[int(j)]
    list_need.append(temp)

# 此处不用遍历，思路：当火柴还有剩的时候，继续加吧

total = 0
for A in range(1200):
    temp_n = 0
    temp_n = 4+list_need[A]  # 表示已用火柴
    if temp_n>=n:
        continue
    for B in range(1200):
        temp_n=temp_n = 4+list_need[A]+list_need[B]
        if temp_n>=n:
            continue
        if (temp_n+list_need[A+B])==n:
            # print("%d + %d = %d"%(A,B,A+B))
            total += 1

print(total)