# -*- coding: utf-8 -*-

list0 = [int(x) for x in input().split()]
list0 = list0[:-1]
list0 = list0[::-1]
print(" ".join(str(i) for i in list0))