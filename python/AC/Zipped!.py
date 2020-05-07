N,M=map(int,input().split())
z=zip(*[input().split() for _ in range(M)])
for i in z:
    print(sum(map(float,i))/M)