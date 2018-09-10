import os
import random
import time
"""This is a Terminal based Tic Tac Toe game. Using Classes."""
"""Using an Object Oriented approach."""


class Board:
    def __init__(self):
        self.grid = [" "]*10

    def display_board(self):
        # Print the empty board for the tic tac toe game
        print("---------".center(40))
        print(f"{self.grid[1]} | {self.grid[2]} | {self.grid[3]}".center(40))
        print("---------".center(40))
        print(f"{self.grid[4]} | {self.grid[5]} | {self.grid[6]}".center(40))
        print("---------".center(40))
        print(f"{self.grid[7]} | {self.grid[8]} | {self.grid[9]}".center(40))
        print("---------".center(40))


class Player:
    def __init__(self):
        self.player_symbol = " "
        self.symbol_X = "X"
        self.symbol_O = "O"

    def players(self):
        player = self.player_symbol
        player_one = input("What is your name Player 1: ")
        player_two = input("What is your name Player 2: ")
        print(f"Welcome {player_one} and {player_two}")
        os.system("cls")
        while player != self.symbol_X or player != self.symbol_O:
            player = input(f"{player_one} do you want to be X or O?:  ").upper()
            if player == self.symbol_X:
                players = {player_one: self.symbol_X, player_two: self.symbol_O}
                for x in players.keys():
                    print(f">>>{x} is {players[x]}")
                return players
            elif player == self.symbol_O:
                players = {player_one: self.symbol_O, player_two: self.symbol_X}
                for x in players.keys():
                    print(f">>>{x} is {players[x]}")
                return players
            else:
                print("Not a valid choice, Please choose X or O.")

    @staticmethod
    def who_goes_first(player_one, player_two):
        # This is the random operator that chooses the player that goes first using random
        print("Eeny, meeny, miny, moe")
        time.sleep(1)
        print("The person that will go first is...")
        time.sleep(1)
        if random.randint(1, 2) == 1:
            print(f"{player_one} makes the first move.")
        else:
            print(f"{player_two} makes the first move.")


def main():
    board = Board()
    os.system("cls")
    print("----------Welcome to Tic-Tac-Toe----------")
    board.display_board()
    player = Player()
    player_one, player_two = player.players()
    player.who_goes_first(player_one, player_two)


if __name__ == "__main__":
    main()
