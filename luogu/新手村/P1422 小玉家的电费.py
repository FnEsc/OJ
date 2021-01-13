# -*- coding: utf-8 -*-
a = int(input())
num = 0


if a>250 :
    if a>400 :
        num = 150*0.4463+250*0.4663+(a-400)*0.5663
    else :
        num = 150*0.4463+(a-150)*0.4663
else :
    num = a*0.4463
print(round(num,1))