# -*- coding: utf-8 -*-
str0 = input()
bsm = int(str0[0])*1+int(str0[2])*2+int(str0[3])*3+int(str0[4])*4+int(str0[6])*5+int(str0[7])*6+int(str0[8])*7+int(str0[9])*8+int(str0[10])*9

bsm = bsm%11
if bsm == 10 :
    bsm = str("X")
bsm = str(bsm)
if bsm == str0[12] :
    print("Right")
else :
    print(str(str0[:-1])+bsm)