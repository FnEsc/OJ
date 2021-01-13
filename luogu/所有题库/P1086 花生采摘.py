# -*- coding: utf-8 -*-
[M,N,K]=[int(x) for x in input().split()]   # M行 N列 K时间
cb=[]
max_num=0
total=0
for i in range(M):
    cb.append([i,[int(x) for x in input().split()]])
    temp_max=max(cb[i][1])
    max_num=max(temp_max,max_num)
while max_num!=0:
    for i in range(M):
        if max_num in cb[i][1]:
            x=i
            y=cb[i][1].index(max_num)
            break
    if total==0:
        if K-i-i-2-1>=0:
            K=K-i-1-1
            total+=max_num
            max_num=0
            x_now=x
            y_now=y
        else:
            break
    else:
        if K-abs(x-x_now)-abs(y-y_now)-i-1-1>=0:
            K=K-abs(x-x_now)-abs(y-y_now)-1
            total+=max_num
            max_num=0
            x_now=x
            y_now=y
        else:
            break
    cb[i][1][y]=0
    for i in range(M):
        temp_max=max(cb[i][1])
        max_num=max(temp_max,max_num)
print(total)