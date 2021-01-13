# -*- coding: utf8 -*-

str0 = input().lower()
art = " "+input().lower()+" "
lsit0 = [x for x in art.split()]

num = lsit0.count(str0)
if num == 0 :
    print("-1")
else :
    print(num,art.find(" "+str0+" "))
