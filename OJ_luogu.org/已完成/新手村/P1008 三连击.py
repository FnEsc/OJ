# -*- coding: utf-8 -*-
# 因为是1:2:3关系，最大的3份关系最大的三位数为999/3且不能重复。
# 则333向上取，则第一个数最大最多可能为为345，大于345不需要验证了

num_set = set([x for x in range(1,10)])

for i in range(123,345+1) :
    j = i*2
    k = i*3
    temp_list = [int(i) for i in str(i)] + [int(j) for j in str(j)] + [int(k) for k in str(k)]
    temp_set = set(temp_list)
    if temp_set == num_set :
        print(i,j,k)