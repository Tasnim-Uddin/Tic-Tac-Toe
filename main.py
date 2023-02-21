import random
# from math import inf as infinity
from random import choice
import platform
import time
from os import system

PLAYER = 'X'
AI = 'O'


# This should return the position of all the cells which don't have a move in them
def empty_cells():
    board = [[' ' for column in range(3)] for row in range(3)]
    return board
    # empty = 0
    # for row in range(0, 3):
    #     for column in range(0, 3):
    #         if board[row][column] == '':
    #             empty += 1
    # return empty


# this will just choose a random move for the computer to make
# we will change this function later to make our computer unbeatable
# for now fill the board with the random move
# Hint: careful the random move can't be a space that is already used
def ai_turn(board):
    x = random.randint(0, 2)
    y = random.randint(0, 2)

    while board[x][y] != ' ':
        x = random.randint(0, 2)
        y = random.randint(0, 2)

    board[x][y] = AI

    return board


def player_turn(board):
    print("It is now your turn")
    position = input("Enter the row followed by the column you would like to play: ")
    x = int(position[0])
    y = int(position[1])

    # while (int(position[0]) < 1 or int(position[0]) > 3) or (int(position[1]) < 1 or int(position[1]) > 3) or (len(position) != 2):
    #     position = input("Enter the row followed by the column you would like to play: ")

    while not (len(position) == 2 or 0 < x < 4 or 0 < y < 4 or board[x][y] == ' '):
        position = input("Enter the row followed by the column you would like to play: ")

    board[x-1][y-1] = PLAYER

    return board


def draw_board(board):
    print()
    print("   1   2   3   ")
    print(" |===|===|===|")
    for Row in range(0, 3):
        print(f"{Row + 1}|", end='')
        for Column in range(0, 3):
            if (Column + 1) % 3 == 0:
                print(f"{' '}{board[Row][Column]}{' '}|", end='')
            else:
                print(f"{' '}{board[Row][Column]}{' '}|", end='')
        print()
        if (Row + 1) % 3 == 0:
            print(" |===|===|===|")
        else:
            print(" |___|___|___|")
    print()


def winner(board):
    pass

# this should put together all the functions we've done so far so that you can play against a computer which plays randomly
# ai and human take turns to make moves
def main():
    board = empty_cells()
    draw_board(board)
    while True:
        board = ai_turn(board)
        draw_board(board)
        board = player_turn(board)
        draw_board(board)



main()