# -*- coding: utf-8 -*-

# import sys
# sys.setrecursionlimit(56477364570)


[a,b,c,d]= [int(x) for x in input().split()]

num0 = 0 # num为可行道路的总和
num1 = 0

num = 0

x = 0
y = 0

nostep = [[c,d],[c-2,d-1],[c-2,d+1],[c-1,d+2],[c+1,d+2],[c+2,d+1],[c+2,d-1],[c+1,d-2],[c-1,d-2]]

ok = [[x,y]] # ok为未校对的两步棋子坐标，只记录正常状态的棋子坐标

readly = [] # readly为已记录的棋子正确姿态
readly_two = [] # readl_two为已记录的棋子下两步其中可行的坐标



if (a<0) or (b<0) or (c<0) or (d<0) or (a>20) or (b>20) or (c>20) or (d>20) :
    print(num)
else :
    for i in range(10000000):
        if len(ok) != 0 :

            x = ok[0][0]
            y = ok[0][1]

            if [x,y]==[a,b]:    # 先判断自身
                ok.remove([x,y])
                num += 1
                continue
            if [x,y] in readly : # 判断目前棋子是否在readly中
                i = readly.index([x,y])
                l = len(readly_two[i])
                if l == 1:
                    ok.append(readly_two[i][0])
                else :
                    ok.append(readly_two[i][0])
                    ok.append(readly_two[i][1])
                ok.remove([x,y])
                continue
            else:   # 棋子未在readly中，下面做记录
                if (x<a)&(y<b):
                    if [x+1,y] in nostep :
                        if [x,y+1] in nostep :
                            ok.remove([x,y])
                            continue
                        else :
                            readly.append([x,y])
                            readly_two.append([[x,y+1]])
                            ok.append([x,y+1])
                            ok.remove([x,y])
                            continue
                    if [x,y+1] in nostep :
                        if [x+1,y] in nostep :
                            ok.remove([x,y])
                            continue
                        else :
                            readly.append([x,y])
                            readly_two.append([[x+1,y]])
                            ok.append([x+1,y])
                            ok.remove([x,y])
                            continue
                    if ([x+1,y] or [x,y+1]) == [a,b] :
                        readly.append([x,y])
                        readly_two.append([[a,b]])
                        num += 1
                        ok.remove([x,y])
                        continue
                    readly.append([x,y])
                    readly_two.append([[x+1,y],[x,y+1]])
                    ok.append([x+1,y])
                    ok.append([x,y+1])
                    ok.remove([x,y])
                    continue
                if x==a :
                    readly.append([x,y]) # 记录正常棋子的坐标
                    readly_two.append([[x,y+1]]) # 记录正常棋子的下两步的坐标
                    ok.append([x,y+1])
                    ok.remove([x,y])
                    continue
                if y==b :
                    readly.append([x,y]) # 记录正常棋子的坐标
                    readly_two.append([[x+1,y]]) # 记录正常棋子的下两步的坐标
                    ok.append([x+1,y])
                    ok.remove([x,y])
                    continue
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") # 不可能判断到这里的
                ok.remove([x,y])
                continue
    print(num)
