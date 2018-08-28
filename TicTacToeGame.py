import os
import random
import time
"""This is a Terminal based Tic Tac Toe game."""


class TicTacToeGame:
    # Create init with number of blank spaces lets use 0 to 9
    #  So 10 spaces ignore one to make it easier to choose a space using a List
    def __init__(self):
        self.grid = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.symbol_X = "X"
        self.symbol_O = "O"

    def print_board(self):
        # Print the empty board for the tic tac toe game
        print("---------")
        print(f"{self.grid[1]} | {self.grid[2]} | {self.grid[3]}")
        print("---------")
        print(f"{self.grid[4]} | {self.grid[5]} | {self.grid[6]}")
        print("---------")
        print(f"{self.grid[7]} | {self.grid[8]} | {self.grid[9]}")
        print("---------")

    @staticmethod
    def players():
        # Ask for the names of player 1 and player 2, then ask player 1 if they want to be O or X
        # When player 1 selects x or o random operator will decide first turn
        player_one = input("What is your name Player One >>> ")
        player_two = input("What is your name Player Two >>> ")
        print(f"Welcome {player_one} and {player_two}")


def main():
    # Run all methods through here
    game = TicTacToeGame()
    print("=================Welcome to TIC-TAC-TOE=================")
    game.players()
    game.print_board()


if __name__ == "__main__":
    main()
