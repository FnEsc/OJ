# -*- coding:utf-8 -*-
n=int(input())
list0=[int(x) for x in input().split()]
wait_list=[]
for i in range(n):
    wait_list.append([i,list0[i]])
wait_list=sorted(wait_list,key=lambda x:x[1])
print(" ".join([str(x[0]+1) for x in wait_list]))
wait=0
list0.sort()
for i in range(n):
    wait+=sum(list0[:i])
    # print(wait)
print("%.2f" % (wait/n))