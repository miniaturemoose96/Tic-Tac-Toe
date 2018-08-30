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

    def draw_board(self):
        # Print the empty board for the tic tac toe game
        print("---------")
        print(f"{self.grid[1]} | {self.grid[2]} | {self.grid[3]}")
        print("---------")
        print(f"{self.grid[4]} | {self.grid[5]} | {self.grid[6]}")
        print("---------")
        print(f"{self.grid[7]} | {self.grid[8]} | {self.grid[9]}")
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
                return player_xo
            elif player == self.symbol_O:
                player_xo = {self.symbol_O: player_one, self.symbol_X: player_two}
                return player_xo
            else:
                print("Error please choose X or O...")

    def place_mark(self, position, player):
        # places the players mark on the board
        self.grid[position] = player

    def check_for_winner(self, player):
        # Check for winning player, we want to check rows, columns and Diagonals
        # Winning combos: [1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]
        return (self.grid[1] and self.grid[2] and self.grid[3] == player or
                self.grid[4] and self.grid[5] and self.grid[6] == player or
                self.grid[7] and self.grid[8] and self.grid[9] == player or
                self.grid[1] and self.grid[4] and self.grid[7] == player or
                self.grid[2] and self.grid[5] and self.grid[8] == player or
                self.grid[3] and self.grid[6] and self.grid[9] == player or
                self.grid[1] and self.grid[5] and self.grid[9] == player or
                self.grid[3] and self.grid[5] and self.grid[7] == player)

    def who_goes_first(self, player_xo):
        # This is the random operator that chooses the player that goes first using random
        print("Eeny, meeny, miny, moe")
        time.sleep(1)
        print("The person that will go first is......")
        time.sleep(1)
        if random.randint(1, 2) == 1:
            print(f"{player_xo} makes the first move.")
            return self.symbol_X
        else:
            print(f"{player_xo} makes the first move.")
            return self.symbol_O

    def is_space_valid(self, position):
        # Checks if the current space selected is available(true) or unavailable(false)
        if self.grid[position] == " ":
            return True
        else:
            return False

    @staticmethod
    def is_board_full(is_space_valid):
        # checks if the players can still make moves to the board
        for element in range(1, 10):
            if is_space_valid(element):
                return False
        else:
            return True

    @staticmethod
    def player_move(player, is_space_valid):
        # inputs position from users and validates if the space is free using is_space_valid()
        player_choice = " "
        while player_choice not in "1 2 3 4 5 6 7 8 9".split() or not is_space_valid(int(player_choice)):
            player_choice = input(f"{player} what is your next move? (1-9)")
        return int(player_choice)

    @staticmethod
    def play_again():
        # Ask the player to play again get Y return true otherwise false
        print("Do you want to play again? (y or n)")
        return input(">>> ").lower().startswith("y")


def main():
    # Run all methods through here
    game = TicTacToeGame()
    os.system("cls")
    print("=================Welcome to TIC-TAC-TOE=================")
    time.sleep(.4)
    player, player_xo = game.players()
    player_turn = game.who_goes_first(player_xo)
    print(f"{player} will go first")
    time.sleep(.4)
    game_is_playing = True
    while game_is_playing:
        if player_turn == "X":
            # Player 1
            game.draw_board()
            # This is to see if the player can make any moves or not.
            status_of_board = game.is_board_full(game.is_space_valid)
            if game.check_for_winner(player):
                print(f"Congrats {player} is the winner")
                break
            if status_of_board:
                print("Its a Draw!")
                break
            position = game.player_move(player, game.is_space_valid)
            status_position = game.is_space_valid(position)
            if status_position is True:
                game.place_mark(position, player)
            player_turn = "O"
        else:
            # Player 2
            game.draw_board()
            # This is to see if the player can make any moves or not.
            status_of_board = game.is_board_full(game.is_space_valid)
            if game.check_for_winner(player):
                print(f"Congrats {player} is the winner")
                break
            if status_of_board:
                print("Its a Draw!")
                break
            position = game.player_move(player, game.is_space_valid)
            status_position = game.is_space_valid(position)
            if status_position is True:
                game.place_mark(position, player)
            player_turn = "X"

        if game.play_again():
            # Else want to play again?
            continue
        else:
            # Thank you for playing close th game
            print("Thank you for playing!")
            time.sleep(.4)
            print("Bye!")
            os.system("cls")
            break


if __name__ == "__main__":
    main()
