import os
os.system("cls")


class Board:
    def __init__(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def display(self):
        """

        :rtype: None
        """
        print(" %s | %s | %s " %(self.cells[1], self.cells[2], self.cells[3]))
        print("----------")
        print(" %s | %s | %s " %(self.cells[4], self.cells[5], self.cells[6]))
        print("----------")
        print(" %s | %s | %s " %(self.cells[7], self.cells[8], self.cells[9]))

    # Update the cell selected by player
    def update_cell(self, cell_number: int, character: str) -> None:
        self.cells[cell_number] = character

    # Check if the player has a matching combination
    def is_winner(self, player):
        if self.cells[1] == player and self.cells[2] == player and self.cells[3] == player:
            return True

        if self.cells[4] == player and self.cells[5] == player and self.cells[6] == player:
            return True

        if self.cells[7] == player and self.cells[8] == player and self.cells[9] == player:
            return True

        if self.cells[1] == player and self.cells[5] == player and self.cells[9] == player:
            return True

        if self.cells[3] == player and self.cells[5] == player and self.cells[7] == player:
            return True

        if self.cells[1] == player and self.cells[4] == player and self.cells[7] == player:
            return True

        if self.cells[2] == player and self.cells[5] == player and self.cells[8] == player:
            return True

        if self.cells[3] == player and self.cells[5] == player and self.cells[9] == player:
            return True

    def reset(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def is_tie(self):
        used_cells = 0
        for cells in self.cells:
            if cells != " ":
                used_cells += 1

        if used_cells == 9:
            return True
        else:
            return False

    def is_used(self,cell):
        if self.cells[cell] != " ":
            return True
        else:
            return False




def print_header():
    print("Welcome to tic tac toe \n")


def refresh_screen():
    os.system("cls")

    print_header()

    board.display()


board = Board()
refresh_screen()

while True:

    # Get X input
    while True:
        x_choice: int = int(input("X :Enter a number 1 to 9:  \n"))
        if board.is_used(x_choice):
            print("Cell already used, please use a different number:  \n")
        else:
            break

    # Show X on screen
    board.update_cell(x_choice, "X")

    refresh_screen()

    # Check for a win
    if board.is_winner("X"):
        print("X Wins")
        play = input("Do you want to continue playing: \n ")
        if play.lower() == "y":
            board.reset()
            continue
        else:
            break

    # Check for a tie
    if board.is_tie():
        print("It's a tie")
        play = input("Do you want to continue playing:  \n")
        if play.lower() == "y":
            board.reset()
            continue
        else:
            break

    # Show Y on screen


    while True:
        y_choice: int = int(input("O :Enter a number 1 to 9: \n"))

        if board.is_used(y_choice):
            print("Cell already used, please use a different number")
        else:
            break

    board.update_cell(y_choice, "O")

    refresh_screen()
    if board.is_winner("O"):
        print("O Wins")
        play = input("Do you want to continue playing: ")
        if play.lower() == "y":
            board.reset()
            continue
        else:
            break

    # Check for a tie
    if board.is_tie():
        print("It's a tie")
        play = input("Do you want to continue playing: ")
        if play.lower() == "y":
            board.reset()
            continue
        else:
            break

