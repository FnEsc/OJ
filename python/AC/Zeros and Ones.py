import numpy
nums=tuple(map(int,input().split()))
print(numpy.zeros(nums, dtype = numpy.int)) # 维度,行,列
print(numpy.ones(nums, dtype = numpy.int)) # 维度,行,列