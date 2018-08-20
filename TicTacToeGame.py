import os
import random
import time
"""This is a Terminal based Tic Tac Toe game."""


class TicTacToeGame:
    # Create init with number of blank spaces lets use 0 to 9
    #  So 10 spaces ignore one to make it easier to choose a space using a List
    def __init__(self):
        self.empty_board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.symbol_X = "X"
        self.symbol_O = "O"
        self.player = " "