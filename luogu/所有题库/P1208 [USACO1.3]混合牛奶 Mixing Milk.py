# -*- coding: utf-8 -*-
N,M = [int(x) for x in input().split()]
M_list=[]
for i in range(M):
    M_list.append([int(x) for x in input().split()])
M_list = sorted(M_list,key=lambda x:x[0])
money=0
need=N
while need>0:
    if M_list[0][1]>=need: # 可以结束了
        money+=need*M_list[0][0]
        break
    else:
        money+=M_list[0][0]*M_list[0][1]
        need-=M_list[0][1]
        M_list.pop(0)
print(money)

