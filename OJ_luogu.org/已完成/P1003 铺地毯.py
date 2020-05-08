# -*- coding: utf-8 -*-
n=int(input())
dz=[]
i=0
while(i<n):
    dz.append([int(x) for x in input().split()])
    i+=1
go=-1
[x,y]=[int(x) for x in input().split()]
for i in range(n):
    if (dz[i][0]<=x<=(dz[i][0]+dz[i][2])) & (dz[i][1]<=y<=(dz[i][1]+dz[i][3])) :
        go=i+1
print(go)