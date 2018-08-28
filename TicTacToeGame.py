import os
import random
import time
"""This is a Terminal based Tic Tac Toe game."""


class TicTacToeGame:
    # Create init with number of blank spaces lets use 0 to 9
    #  So 10 spaces ignore one to make it easier to choose a space using a List
    def __init__(self):
        self.symbol_X = "X"
        self.symbol_O = "O"

    @staticmethod
    def draw_board(board):
        # Print the empty board for the tic tac toe game
        print("---------")
        print(f"{board[1]} | {board[2]} | {board[3]}")
        print("---------")
        print(f"{board[4]} | {board[5]} | {board[6]}")
        print("---------")
        print(f"{board[7]} | {board[8]} | {board[9]}")
        print("---------")

    def players(self):
        # Ask for the names of player 1 and player 2, then ask player 1 if they want to be O or X
        # When player 1 selects x or o random operator will decide first turn
        player = " "
        player_one = input("What is your name Player One >>> ")
        player_two = input("What is your name Player Two >>> ")
        print(f"Welcome {player_one} and {player_two}")
        os.system("cls")
        while player != self.symbol_X or player != self.symbol_O:
            player = input(f"{player_one} who do you want to be X or O? ").upper()
            if player == self.symbol_X:
                # Create a dictionary to represent the players x and o
                player_xo = {self.symbol_X: player_one, self.symbol_O: player_two}
                # Print who is X or O, Return the player dict for the next method
                print(f"Player X: {player_xo[self.symbol_X]}, Player O: {player_xo[self.symbol_O]}")
                return player_xo
            elif player == self.symbol_O:
                player_xo = {self.symbol_O: player_one, self.symbol_X: player_two}
                print(f"Player X: {player_xo[self.symbol_X]}, Player O: {player_xo[self.symbol_O]}")
                return player_xo
            else:
                print("Error please choose X or O...")

    def who_goes_first(self, player_xo):
        # This is the random operator that chooses the player that goes first using random
        print("Eeny, meeny, miny, moe")
        time.sleep(1)
        print("The person that will go first is......")
        time.sleep(1)
        if random.randint(1, 2) == 1:
            print(f"{player_xo[self.symbol_X]} makes the first move.")
            return self.symbol_X
        else:
            print(f"{player_xo[self.symbol_O]} makes the first move.")
            return self.symbol_O


"""
    def place_mark(self, player):
        # places the players mark on the board
    def check_for_winner(self):
        # Check for winning player, we want to check rows, columns and Diagonals
        # Winning combos: [1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]
"""


def main():
    # Run all methods through here
    game = TicTacToeGame()
    print("=================Welcome to TIC-TAC-TOE=================")
    player_xo = game.players()
    board = [" "]*10
    game.who_goes_first(player_xo)
    game.draw_board(board)


if __name__ == "__main__":
    main()
