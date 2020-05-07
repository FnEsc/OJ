# N=int(input())
# a=set(map(int,input().split()))
# M=int(input())
# b=set(map(int,input().split())) # 等价上4条
a,b = [set(input().split()) for _ in range(4)][1::2] # [x:y:n] : 从x到y-1，每n个取一个制作切片
c=list(map(str,(sorted(a.difference(b).union(b.difference(a)),key=int))))
print("\n".join(c))