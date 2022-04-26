import numpy as np 

n = int(input())
arr = np.zeros((n,n))

for i in range(n):
    lst = input().split(" ")
    for j in range(n):
        arr[i,j] = float(lst[j])

det = np.linalg.det(arr)
# If float, two decimals. If not 1. 
if det % 1 != 0:
    print(format(det, '.2f'))
else:
    print(format(det, '.1f'))