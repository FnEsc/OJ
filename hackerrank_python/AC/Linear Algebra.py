import numpy
N=int(input())
print(round(numpy.linalg.det(numpy.array([list(map(float,input().split())) for _ in range(N)])),2))
