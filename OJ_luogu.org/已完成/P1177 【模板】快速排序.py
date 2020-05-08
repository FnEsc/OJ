# -*- coding: utf-8 -*-
n=int(input())
L=[int(x) for x in input().split()]
# import random
# L=[]
# for i in range(100):
#     L.append(random.randint(1,1000000000))
# import time
# a=time.clock()
L.sort()
print(" ".join(map(str,L)))
# print(time.clock()-a)