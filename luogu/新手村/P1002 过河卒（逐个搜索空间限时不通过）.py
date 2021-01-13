# -*- coding: utf-8 -*-

import sys
sys.setrecursionlimit(9999999999999)

[a,b,c,d]= [int(x) for x in input().split()]

num = 0 # num为可行道路的总和

x = 0
y = 0

nostep = [[c,d],[c-2,d-1],[c-2,d+1],[c-1,d+2],[c+1,d+2],[c+2,d+1],[c+2,d-1],[c+1,d-2],[c-1,d-2]]

ok = [[x,y]]

# 选择可行坐标建立数组
def selfok(x,y):
    global num
    global ok
    if [x,y] in nostep :
        ok.remove([x,y])
        return 1
    if [x,y]==[a,b]:
        ok.remove([x,y])
        num += 1
        return 1
    if (x<a) and (y<b):
        ok.append([x+1,y])
        ok.append([x,y+1])
        ok.remove([x,y])
    if (x==a):
        ok.append([x,y+1])
        ok.remove([x,y])
    if (y==b):
        ok.append([x+1,y])
        ok.remove([x,y])




if (a<0) or (b<0) or (c<0) or (d<0) or (a>20) or (b>20) or (c>20) or (d>20) :
    print(num)
else :
    while len(ok) !=0 :
        # print("此时为")
        # print(ok)
        selfok(ok[0][0],ok[0][1])
    print(num)

