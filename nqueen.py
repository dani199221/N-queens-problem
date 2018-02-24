#!/usr/bin/env python
# nrooks.py : Solve the N-Rooks problem!
# D. Crandall, 2016
# Updated by Zehua Zhang, 2017
#
# The N-rooks problem is: Given an empty NxN chessboard, place N rooks on the board so that no rooks
# can take any other, i.e. such that no two rooks share the same row or column.

import sys
import pdb


# Count # of pieces in given row
def count_on_row(board, row):
    return sum( board[row] ) 

# Count # of pieces in given column
def count_on_col(board, col):
    return sum( [ row[col] for row in board ] ) 

def count_on_diag(board, row, col):
    global is_type

    if is_type == "nrook": return -1

    i = row
    j = col
    diag_sum = 0
    while(i >= 0 and j >= 0):
        diag_sum = diag_sum + board[i][j]
        i = i - 1
        j = j - 1
    
    if diag_sum: return diag_sum
    i = row
    j = col
    while(i >= 0 and j < N):
        diag_sum = diag_sum + board[i][j]
        i = i - 1
        j = j + 1
    
    if diag_sum: return diag_sum
    i = row
    j = col
    while(i < N and j < N):
        diag_sum = diag_sum + board[i][j]
        i = i + 1
        j = j + 1

    if diag_sum: return diag_sum
    i = row
    j = col
    while(i < N and j >= 0):
        diag_sum = diag_sum + board[i][j]
        i = i + 1
        j = j - 1
    return diag_sum 

# Count total # of pieces on board
def count_pieces(board):
    return sum([ sum(row) for row in board ] )

# Return a string with the board rendered in a human-friendly format
def printable_board(board):
    global is_type
    piece = "R"
    if is_type == "nqueen": piece = "Q"
    
    return "\n".join([ " ".join([piece if col == 1 else "X" if col == -1 else "_" for col in row]) for row in board])

# Add a piece to the board at the given position, and return a new board (doesn't change original)
def add_piece(board, row, col):
    global x_r
    global x_c
    global is_unavailable
    if (row == x_r and col == x_c and is_unavailable):
        return None
    else:
        return board[0:row] + [board[row][0:col] + [1,] + board[row][col+1:]] + board[row+1:]

# Get list of successors of given board state
def successors(board):
    return [ add_piece(board, r, c) for r in range(0, N) for c in range(0,N) ]

def successors2(board):
    #make an empty list of list
    successors = [[]]
    
    #find the sum of rows and colums and add a piece only if the sum is <1
    for r in range(0, N):
        if( count_on_row(board, r) <= 0):
            for c in range(0,N):
                if(count_on_col(board, c) <= 0) and count_on_diag(board, r, c) <= 0:
                    a = add_piece(board, r, c)
                    if a != None:
                        successors.append(a)
    #pop the useless first element used to create a list of list
    successors.pop(0)
    return successors


# check if board is a goal state
def is_goal(board):
    return count_pieces(board) == N and \
        all( [ count_on_row(board, r) <= 1 for r in range(0, N) ] ) and \
        all( [ count_on_col(board, c) <= 1 for c in range(0, N) ] )

# Solve n-rooks!
def solve(initial_board):
    fringe = [initial_board]
    global dfs
    #condition for dfs
    if dfs: 
        while len(fringe) > 0:
            for s in successors2( fringe.pop() ):
                if is_goal(s):
                    return(s)
                if s not in fringe:
                    fringe.append(s)
    #condition for bfs
    else:
        while len(fringe) > 0:
            state = fringe.pop(0)
            if is_goal(state):
                return(state)
            for s in successors2(state):
                if s not in fringe:
                    fringe.append(s)

    return False

# This is N, the size of the board. It is passed through command line arguments.
N = int(sys.argv[2])
is_type  = sys.argv[1]
x_r = int(sys.argv[3])
x_c = int(sys.argv[4])

#global variable to choose between dfs and bfs
dfs = 1

#check for unavailable box 
is_unavailable = 1
# The board is stored as a list-of-lists. Each inner list is a row of the board.
# A zero in a given square indicates no piece, and a 1 indicates a piece.
#initial_board = [[0]*N]*N
initial_board = [[0]*N for _ in range(N)]

#conditions for unavailable boxes
if(x_r < 0 or x_r > N or x_c < 0 or x_c > N):
    print "\nInvalid values for unavailable position.\n The values should > 0 and <= N\n.Continuing without the co-ordinates given. Treating this as a (0,0) case.\n"
    is_unavailable = 0
elif(x_r == 0 or x_c == 0):
    print "\nEither unavailable row or col as input is zero. Treating this as a (0,0) case"
    is_unavailable = 0
else:
    x_r = x_r - 1
    x_c = x_c - 1


print ("Starting from initial board:\n" + printable_board(initial_board) + "\n\nLooking for solution...\n")
solution = solve(initial_board)
if is_unavailable:
    solution[x_r][x_c] = -1
print (printable_board(solution) if solution else "Sorry, no solution found. :(")

