# -*- coding: utf-8 -*-
import math
[s,x]=[int(x) for x in input().split()]
s_1=max(s-x,0)
s_2=s+x
t_1=math.sqrt(s_1/0.5/0.98)
t_2=math.sqrt(s_2/0.5/0.98)
if (t_2-t_1)>=1:
    print("y")
else:
    print("n")