# -*- coding: utf-8 -*-
str0=input()
num = int(str0)
if num<0:
    print("-"+str(int(str0[:0:-1])))
else:
    print(int(str0[::-1]))