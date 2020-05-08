# -*- coding: utf-8 -*-

list0=[]
[N,R,Q]=[int(x) for x in input().split()]
R_02468=[x for x in range(2*N) if x%2==0]
cs=[int(x) for x in input().split()]
sl=[int(x) for x in input().split()]

# import time
# a=time.clock()

for i in range(2*N):
    list0.append({'for_reverse':1000000-i,'index':i+1,'cs':cs[i],'sl':sl[i]})    # index(从1开始),cs,sl

list0=sorted(list0,reverse=True,key=lambda x:(x['cs'],x['for_reverse'])) # 倒排

for i in range(R):
    for j in R_02468: # j为偶数
        if list0[j]['sl']>list0[j+1]['sl']:
            list0[j]['cs']+=1
        else:
            list0[j+1]['cs']+=1
    list0=sorted(list0,reverse=True,key=lambda x:(x['cs'],x['for_reverse'])) # 倒排

print(list0[Q-1]['index'])
# print(time.clock()-a)

