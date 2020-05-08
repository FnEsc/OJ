import numpy
N,M=input().split()
my_array = numpy.array([input().split() for _ in range(int(N))],int)
print(numpy.transpose(my_array))
print(my_array.flatten())
