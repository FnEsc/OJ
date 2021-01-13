# -*- coding: utf-8 -*-

[n,x] = [int(x) for x in input().split()]
stay = [x for x in range(n+1)]
mov = []
for x in range(x) :
    [i,j] = [int(x) for x in input().split()]
    mov += [x for x in range(i,j+1)]
print(len(list(set(stay) - set(mov))))