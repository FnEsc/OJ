# -*- coding: utf-8 -*-
import numpy as np
from numpy import zeros,ones,empty
import itertools,time

start = time.clock()

n = int(input("请输入维度；"))
cols,rows = [],[]
# for i in range(10):
#     col = input("请输入第%s列数据："%i)
#     cols.append(list(map(int,col.split())))
# for i in range(10):
#     row = input("请输入第%s行数据："%i)
#     rows.append(list(map(int,ros.split())))

# print(cols)
# print(rows)


z = np.arange(9).reshape(3,3)

def checknum_res(z, row, col):
    # 返回矩阵z取某行或某列的切割list
    res=[]
    count=0
    if(row!=-1): # 切割行
        temp_list = z[row].tolist() # 取矩阵行转list
        for i in temp_list:
            if i == '1':
                count+=1
            else:
                if count!=0:
                    res.append(count)
                count=0
    else: # 切割列
        temp_list = z[:,row].tolist() # 取矩阵列转list
        for i in temp_list:
            if i == '1':
                count+=1
            else:
                if count!=0:
                    res.append(count)
                count=0
    return(res)


def check_right():
    for i in range(n): # 检查行
        if (checknum_res(a,i,-1) == rows[i]):
            continue
        else:
            return False
    for i in range(n): # 检查列
        if (checknum_res(a,-1,i) == col[i]):
            continue
        else:
            return False

co = 0

arr = [i for i in itertools.product('01', repeat = n)]


for i in itertools.combinations_with_replacement(arr, n):
    co += 1
    # if co == 208:
    #     print("抽样：",i)
print("枚举总数：",co)


print("使用时间：", time.clock()-start, "秒")

