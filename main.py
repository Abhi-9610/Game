import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.board = [""] * 9
        self.current_player = "X"
        self.buttons = []
        self.create_board()

    def create_board(self):
        for i in range(9):
            button = tk.Button(self.root, text="", font='Arial 20 bold', width=5, height=2, command=lambda i=i: self.on_button_click(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

    def on_button_click(self, index):
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            winning_combination = self.check_winner()
            if winning_combination:
                self.highlight_winner(winning_combination)
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_board()
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "":
                return combo
        return None

    def highlight_winner(self, combo):
        for index in combo:
            self.buttons[index].config(bg="green")

    def reset_board(self):
        self.board = [""] * 9
        self.current_player = "X"
        for button in self.buttons:
            button.config(text="", bg=self.root.cget('bg'))

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
