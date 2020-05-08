# -*- coding: utf-8 -*-
n=int(input())
# 前i层有temp_i个数，若转向下层为偶数层，则向x方向+1移动。
for i in range(10000):
    temp_i=(1+i)*i/2
    if n<=temp_i:
        break
# 所求数字在第i层,i层内有temp_i个数,i层前有temp_i-i个数
if i%2!=0:
    # 向y+1
    y=n-(temp_i-i)
    x=i+1-y

else:
    # 向x+1
    x=n-(temp_i-i)
    y=i+1-x

print("%d/%d"%(x,y))