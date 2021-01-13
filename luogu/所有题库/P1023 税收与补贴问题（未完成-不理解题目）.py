# -*-coding: utf-8 -*-

# 政府期望
exp=int(input())
[std_pri,std_sales]=[int(x) for x in input().split()]
# 成本额与成本销售量
std_profit=(exp-std_pri)*std_sales
print("政府期望利润：%d"%std_profit)
# 市场调查
pri_and_sales={}
pri=[]
sales=[]
profit=[]
while 1:
    [x,y] = [int(x) for x in input().split()]
    if [x,y]==[-1,-1]:
        break
    pri_and_sales.update({x:y})
    pri.append(x)
dec=int(input())
h_pri=max(pri)
temp_pri=h_pri
temp_sales=pri_and_sales.get(h_pri)-dec
while (temp_sales)>0 :
    temp_pri+=1
    pri_and_sales.update({temp_pri:temp_sales})
    temp_sales-=dec
for eachitem in pri_and_sales.items():
    profit.append((eachitem[0]-std_pri)*eachitem[1])
h_profit=max(profit)
if h_profit>std_profit:
    print("NO SOLUTION")
else:
    print(profit)
print(pri_and_sales)
print(profit)