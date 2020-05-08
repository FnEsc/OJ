# -*- coding:utf- 8 -*-
# 题目有错，题目实意为a为1
a=['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty']
b=[i for i in range(1,21)]
num_dict=dict(zip(a,b))
num_dict.update({'a':1})
page=[x for x in input().split()]
num=[]
for i in range(len(page)):
    if num_dict.get(page[i]) != None :
        temp=((num_dict.get(page[i]))**2)%100
        if len(str(temp)) != 2:
            num.append("0"+str(temp))
        else:
            num.append(str(temp))
num=sorted(num,key=lambda x:x[0])
go=''
for i in num:
    go+=str(i)
if go != '' :
    print(int(go))
else:
    print("0")