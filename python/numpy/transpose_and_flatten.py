import numpy as np 

lst = input().split()
n,m = int(lst[0]), int(lst[1])

arr_x = None
for i in range(n):
    y = [np.array(input().split(), dtype=int)]
    if i == 0:
        arr_x = y
    else:
        arr_x = np.concatenate((arr_x, y), axis=0)

print(np.transpose(arr_x))
print(arr_x.flatten())