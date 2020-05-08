# -*- coding: utf-8 -*-
[n,s]=[int(x) for x in input().split()]
[a,b]=[int(x) for x in input().split()]
get_high=a+b
# n个数,s力气,a+b高度
apple_dict={}
for i in range(n):
    [xi,yi]=[int(x) for x in input().split()]
    if yi in apple_dict.keys():
        while yi in apple_dict.keys() :
            yi+=0.00001
            print(yi)
        apple_dict.update({yi:xi})
    else:
        apple_dict.update({yi:xi})
total=0
for yi in sorted(apple_dict.keys()):
    if get_high>=int(apple_dict[yi]):
        s-=int(yi)
        if s>=0:
            total+=1
            # print(yi,apple_dict[yi])
        else:
            break
    else:
        continue
print(total)
print(apple_dict)