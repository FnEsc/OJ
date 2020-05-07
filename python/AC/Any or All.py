N,arr=[input().split() for _ in range(2)]
print(all([N[0]==N[0][::-1],all([int(i)>0 for i in arr])]))