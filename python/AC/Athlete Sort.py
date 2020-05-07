import collections
N,M=map(int,input().split())
Man=collections.namedtuple('Mam',",".join(map(lambda x:"x"+str(x),range(M))))
# print(Man)
Mans=[Man(*tuple(map(int,input().split()))) for _ in range(N)]
# print(Mans)
sort_mans=sorted(Mans,key=eval("lambda x:x.x{}".format(input())))
for i in sort_mans:
    print(*i)