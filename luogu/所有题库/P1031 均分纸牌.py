# -*- coding: utf-8 -*-
# 方法一：选出最高值,平均转移数值到左右,方法未能编写出
# 方法二：向右取数,直至平均,本程序用此方法(来自题解)
n=int(input())
A=[int(x) for x in input().split()]
average=sum(A)/n
mov=0
for i in range(n-1):
    if A[i]==average:
        continue
    else:
        A[i+1]+=(A[i]-average)
        mov+=1
print(mov)