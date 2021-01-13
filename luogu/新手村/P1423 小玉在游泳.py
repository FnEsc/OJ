# -*- coding: utf-8 -*-

total = 0
k = float(input())
i = 0
step = 2
while (total<k) :
    total += step
    step = step*0.98
    i += 1
    # print(total)
print(i)