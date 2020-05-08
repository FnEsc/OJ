# -*- coding: utf-8 -*-

[n,x] = [x for x in input().split()]
total = ""
for i in range(1,int(n)+1) :
    total += str(i)
print(total.count(str(x)))