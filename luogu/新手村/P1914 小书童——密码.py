# -*- coding: utf-8 -*-

num = int(input())%26
pwd = [ord(x) for x in input()]
pwd_new = ""

for i in pwd :
    i += num
    if i > 122 :
        i -= 26
    pwd_new += chr(i)

print(pwd_new)