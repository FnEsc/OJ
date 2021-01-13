# -*- coding: utf-8 -*-

n = int(input())
list0 = [int(x) for x in input().split()]
# list1存储鱼的比当前可爱的个数,用于输出
list1 = [0]
# list2存储已经比较的鱼
list2 = [list0[0]]
for x in range(1,n) :
    go = 0
    for j in list2 :
        if list0[x] > j :
            go += 1
    list2.append(list0[x])
    list1.append(go)

print(" ".join(str(x) for x in list1))