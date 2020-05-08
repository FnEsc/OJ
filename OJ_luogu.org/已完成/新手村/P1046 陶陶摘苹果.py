# -*- coding: utf-8 -*-
a = [int(x) for x in input().split()]
b = int(input())+30
i = 0
for j in a :
    if b >= j :
        i += 1
print(i)