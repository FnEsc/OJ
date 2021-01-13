# -*- coding: utf-8 -*-

[a,b] = [int(x) for x in input().split()]
one = a+b
[a,b] = [int(x) for x in input().split()]
two = a+b
[a,b] = [int(x) for x in input().split()]
three = a+b
[a,b] = [int(x) for x in input().split()]
four = a+b
[a,b] = [int(x) for x in input().split()]
five = a+b
[a,b] = [int(x) for x in input().split()]
six = a+b
[a,b] = [int(x) for x in input().split()]
eleven = a+b

addlist = [one,two,three,four,five,six,eleven]
themax = max(addlist)
if themax > 8 :
    print(addlist.index(themax)+1)
else :
    print("0")

