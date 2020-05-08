# -*- coding: utf-8 -*-
import time
go=[]
[n,k]=[int(x) for x in input().split()]
E=[int(x) for x in input().split()]
W=[int(x) for x in input().split()]
a=time.clock()
for i in range(n):
    go.append([i,W[i]])    # i编号，W权值
go=sorted(go,reverse=True,key=lambda x:x[1])
for i in range(n):
    go[i][1]+=E[i%10]
go=sorted(go,reverse=True,key=lambda x:x[1])
pr=[]
for i in range(k):
    pr.append(go[i][0])
# print(" ".join(str(x+1) for x in pr))
print(time.clock()-a)