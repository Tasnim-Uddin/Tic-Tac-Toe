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

    board[x - 1][y - 1] = PLAYER

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
    game_end = False
    line = 0

    for row in range(0, 3):
        for column in range(0, 3):
            if board[row][column] == 'X' or board[row][column] == 'O':
                if board[row][0] == board[row][1] == board[row][2]:
                    line += 1
                elif board[0][column] == board[1][column] == board[2][column]:
                    line += 1
                break
            break

    if board[0][0] == 'X' or board[0][0] == 'O':
        if board[0][0] == board[1][1] == board[2][2]:
            line += 1
        elif board[0][2] == board[1][1] == board[2][0]:
            line += 1

    if line >= 1:
        game_end = True

    return game_end


# this should put together all the functions we've done so far so that you can play against a computer which plays randomly
# ai and human take turns to make moves
def main():
    board = empty_cells()
    draw_board(board)
    starter = input("Would you like to start? ")

    while starter.lower() != 'yes' and starter.lower() != 'no':
        starter = input("Would you like to start? ")

    if starter.lower() == 'yes':
        while not winner(board):
            board = player_turn(board)
            draw_board(board)
            board = ai_turn(board)
            draw_board(board)

    elif starter.lower() == 'no':
        while not winner(board):
            board = ai_turn(board)
            draw_board(board)
            board = player_turn(board)
            draw_board(board)


main()
