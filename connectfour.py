import numpy as np
import math
import pygame
import sys
ROW_COUNT = 6
COLUMN_COUNT = 7
EVEN = 0
ODD = 1

def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT)) #makes a matrix of all zeroes, 6 rows by 7 columns (using numpy)
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[ROW_COUNT-1][col]== 0 #checks the top row (row 5) that each column equals 0 so that it's a valid location to fill

def get_next_open_row():
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def print_board(board): #changes orientation so what we see is bott left is origin instead of top left
    print(np.flip(board, 0))

def winning_move(board, piece):
    # Check horizontal locations for win
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3]==piece:
                return True


board = create_board() #initialize board
print_board(board)
game_over = False
turn = 0

while not game_over:
    # Ask for Player 1 Input
    if turn == 0:
        col = int(input("Player 1 Make your Selection(0-6): "))

        if is_valid_location(board, col):
            row = get_next_open_row()
            drop_piece(board, row, col, 1)

    # Ask for Player 2 Input
    else :
        col = int(input("Player 2 Make your Selection(0-6): "))

        if is_valid_location(board, col):
            drop_piece(board, row, col, 2)
            row = get_next_open_row()

            if winning_move(board, 1):
                print("PLAYER 1 WINS!!!! CONGRATS!!!!!")
                game_over = True3

    print_board(board)
    turn +=1
    turn = turn%2