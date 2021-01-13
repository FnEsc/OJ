# -*- coding: utf-8 -*-
n=int(input())
std=[]
for i in range(n):
    [y,s,e]=[int(x) for x in input().split()]   # yse分别为语数英
    std.append([i+1,y,s,e,sum([y,s,e])])
std=sorted(std,key=lambda x:(x[4],x[1]),reverse=True)
for i in range(5):
    print(std[i][0],std[i][4])
