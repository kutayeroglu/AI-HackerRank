'''
Difficulty: EASY
Link: https://www.hackerrank.com/challenges/botcleanr
'''

#!/bin/python3

def nextMove(posr, posc, board):
    #Board size as a dynamic parameter
    board_size = 5
    
    # Garbage row, column information
    dirt_r = 0
    dirt_c = 0 
    
    for i in range(board_size):
        for j in range(board_size):
            if board[i][j] == "d":
                dirt_r = i
                dirt_c = j
    
    if posr == dirt_r and posc == dirt_c:
        print("CLEAN")
    elif posr > dirt_r:
        print("UP")
    elif posr < dirt_r:
        print("DOWN")
    elif posc > dirt_c:
        print("LEFT")
    elif posc < dirt_c:
        print("RIGHT")

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    nextMove(pos[0], pos[1], board)