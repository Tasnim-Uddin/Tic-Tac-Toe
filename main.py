import random
# from math import inf as infinity
from random import choice
import platform
import time
from os import system

PLAYER = 'X'
AI = 'O'


def empty_board():  # create an empty board at start of game
    board = [[' ' for row in range(3)] for column in range(3)]
    return board


def ai_turn(board):  # logic for ai moves
    x = random.randint(0, 2)
    y = random.randint(0, 2)

    while board[x][y] != ' ':
        x = random.randint(0, 2)
        y = random.randint(0, 2)

    if (board[0][0] == 'X' or board[0][2] == 'X' or board[2][0] == 'X' or board[2][2] == 'X') and board[1][1] == ' ':
        x = 1
        y = 1

    board[x][y] = AI

    return board


def player_turn(board):
    print("It is now your turn")
    position = input("Enter the row followed by the column you would like to play: ")
    x = int(position[0])
    y = int(position[1])

    while not (len(position) == 2 and 0 < x < 4 and 0 < y < 4 and board[x-1][y-1] == ' '):
        print("You have entered an invalid move")
        position = input("Enter the row followed by the column you would like to play: ")
        x = int(position[0])
        y = int(position[1])

    board[x - 1][y - 1] = PLAYER

    return board


def display_board(board):
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

    # rows and columns check
    for row in range(0, 3):
        for column in range(0, 3):
            if board[row][column] == 'X' or board[row][column] == 'O':
                if board[row][0] == board[row][1] == board[row][2]:
                    line += 1
                elif board[0][column] == board[1][column] == board[2][column]:
                    line += 1
                break
            break

    # diagonals check
    if board[1][1] == 'X' or board[1][1] == 'O':
        if board[0][0] == board[1][1] == board[2][2]:
            line += 1
        elif board[0][2] == board[1][1] == board[2][0]:
            line += 1

    if line >= 1:
        game_end = True

    return game_end


def main():
    board = empty_board()
    display_board(board)
    starter = input("Would you like to start? ")

    while starter.lower() != 'yes' and starter.lower() != 'no':
        starter = input("Would you like to start? ")

    if starter.lower() == 'yes':
        while not winner(board):
            board = player_turn(board)
            display_board(board)
            if not winner(board):
                board = ai_turn(board)
                display_board(board)

    elif starter.lower() == 'no':
        while not winner(board):
            board = ai_turn(board)
            display_board(board)
            if not winner(board):
                board = player_turn(board)
                display_board(board)


if __name__ == '__main__':
    main()
