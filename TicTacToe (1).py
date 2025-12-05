import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic Tac Toe ")

# Get screen resolution
screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()

# Use the smaller dimension so the board stays square
canvas_size = min(screen_w, screen_h)

cell_size = canvas_size // 3

root.geometry(f"{screen_w}x{screen_h}")

canvas = tk.Canvas(root, width=canvas_size, height=canvas_size, bg="white")
canvas.pack()

board = [""] * 9
current_player = "X"
game_over = False

# Draw board lines
def draw_board():
    canvas.create_line(cell_size, 0, cell_size, canvas_size, width=8)
    canvas.create_line(cell_size * 2, 0, cell_size * 2, canvas_size, width=8)
    canvas.create_line(0, cell_size, canvas_size, cell_size, width=8)
    canvas.create_line(0, cell_size * 2, canvas_size, cell_size * 2, width=8)

# Draw X
def draw_x(row, col):
    padding = cell_size * 0.3
    x1 = col * cell_size + padding
    y1 = row * cell_size + padding
    x2 = (col + 1) * cell_size - padding
    y2 = (row + 1) * cell_size - padding
    canvas.create_line(x1, y1, x2, y2, width=10, fill="red")
    canvas.create_line(x1, y2, x2, y1, width=10, fill="red")

# Draw O
def draw_o(row, col):
    x = col * cell_size + cell_size / 2
    y = row * cell_size + cell_size / 2
    r = cell_size * 0.2
    canvas.create_oval(x-r, y-r, x+r, y+r, width=10, outline="blue")

# Draw win line
def draw_win_line(a, c):
    ax = (a % 3) * cell_size + cell_size/2
    ay = (a // 3) * cell_size + cell_size/2
    cx = (c % 3) * cell_size + cell_size/2
    cy = (c // 3) * cell_size + cell_size/2
    canvas.create_line(ax, ay, cx, cy, width=10, fill="green")

# Check win
def check_win(player):
    wins = [
        (0,1,2), (3,4,5), (6,7,8), 
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for a, b, c in wins:
        if board[a] == board[b] == board[c] == player:
            draw_win_line(a, c)
            return True
    return False

# Handle click
def click(event):
    global current_player, game_over

    if game_over:
        return

    col = event.x // cell_size
    row = event.y // cell_size

    if col >= 3 or row >= 3:
        return

    idx = row * 3 + col

    if board[idx] != "":
        return

    board[idx] = current_player

    if current_player == "X":
        draw_x(row, col)
    else:
        draw_o(row, col)

    if check_win(current_player):
        game_over = True
        messagebox.showinfo("Game Over", f"{current_player} wins!")
        return

    if "" not in board:
        game_over = True
        messagebox.showinfo("Game Over", "It's a draw!")
        return

    current_player = "O" if current_player == "X" else "X"

# Reset game
def reset_game():
    global board, current_player, game_over
    board = [""] * 9
    current_player = "X"
    game_over = False
    canvas.delete("all")
    draw_board()

reset_btn = tk.Button(root, text="Reset Game", font=("Arial", 20), command=reset_game)
reset_btn.pack(fill="x")

draw_board()
canvas.bind("<Button-1>", click)
root.mainloop()
