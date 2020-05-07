import collections
N,arr,n=[[int(x) for x in input().split()] for _ in range(3)]
L=[]
for i in range(n[0]):
    L.append([int(x) for x in input().split()])
dic=collections.Counter(arr)
total=0
for i in L:
    if i[0] in dic.keys():
        if dic[i[0]]: # bool即可,可以不判断其是否为0
            dic[i[0]]-=1
            total+=i[1]
print(total)