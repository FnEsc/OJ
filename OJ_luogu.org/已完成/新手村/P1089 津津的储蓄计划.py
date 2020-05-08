# -*- coding: utf-8 -*-

get_money = 300
now_money = 0
month_money = 0
stop_month = 0
y = 0

for i in range(12) :
    out_money = int(input())
    now_money += get_money
    if now_money<out_money :
        if y == 0 :
            stop_month = i+1
            y += 1
        else :
            continue
    now_money -= out_money
    month_money += (now_money//100)*100
    now_money -= (now_money//100)*100
    # print(i+1,month_money,now_money,stop_month)

if stop_month!=0 :
    print(stop_month*(-1))
else :
    print(int(month_money*1.2+now_money))