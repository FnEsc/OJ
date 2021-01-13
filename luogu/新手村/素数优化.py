# -*- coding: utf-8 -*-
# 素数的倍数都是非素数
import time
import math
start =time.clock()
# 素数优化
# 算出100000000以内的素数
ss=[]
for i in range(31):
    if i%2==0:
        ss.append(0)
    else:
        ss.append(1)
ss[0]=0
ss[1]=0
ss[2]=1

for i in range(3,int(math.sqrt(31))):
    if (bool(ss[i])):
        go=i+i
        while go < 31:
            ss[go]=0
            go+=i
# ss_num=[]
# for i in range(100000000):
#     if bool(ss[i]):
#         ss_num.append(i)

end = time.clock()
print('Running time: %s Seconds'%(end-start))
# print(ss)





# hw_ab_ss=[]
# for i in hw_ab:
#     for j in range(2,int(math.sqrt(i))+1):
#         if i%j == 0:
#             break
#     else :
#         hw_ab_ss.append(i)
# for i in hw_ab_ss:
#     print(i)
# end = time.clock()