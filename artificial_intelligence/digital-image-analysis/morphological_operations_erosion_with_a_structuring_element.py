import numpy as np 

B = np.array([[0,0,1,1,0],
              [0,0,1,1,0],
              [0,0,1,1,0],
              [1,1,1,1,1]])

# Structuring element is [1,1,1] as a column vector

# Erosion
row, column = B.shape[0], B.shape[1]
B_prime = np.copy(B)
for i in range(row):
    for j in range(column):
        if i in [1,2]:
            # Check up and down
            if B[i-1,j] == 0 or B[i+1, j] == 0:
                B_prime[i,j] = 0
        else:
            B_prime[i,j] = 0

print(B_prime)
