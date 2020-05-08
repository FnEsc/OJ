# -*- coding: utf-8 -*-
s=''
W_11=L_11=0
W_21=L_21=0
s_21=[]
flag_11=flag_21=0
while("E" not in s):
    s+=input()
for i in s:
    if i=='W':
        W_11+=1
        W_21+=1
    elif i=='L':
        L_11+=1
        L_21+=1
    elif i=='E':
        break
    if ((W_11>=11)&(L_11<=9)) or ((L_11>=11)&(W_11<=9)) or ((W_11>=10)&(L_11>=10)&((W_11-L_11>=2)or(L_11-W_11>=2))) :
        print("%d:%d"%(W_11,L_11))
        W_11=0
        L_11=0
        flag_11=1
    if ((W_21>=21)&(L_21<=19)) or ((L_21>=21)&(W_21<=19)) or ((W_21>=20)&(L_21>=20)&((W_21-L_21>=2)or(L_21-W_21>=2))) :
        s_21.append("%d:%d"%(W_21,L_21))
        W_21=0
        L_21=0
        flag_21=1
# if (W_11!=0 or L_11!=0) or (flag_11==0):
#     print("%d:%d"%(W_11,L_11))
print("%d:%d"%(W_11,L_11))

print("")

for i in s_21:
    print(i)
# if (W_21!=0 or L_21!=0) or (flag_21==0):
#     print("%d:%d"%(W_21,L_21))
print("%d:%d"%(W_21,L_21))

