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

    def print_board(self):
        os.system("cls")
        # Method to print board with spaces available
        print(f" {self.empty_board[1]} | {self.empty_board[2]} | {self.empty_board[3]}")
        print("-----------")
        print(f" {self.empty_board[4]} | {self.empty_board[5]} | {self.empty_board[6]}")
        print("-----------")
        print(f" {self.empty_board[7]} | {self.empty_board[8]} | {self.empty_board[9]}")

    def get_player(self):
        player = self.player
        # Ask the players to input their names and choose their mark to play
        name_one = input("Please enter your name Player 1: ")
        name_two = input("Please enter your name Player 2: ")
        os.system("cls")
        while not(player == self.symbol_X or player == self.symbol_O):
            player = input(f"{name_one} do you want to be X or O >>>").upper()
            if player == self.symbol_X:
                # Returns a dict assigns name to the mark for both players
                player_stat = {self.symbol_X: name_one, self.symbol_O: name_two}
                return player_stat
            elif player == self.symbol_O:
                player_stat = {self.symbol_O: name_one, self.symbol_X: name_two}
                return player_stat
            else:
                # not a valid choice, validation for input
                error_messages = ["Sorry Not a valid choice Try Again.", "Please choose X or O", "Stop wasting time"]
                error_choice = random.randint(0, 2)
                print(error_messages[error_choice])

    def place_mark(self, position, player):
        # Place a value on individual cell of board
        self.empty_board[position] = player

    def check_winner(self, player):
        # Check if there is a winner on the board
        return (self.empty_board[1] == self.empty_board[2] == self.empty_board[3] == player or
                self.empty_board[4] == self.empty_board[5] == self.empty_board[6] == player or
                self.empty_board[7] == self.empty_board[8] == self.empty_board[9] == player or
                self.empty_board[1] == self.empty_board[4] == self.empty_board[7] == player or
                self.empty_board[2] == self.empty_board[5] == self.empty_board[8] == player or
                self.empty_board[3] == self.empty_board[6] == self.empty_board[9] == player or
                self.empty_board[1] == self.empty_board[5] == self.empty_board[9] == player or
                self.empty_board[7] == self.empty_board[5] == self.empty_board[3] == player)

    def first_turn(self):
        # Random selected first move
        if random.randint(1, 2) == 1:
            return self.symbol_X
        else:
            return self.symbol_O

    def is_space_valid(self, position):
        # check if the position is available or not
        if self.empty_board[position] == " ":
            return True
        else:
            return False

    def is_board_full(self, is_space_valid):
        # Checks if the board is full
        for pos in range(1, 10):
            if is_space_valid(self.empty_board, pos):
                return False
            else:
                return True

    def player_input(self, player, is_space_valid):
        # inputs position from users and validates if the space is free using is_space_valid()
        player_choice = " "
        while player_choice not in "1 2 3 4 5 6 7 8 9".split() or not is_space_valid(self.empty_board,
                                                                                     int(player_choice)):
            player_choice = input(f"{player} what is your next move? (1-9)")
        return int(player_choice)

    @staticmethod
    def play_again():
        # Ask the player to play again get Y return true otherwise false
        print("Do you want to play again? (y or n)")
        return input(">>> ").lower().startswith("y")


def main():
    # Run all methods through here
    while True:
        os.system("cls")
        game = TicTacToeGame()
        print("=================Welcome to TIC-TAC-TOE=================")
        time.sleep(.4)
        board = [" "]*10
        name = game.get_player()
        turn = game.first_turn()
        print(f"{turn} will go first.")
        time.sleep(.3)
        game_playing = True
        time.sleep(1)
        while game_playing:
            if turn == "X":
                # This is player 1
                game.print_board()
                full_board = game.is_board_full(board)
                # check for wins
                if game.check_winner(board, "O"):
                    print(f"Congrats {name} is the winner")
                    break
                if full_board:
                    print("Evenly matched! Its a Tie!")
                    break
                pos = game.player_input(board, name["X"])
                status_position = game.is_space_valid(board, pos)
                if status_position is True:
                    game.place_mark(pos, board, "X")
                turn = "O"
            else:
                # player 2
                game.print_board()
                board_full = game.is_board_full(board)
                # check for wins
                if game.check_winner(board, "X"):
                    print(f"Congrats {name} is the winner")
                    break
                if board_full:
                    print("Evenly matched! Its a Tie!")
                    break
                pos = game.player_input(board, name["O"])
                status_position = game.is_space_valid(board, pos)
                if status_position is True:
                    game.place_mark(pos, board, "O")
                turn = "X"

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
