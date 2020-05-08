# -*- coding: utf-8 -*-
import time
import math

[a,b]=[int(x) for x in input().split()]

start =time.clock()


# 先找回文数（这个回文数必须是奇数）
# 数太大了，可以先根据回文数的特点，列出所有的回文数来形成回文数列表

# 长度为1的回文数
hw_num=[1,2,3,5,7]
# 长度为2的回文数
for i in range(1,10,2):
    temp_hw=i*11
    hw_num.append(temp_hw)
# print("ok2")
# 长度为3的回文数
for i in range(1,10,2):
    for j in range(10):
        temp_hw=i*101+j*10
        hw_num.append(temp_hw)
# print("ok3")
# 长度为4的回文数
for i in range(1,10,2):
    for j in range(10):
        temp_hw=i*1001+j*110
        hw_num.append(temp_hw)
# print("ok4")
# 长度为5的回文数
for i in range(1,10,2):
    for j in range(10):
        for k in range(10):
            temp_hw=10001*i+1010*j+100*k
            hw_num.append(temp_hw)
# print("ok5")
# 长度为6的回文数
for i in range(1,10,2):
    for j in range(10):
        for k in range(10):
            temp_hw=100001*i+10010*j+1100*k
            hw_num.append(temp_hw)
# print("ok6")
# 长度为7的回文数
for i in range(1,10,2):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                temp_hw=1000001*i+100010*j+10100*k+l*1000
                hw_num.append(temp_hw)
# print("ok7")
# 长度为8的回文数
for i in range(1,10,2):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                temp_hw=10000001*i+1000010*j+100100*k+l*11000
                hw_num.append(temp_hw)
# print("ok8")
# print(len(hw_num))


hw_ab=[]
for i in hw_num:
    if i in range(a,b+1):
        hw_ab.append(i)
# print(len(hw_ab))
end = time.clock()
# print('Running time: %s Seconds'%(end-start))

# print(91019 in hw_num)
# 从回文数里找范围
# 从范围回文数中找素数
hw_ab_ss=[]
for i in hw_ab:
    for j in range(2,int(math.sqrt(i))+1):
        if i%j == 0:
            break
    else :
        hw_ab_ss.append(i)
for i in hw_ab_ss:
    print(i)
end = time.clock()
# print('Running time: %s Seconds'%(end-start))

# 素数优化
# 算出100000000以内的素数
# ss=[]
# for i in range(100000000):
#     if i%2==0:
#         ss.append(0)
#     else:
#         ss.append(1)
# ss[0]=0
# ss[1]=0
# ss[2]=1

# for i in range(3,int(math.sqrt(100000000))):
#     if (bool(ss[i])):
#         go=i+i
#         while go < 100:
#             ss[go]=0
#             go+=i
# end = time.clock()
# print('Running time: %s Seconds'%(end-start))

# ss_num=[]
# for i in range(100000000):
#     if bool(ss[i]):
#         ss_num.append(i)

# # 回文素数
# go=[]
# for i in hw_ab:
#     if i in ss_num:
#         go.append(i)
# for i in go :
#     print(i)


# end = time.clock()
# print('Running time: %s Seconds'%(end-start))