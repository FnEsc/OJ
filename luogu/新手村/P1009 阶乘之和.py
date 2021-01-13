# -*- coding: utf-8 -*-
a = int(input())

add = 0

for i in range(a):
    i += 1
    a = i
    while(i>=2):
        a = a*(i-1)
        i -= 1
    add += a
print(add)