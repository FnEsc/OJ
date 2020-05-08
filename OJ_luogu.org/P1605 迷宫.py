# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(1000000) # 设置递归深度

N,M,T=[int(x) for x in input().split()] # N行M列T个障碍
a,b,c,d=[int(x) for x in input().split()] # ab起点,cd终点
list_T=[]
for i in range(T):
    list_T.append([int(x) for x in input().split()])
list_T=list_T+[[0,y] for y in range(1,N+1)]+[[M+1,y] for y in range(1,N+1)]+[[x,0] for x in range(1,M+1)]+[[x,N+1] for x in range(1,M+1)]
gone=[]
total=0
def go(x,y):
    print("(%s,%s)"%(x,y),end='->')
    global list_T,a,b,c,d,gone,total
    if [x,y]==[c,d]: # 搜索完成
        total+=1
        print("ok")
        return 1
    else: # 继续搜索
        if [x,y] in gone:
            print("gone")
            return 0
        if [x,y] in list_T:
            print("list_T")
            return 0
        gone.append([x,y]) # 记录棋子此时走过xy
        go(x-1,y)
        go(x+1,y)
        go(x,y-1)
        go(x,y+1)
go(a,b)
print(total)
