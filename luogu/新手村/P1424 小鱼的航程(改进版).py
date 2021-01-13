# -*- coding: utf-8 -*-

total = 0
[z,n] = [int(x) for x in input().split()]
m = n
weekend_days = 0

# 先判断到周一
while (z!=1) and (n>0) :
    if z not in range(1,6) :
        weekend_days += 1
    z += 1
    n -= 1
    if z == 8 :
        z = 1

# 周一开始新的一周
weeks = n//7
weekend_days += weeks*2
last_week = n%7
if last_week == 6 :
    weekend_days += 1

# print(weekend_days)
print((m-weekend_days)*250)