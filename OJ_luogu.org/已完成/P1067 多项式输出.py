# -*- coding: utf-8 -*-
n=int(input())
ai=[int(x) for x in input().split()]
s=''
for i in range(n+1):
    if ai[i]>0:
        s+=("+%dx^%d"%(ai[i],n-i))
    if ai[i]<0:
        s+=("%dx^%d"%(ai[i],n-i))
s=s.replace('x^1+','x+').replace('x^1-','x-').replace('x^0','').replace('-1x','-x').replace('+1x','+x')
if s[0]=='+':
    s=s[1:]
print(s)