import numpy as np 
np.set_printoptions(legacy='1.13')

lst = input().split(" ")
n, m = int(lst[0]), int(lst[1])

print(np.eye(n,m, k=0))