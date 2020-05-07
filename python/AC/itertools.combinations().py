import itertools
arr,N=[sorted(i) for i in input().split()]
for i in range(1,int(N[0])+1):
    print("\n".join(list(["".join(i) for i in itertools.combinations(arr,i)])))