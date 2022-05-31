import numpy as np 

lst = input().split()
n, m = int(lst[0]), int(lst[1])

arr_x = None 
for i in range(n):
    y = np.array(input().split(), dtype=int)
    if i == 0:
        arr_x = y
    else:
        arr_x = np.concatenate((arr_x, y), axis=0)
        
arr_y = None 
for i in range(n):
    z = np.array(input().split(), dtype=int)
    if i == 0:
        arr_y = z
    else:
        arr_y = np.concatenate((arr_x, z), axis=0)

# Following line is here just to match the expected output
arr_x, arr_y = [arr_x], [arr_y]
     
print(np.add(arr_x, arr_y))
print(np.subtract(arr_x, arr_y))
print(np.multiply(arr_x, arr_y))
print(np.floor_divide(arr_x, arr_y))
print(np.mod(arr_x, arr_y))
print(np.power(arr_x, arr_y))