import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    a = numpy.ones((len(arr)), float)
    i = 0 
    for el in reversed(arr):
        a[i] = el
        i += 1
    return a

arr = input().strip().split(' ')
result = arrays(arr)
print(result)