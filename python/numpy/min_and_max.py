import numpy as np

lst = input().split(" ")
n, m = int(lst[0]), int(lst[1])
arr = np.zeros((n,m))

for i in range(n):
    lst = input().split(" ")
    for j in range(m):
        arr [i,j] = lst[j]  
print(int(max(np.min(arr, axis = 1))))