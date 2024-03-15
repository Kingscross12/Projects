from tkinter import *

def on_click(button):
    button.config(text="X", state="disabled")

root = Tk()
root.title("Tic Tac Toe")

# Create buttons for the Tic Tac Toe grid
buttons = [[None]*3 for _ in range(3)]  # Empty list to store buttons

for row in range(3):
    for col in range(3):
        button = Button(root, width=10, height=5, command=lambda button=button: on_click(button))
        button.grid(row=row, column=col)
        button.text = StringVar()
        button.config(textvariable=button.text)
        buttons[row][col] = button  # Store the button in the list

root.mainloop()
