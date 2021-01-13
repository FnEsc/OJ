# -*- coding: utf-8 -*-

import sys
sys.setrecursionlimit(56477364570)

[a,b,c,d]= [int(x) for x in input().split()]

num = 0 # num为可行道路的总和

x = 0
y = 0

nostep = [[c,d],[c-2,d-1],[c-2,d+1],[c-1,d+2],[c+1,d+2],[c+2,d+1],[c+2,d-1],[c+1,d-2],[c-1,d-2]]

# 主线向右进行递归
def goright(x,y):
    global num
    if (x<=a)&(y<=b) :
        # prin(x,y)
        if [x,y] in nostep :
            # print("此处为nostep!")
            return 1
        if [x,y]==[a,b]:
            # print("此处OK!")
            num += 1
            return 1
        goright(x+1,y)
        goright(x,y+1)
        return 1
    else :
        # print("超过目标了!")
        return 0


def prin(x,y) :
    print("目前棋子在：",str(x),str(y))

if (a<0) or (b<0) or (c<0) or (d<0) or (a>20) or (b>20) or (c>20) or (d>20) :
    print(num)
else :
    goright(x,y)
    print(num)

