import collections
N,arr=[input() for _ in range(2)]
std=collections.namedtuple('std',arr)
print("%.2f" % (sum([float(i.MARKS) for i in [std(*tuple(input().split())) for _ in range(int(N))]])/int(N)))

# import collections
# N,arr=[input() for _ in range(2)]
# std=collections.namedtuple('std',arr)
# d=[]
# for i in range(int(N)):
#     d.append(std(*tuple(input().split())))
# print("%.2f" % (sum([float(i.MARKS) for i in d])/int(N)))