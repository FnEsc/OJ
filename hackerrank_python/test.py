from itertools import product
k,m=map(int,input().split())
p=product(*(map(int,input().split()[1:]) for _ in range(k)))
print(list(sum(x*x for x in t)%m for t in p))