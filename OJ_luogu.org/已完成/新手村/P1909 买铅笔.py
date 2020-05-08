# -*- coding: utf-8 -*-
import math

need_num = int(input())
[one_num,one_price] = [int(x) for x in input().split()]
[two_num,two_price] = [int(x) for x in input().split()]
[three_num,three_price] = [int(x) for x in input().split()]

# 直接算出三种笔要的价钱

total_one = (math.ceil(need_num/one_num))*one_price
total_two = (math.ceil(need_num/two_num))*two_price
total_three = (math.ceil(need_num/three_num))*three_price

print(min(total_one,total_two,total_three))