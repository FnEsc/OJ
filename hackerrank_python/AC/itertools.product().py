import itertools
A,B=[[int(x) for x in input().split()] for _ in range(2)]
print(" ".join(map(str,itertools.product(A,B))))