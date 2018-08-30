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
                print(player_xo)
                return player_xo
            elif player == self.symbol_O:
                player_xo = {self.symbol_O: player_one, self.symbol_X: player_two}
                print(player_xo)
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
            print(f"{player_xo} makes the first move.")
            return self.symbol_X
        else:
            print(f"{player_xo} makes the first move.")
            return self.symbol_O

    @staticmethod
    def place_mark(board, position, player):
        # places the players mark on the board
        board[position] = player

    @staticmethod
    def is_space_valid(board, position):
        # Checks if the current space selected is available(true) or unavailable(false)
        if board[position] == " ":
            return True
        else:
            return False

    @staticmethod
    def is_board_full(board, is_space_valid):
        # checks if the players can still make moves to the board
        for pos in range(1, 10):
            if is_space_valid(board, pos):
                return False
        else:
            return True

    @staticmethod
    def check_for_winner(board, player):
        # Check for winning player, we want to check rows, columns and Diagonals
        # Winning combos: [1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]
        return(board[1] == board[2] == board[3] == player or
               board[4] == board[5] == board[6] == player or
               board[7] == board[8] == board[9] == player or
               board[1] == board[4] == board[7] == player or
               board[2] == board[5] == board[8] == player or
               board[3] == board[6] == board[9] == player or
               board[1] == board[5] == board[9] == player or
               board[7] == board[5] == board[3] == player)

    @staticmethod
    def player_input(board, player, is_space_valid):
        # inputs position from users and validates if the space is free using is_space_valid()
        player_choice = " "
        while player_choice not in "1 2 3 4 5 6 7 8 9".split() or not is_space_valid(board, int(player_choice)):
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
    board = [" "] * 10
    name, player_xo = game.players()
    turn = game.who_goes_first(player_xo)
    print(turn)
    game_playing = True
    while game_playing:
        if turn == "X":
            # This is player X
            game.draw_board(board)
            check_board = game.is_board_full(board, game.is_space_valid)
            if game.check_for_winner(board, "O"):
                print(f"Congrats to {name} you have won!")
                break
            if check_board:
                print("Evenly Matched, It's a Draw!")
                break
            position = game.player_input(board, name, game.is_space_valid)
            new_position = game.is_space_valid(board, position)
            if new_position is True:
                game.place_mark(board, position, "X")
        else:
            # This is player O
            game.draw_board(board)
            check_board = game.is_board_full(board, game.is_space_valid)
            if game.check_for_winner(board, "X"):
                print(f"Congrats to {name} you have won!")
                break
            if check_board:
                print("Evenly Matched, It's a Draw!")
                break
            position = game.player_input(board, name, game.is_space_valid)
            new_position = game.is_space_valid(board, position)
            if new_position is True:
                game.place_mark(board, position, "O")

        if game.play_again():
            # Else want to play again?
            continue
        else:
            # Thank you for playing close th game
            print("Thank you for playing!")
            time.sleep(.4)
            os.system("cls")
        break


if __name__ == "__main__":
    main()
