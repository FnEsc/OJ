# -*- coding: utf-8 -*-
[A,B,C]=[int(x) for x in input().split()]
go_list=[]
num_set=set([x for x in range(1,10)])
for a in range(123,333):
    temp_set=[]
    b=(B/A)*a
    c=(C/A)*a
    temp_set.append(a//100)
    temp_set.append(a%100//10)
    temp_set.append(a%10)
    temp_set.append(b//100)
    temp_set.append(b%100//10)
    temp_set.append(b%10)
    temp_set.append(c//100)
    temp_set.append(c%100//10)
    temp_set.append(c%10)
    if set(temp_set)==num_set:
        go_list.append([a,b,c])
        print(int(a),int(b),int(c))

if len(go_list):
    pass
else:
    print("No!!!")