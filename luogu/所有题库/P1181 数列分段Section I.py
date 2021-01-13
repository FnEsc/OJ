# -*- coding:utf-8 -*-

N,M = [int(x) for x in input().split()] # N为长度,M为和
list0=[int(x) for x in input().split()]
total=0
temp=0
i=0
while i<N :
    temp+=list0[i]
    if temp<M: # 有剩
        i+=1
        continue
    elif temp==M: # 刚好
        i+=1
        total+=1
        temp=0
        continue
    else: # 超出
        total+=1
        temp=0
        continue
if temp!=0:
    total+=1
print(total)


