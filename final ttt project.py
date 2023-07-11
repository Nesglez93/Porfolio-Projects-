#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("Welcome to Nestor's Tic-Tac-Toe")


def display_board(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


def player_input():
    choice = " "
    while not (choice == "X" or choice == "O"):
        choice = input("Please choose your Symbol X or O ").upper()
   
    if choice != "X" or choice != "O": 
        print ( "Choose a letter this is Tic Tac Toe not something else")
    elif choice == 'X':
        return ('X', 'O')
   
    else:
        return ('O', 'X')
    


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            (board[9] == mark and board[6] == mark and board[3] == mark) or
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[9] == mark and board[5] == mark and board[1] == mark))


import random

def choose_first():
    if random.randint(0, 1) == 0:
        return "Player 2 Goes First"
    else:
        return "Player 1 Goes First"


def space_check(board, position):
    return board[position] == " "


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input("Please choose your next position on the board (1-9): "))
    return position


def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


while True:
    board_list = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')

    play_game = input('Are you ready to play? Enter Yes or No: ')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
        print( " Please enter yes or no, It's not that hard")

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(board_list)
            position = player_choice(board_list)
            place_marker(board_list, player1_marker, position)

            if win_check(board_list, player1_marker):
                display_board(board_list)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(board_list):
                    display_board(board_list)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(board_list)
            position = player_choice(board_list)
            place_marker(board_list, player2_marker, position)

            if win_check(board_list, player2_marker):
                display_board(board_list)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(board_list):
                    display_board(board_list)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break


# In[ ]:





# In[ ]:





# In[ ]:




