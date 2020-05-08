# -*- coding: utf: utf-8 -*-

str0 = input()
str1 = input()

num0 = 1
num1 = 1

for i in str0 :
    num0 *= int(ord(i)-64)
for i in str1 :
    num1 *= int(ord(i)-64)

if (num0%47) == (num1%47) :
    print("GO")
else :
    print("STAY")