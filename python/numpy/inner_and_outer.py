import numpy as np 

first = np.array(input().split(), dtype=int)
second = np.array(input().split(), dtype=int)

print(np.inner(first, second))
print(np.outer(first, second))