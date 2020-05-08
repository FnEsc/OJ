# -*- coding:utf-8 -*-
max_num=int(input())
n=int(input())
list0=[]
for i in range(n):
    list0.append(int(input()))
list0.sort()
total=0
while len(list0)!=0:
    if len(list0)<=20:
        print(list0,total)
    if len(list0)==1:
        list0.pop(0)
        total+=1
    elif (list0[0]+list0[-1])==max_num:   # 前后刚好
        list0.pop(0)
        list0.pop(-1)
        total+=1
    elif (list0[0]+list0[-1])>max_num:    # 大小组合超出
        list0.pop(-1)
        total+=1
    elif (list0[0]+list0[-1])<max_num:    # 前后还有剩,则应继续推下去两个最大
        for j in range(0,len(list0)):   # 到个数减一,不能到达最大值
            if (list0[j]+list0[-1])>max_num:
                list0.append(list0[j-1]+list0[-1])
                list0.pop(j-1)
                list0.pop(-2)
                break
            elif (list0[j]+list0[-1])==max_num:
                list0.pop(j)
                list0.pop(-1)
                total+=1
                break
            elif (list0[j]+list0[-1])<max_num:
                if j==(len(list0)-1):
                    list0.pop(j)
                    list0.pop(-1)
                    total+=1
                    break
print(total)