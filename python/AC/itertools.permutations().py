import itertools
arr,N=[sorted(i) for i in input().split()]
print("\n".join(["".join((list(map(str,i)))) for i in list(itertools.permutations(arr,int(N[0])))]))