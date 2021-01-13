# -*- coding: utf-8 -*-
# import time
import math

# 素数优化
num = int(input())
# start =time.clock()
# 算出no以内的素数
# ss=[]
# 方法1：
# for i in range(no):
#     if i%2==0:
#         ss.append(0)
#     else:
#         ss.append(1)
# ss[0]=0
# ss[1]=0
# ss[2]=1

# for i in range(3,int(math.sqrt(no))):
#     if (bool(ss[i])):
#         go=i+i
#         while go < no:
#             ss[go]=0
#             go+=i
ss_num=[2]
# for i in range(no):
#     if bool(ss[i]):
#         ss_num.append(i)
# 方法2：
for i in range(3,num):
    for j in range(2,int(math.sqrt(i))+1):
        if i%j==0:
            break
    else:
        ss_num.append(i)

class Getoutofloop(Exception):
    """抛出异常跳出循环"""
    pass

no=num/3+2
no2=0.7*num+2
try:
    for i in ss_num:
        if i>=no:
            continue
        for j in ss_num:
            if (i+j)>=no2:
                continue
            # for k in ss_num:
            #     if (i+j+k)==num:
            #         print(i,j,k)
            #         raise Getoutofloop()
            k=num-i-j
            if k in ss_num:
                print(i,j,k)
                raise Getoutofloop()
except Getoutofloop:
    pass

# end = time.clock()
# print('Running time: %s Seconds'%(end-start))
# print(3 in ss_num)