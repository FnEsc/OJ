import numpy
n=int(input())
A = numpy.array([input().split() for _ in range(n)],int)
B = numpy.array([input().split() for _ in range(n)],int)
print(numpy.dot(A,B))
