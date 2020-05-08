import itertools
K,M=map(int,input().split())
lst=[]  # 保存所有输入数组中i**2后的值的数组
for _ in range(K):
    lst.append(list([int(x)**2 for x in input().split()[1:]]))
print(max([sum(i)%M for i in list(itertools.product(*lst))]))


