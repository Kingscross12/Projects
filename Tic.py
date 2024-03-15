import tkinter as tk
from tkinter import messagebox

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def button_click(row, col):
    global current_player, buttons, board
    if board[row][col] == " ":
        buttons[row][col].config(text=current_player)
        board[row][col] = current_player
        if check_winner(board, current_player):
            messagebox.showinfo("Winner", f"Player {current_player} wins!")
            reset_board()
        elif all(" " not in row for row in board):
            messagebox.showinfo("Draw", "It's a draw!")
            reset_board()
        else:
            current_player = "O" if current_player == "X" else "X"
            label.config(text=f"Player {current_player}'s turn")

def reset_board():
    global buttons, board, current_player
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text=" ")
            board[row][col] = " "
    current_player = "X"
    label.config(text="Player X's turn")

# Initialize the game variables
current_player = "X"
board = [[" " for i in range(3)] for i in range(3)]

# Create the main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Create buttons for the Tic Tac Toe grid
buttons = [[None]*3 for i in range(3)]
for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(root, width=10, height=5, command=lambda row=row, col=col: button_click(row, col))
        buttons[row][col].grid(row=row, column=col)

# Create label for displaying current player
label = tk.Label(root, text=f"Player {current_player}'s turn", font=("Helvetica", 12))
label.grid(row=3, columnspan=3)

# Start the game
root.mainloop()
