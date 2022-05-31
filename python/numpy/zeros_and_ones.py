import numpy as np

lst = input().split()
x, y, z = int(lst[0]), int(lst[1]), int(lst[2])

print(np.zeros((x,y,z), dtype=int))
print(np.ones((x,y,z), dtype=int))