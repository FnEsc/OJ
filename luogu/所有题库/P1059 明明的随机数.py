# -*- coding: utf-8 -*-
n=int(input())
L=[] # [ [1,2],[2,3] ]
for i in range(n): # [)
    L.append(int(input())) # insert (index,num)
max_num=max(L)
print(L.index(max_num)+1)
print(max_num)