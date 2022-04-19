'''
Link to problem:
https://www.hackerrank.com/challenges/saveprincess2?h_r=profile&hr_b=1
'''

def nextMove(n,r,c,grid):
    # Initialize row and colum coordinates of the princess
    p_row = 0
    p_column = 0 
    
    # Find row and column of the princess
    for i in range(n):
        for j in range(n):
            if grid[i][j] == "p":
                p_row = i
                p_column = j
    
    if r > p_row:
        return("UP")
    elif r < p_row:
        return("DOWN")
    if c > p_column:
        return("LEFT")
    elif c < p_column:
        return("RIGHT")

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))