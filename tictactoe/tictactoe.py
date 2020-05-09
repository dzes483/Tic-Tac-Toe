#!/usr/bin/python3
# TicTacToe.py - A basic Tic-Tac-Toe game.

import random

board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']

# Function to display the Tic-Tac-Toe board
def display_board(board):
    print(board[1]+' ┃'+board[2]+' ┃'+board[3])
    print(''+ '━━''╋'+'━━'+'╋'+ '━━')
    print(board[4]+' ┃'+board[5]+' ┃'+board[6])
    print(''+ '━━''╋'+'━━'+'╋'+ '━━')
    print(board[7]+' ┃'+board[8]+' ┃'+board[9], end='\n\n\n\n\n')


# Function to take in the player's choice of position
def player_choice():
    while True:
        # Make sure the number is not less than one nor more than ten
        position = int(input('Choose your next position: (1-9) '))
        if position not in range(1,10):
            print('Not a valid number. Please enter a number 1-9')
            continue
        # Ensure that the player's choice of space is empty
        elif board[position] != ' ':
            print('Not an empty space. Please enter a different number.')
            continue
        else:
            return position


# Function to allow players to choose their sign ('X' or 'O')
def choose_marker():
    # Make the player's signs global for ease of use
    global player1_sign
    global player2_sign
    marker = ''
    while marker.upper() != 'X' and marker.upper() != 'O':
        marker = input('Player 1, choose X or O: ')

    player1_sign = marker.upper()

    if marker.upper() == 'X':
        player2_sign = 'O'
    elif marker.upper() == 'O':
        player2_sign = 'X'


# Function to decide randomly who goes first
def who_goes_first():
    x = random.randint(0,1)

    if x == 0:
        print('Player 1, you go first!')
        return('P1')
    else:
        print('Player 2, you go first!')
        return('P2')


# Function to check for wins
def win_check(board,character):

    # Across the top
    return((board[1] == character and board[2] == character and board[3] == character)
    # Across the middle
    or (board[4] == character and board[5] == character and board[6] == character)
    # Across the bottom
    or (board[7] == character and board[8] == character and board[9] == character)
    # Diagonally from top left to bottom
    or (board[1] == character and board[5] == character and board[9] == character)
    # Diagonally from top right to bottom
    or (board[3] == character and board[5] == character and board[7] == character)
    # Down the left
    or (board[1] == character and board[4] == character and board[7] == character)
    # Down the middle
    or (board[2] == character and board[5] == character and board[8] == character)
    # Down the right
    or (board[3] == character and board[6] == character and board[9] == character))


# Function to check if the board is full
def full_board():

    for p in board:
        if ' ' not in board:
            return True
        else:
            return False


# Function to check if the user wishes to replay the game
def replay():
    return input('Do you want to play again?').lower().startswith('y')


print('Welcome to Tic-Tac-Toe!')
while True:
    # Reset the board
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    choose_marker()
    turn = who_goes_first()
    lets_play = input('Are you ready to play? Type Yes or No: ')
    if lets_play.lower()[0] == 'y':
        game = True
    else:
        game = False

    while game:
        if turn == 'P1':
            display_board(board)
            position = player_choice()
            board[position] = player1_sign
            display_board(board)

            if win_check(board, player1_sign):
                display_board(board)
                print("Congratulations, you've won the game!")
                game = False
            else:
                if full_board():
                    display_board(board)
                    print("It's a draw!")
                    break
                else:
                    turn = 'P2'
        else:
            display_board(board)
            position = player_choice()
            board[position] = player2_sign
            display_board(board)
            if win_check(board, player2_sign):
                display_board(board)
                print("Congratulations, you've won the game!")
                game = False
            else:
                if full_board():
                    display_board(board)
                    print("It's a draw!")
                    break
                else:
                    turn = 'P1'

    if not replay():
        break
