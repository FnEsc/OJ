# -*- coding: utf-8 -*-
[a,b,c,d]= [int(x) for x in input().split()]
h = ((c*60+d)-(a*60+b))//60
m = ((c*60+d)-(a*60+b))-h*60
print(h,m)