# -*- coding: utf-8 -*-
# 此类型题目必须从低向高递归上去才好
n = int(input())
# total为临时变量
total = 0
# num_list为记录该数可叠加次数
num_list = [0]
i = 1
while i <= n/2 :
    total = 1
    j = 1
    # print(i)
    while j <= i/2 :
        total += num_list[j]
        j += 1
        # print(i,j)
    num_list.append(total)
    i += 1

final = 1
for k in num_list :
    final += k
print(final)
# print(num_list)