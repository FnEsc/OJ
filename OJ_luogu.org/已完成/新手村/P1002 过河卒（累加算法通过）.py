# -*- coding: utf-8 -*-

[a,b,c,d]= [int(x) for x in input().split()]


x = 0
y = 0

nostep = [[c,d],[c-2,d-1],[c-2,d+1],[c-1,d+2],[c+1,d+2],[c+2,d+1],[c+2,d-1],[c+1,d-2],[c-1,d-2]]

readly = [[0,0]] # readly为已记录的棋子坐标
readly_step = [1]



if (a<0) or (b<0) or (c<0) or (d<0) or (a>20) or (b>20) or (c>20) or (d>20) :
    print(num)
else :
    for y in range(b+1) :
        for x in range(a+1):
            if [x,y] in nostep :
                readly.append([x,y])
                readly_step.append(0)
            else :
                if [x-1,y] in readly :
                    i = readly.index([x-1,y])
                    i = readly_step[i]
                else :
                    i = 0
                if [x,y-1] in readly :
                    j = readly.index([x,y-1])
                    j = readly_step[j]
                else :
                    j = 0
                readly.append([x,y])
                readly_step.append(i+j)
            # print("正在检验",str(x),str(y),str(i),str(j))
    i = readly.index([a,b])
    num = readly_step[i]
    print(num)