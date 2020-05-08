# -*- coding: utf-8 -*-

num = input()

total = int(num[0])*1+int(num[2])*2+int(num[3])*3+int(num[4])*4+int(num[6])*5+int(num[7])*6+int(num[8])*7++int(num[9])*8++int(num[10])*9

last_num = total%11

if last_num == 10 :
    k = "X"
else :
    k = str(last_num)

if k == num[12] :
    print("Right")
else :
    print(num[:-1]+k)

