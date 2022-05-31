import numpy as np

# Find n, m, p
lst = input().split()
n = int(lst[0])
m = int(lst[1])
p = int(lst[2])

init_array = None
for i in range(n):
    line = [np.array(input().split(), dtype=int)]
    if i == 0:
        init_array = line
    else:
        init_array = np.concatenate((init_array, line), axis=0)
        
for i in range(m):
    line = [np.array(input().split(), dtype=int)]
    init_array = np.concatenate((init_array, line), axis=0)      

print(init_array)