import numpy
numpy.set_printoptions(sign=' ')
N,M=tuple(map(int,input().split()))
my_array = numpy.array([input().split() for _ in range(N)],int)
print(numpy.mean(my_array, axis = 1))
print(numpy.var(my_array, axis = 0))
print(round(numpy.std(my_array, axis = None),12))
