# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-05-08

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 83 - Tic-Tac-Toe Game

# Using what you have learnt about Python programming, you will build a text-based version of the Tic Tac Toe game.
# The game should be playable in the command line just like the Blackjack game we created on Day 11.
# It should be a 2-player game, where one person is "X" and the other plays "O".

# This is a simple demonstration of how the game works:
# https://www.google.com/search?q=tic+tac+toe

ORDER = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

# Starting positions (all empty)
position = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

# Print current position of the board
def print_board(input_position):
    print("Current board:")
    separator = "_______"
    row1 = "|" + input_position[0] + "|" + input_position[1] + "|" + input_position[2] + "|"
    row2 = "|" + input_position[3] + "|" + input_position[4] + "|" + input_position[5] + "|"
    row3 = "|" + input_position[7] + "|" + input_position[7] + "|" + input_position[8] + "|"
    board = [row1, separator, row2, separator, row3, "\n"]
    for i in board:
        print(i)


# List available choices 1-9
def choose_position(input_position, input_player):
    choices = input_position
    for i in range(len(choices)):
        if choices[i] == " ":
            choices[i] = ORDER[i]

    new_position = input(player + ", choose a position:")
    separator = "_______"
    row1 = "|" + choices[0] + "|" + choices[1] + "|" + choices[2] + "|"
    row2 = "|" + choices[3] + "|" + choices[4] + "|" + choices[5] + "|"
    row3 = "|" + choices[7] + "|" + choices[7] + "|" + choices[8] + "|"
    board = [row1, separator, row2, separator, row3, "\n"]
    for i in board:
        print(i)

    output_position =



print_board(position)
player = "X"
choose_position(position, player)
