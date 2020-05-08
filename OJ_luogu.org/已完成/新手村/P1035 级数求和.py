# -*- coding: utf-8 -*-

k = int(input())
sn = 0

for n in range(1,9999999) :
    sn += 1/n
    if sn > k :
        print(n)
        break