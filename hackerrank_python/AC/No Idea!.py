import time
x=time.clock()
N,M=map(int,input().split())
array=list(map(int,input().split()))
A=set(map(int,input().split()))
B=set(map(int,input().split()))
happiness=0
for i in range(N):
    # happiness+=array.count(A[i])
    # happiness-=array.count(B[i])
    happiness+=int(array[i] in A)
    happiness-=int(array[i] in B)
print(happiness)
# print(time.clock()-x)
