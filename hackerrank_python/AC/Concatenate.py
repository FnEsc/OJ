import numpy
N,M,P=input().split()
array_1 = numpy.array([input().split() for _ in range(int(N))],int)
array_2 = numpy.array([input().split() for _ in range(int(M))],int)
print(numpy.concatenate((array_1, array_2)))
