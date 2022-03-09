'''
Link to the problem:
https://www.hackerrank.com/challenges/saveprincess?h_r=profile&hr_b=1
'''
#!/usr/bin/python


def displayPathtoPrincess(n,grid):
#print all the moves here
    # Bot is in the middle
    m = int((n-1)/2)
    
    # 4 possible locations for the princess
    if grid[0][0] == "p": 
        for i in range(m):
            print("UP")
            print("LEFT")
    elif grid[0][n-1] == "p":
        for i in range(m):
            print("UP")
            print("RIGHT")
    elif grid[n-1][0] == "p":
        for i in range(m):
            print("DOWN")
            print("LEFT")
    elif grid[n-1][n-1] == "p":
        for i in range(m):
            print("DOWN")
            print("RIGHT")
    else:
        return

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)