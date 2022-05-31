import numpy as np

lst = input().split()

print(np.zeros((tuple(map(int, lst))), dtype=int))
print(np.ones((tuple(map(int, lst))), dtype=int))