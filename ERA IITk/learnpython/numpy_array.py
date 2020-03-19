import numpy

def arrays(arr):
    arr=arr[::-1]
    x=numpy.array(arr,float)
    return x


arr = input().strip().split(' ')
result = arrays(arr)
print(result)