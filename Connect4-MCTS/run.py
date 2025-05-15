import tkinter as tk
from tkinter import messagebox
from connect4 import Connect4
from mcts import ucb2_agent
import time
import threading

class Connect4GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Connect 4")
        self.game = Connect4()
        self.pos = self.game.get_initial_position()
        self.board = [[0 for _ in range(7)] for _ in range(6)]
        self.strategy = ucb2_agent(7)
        self.first_player = None  # True if computer goes first, False if player goes first
        self.lock = threading.Lock()

        # Ask who goes first
        self.ask_first_player()

        # Create the game grid
        self.canvas = tk.Canvas(root, width=700, height=600, bg="blue")
        self.canvas.pack(pady=20)
        self.draw_grid()

        # Bind click event to canvas
        self.canvas.bind("<Button-1>", self.on_click)

        # Start computer's turn if it goes first
        if self.first_player:
            self.print_board()  # In trạng thái bảng ban đầu
            self.root.after(500, self.computer_turn)

    def ask_first_player(self):
        response = messagebox.askyesno("Turn Order", "Do you want to go first?")
        self.first_player = not response
        print(f"{'Computer' if self.first_player else 'Player'} goes first.")

    def print_board(self):
        """In trạng thái hiện tại của bảng ra terminal"""
        print("\nCurrent Board State:")
        for row in self.board:
            print(" ".join(['.' if cell == 0 else 'X' if cell == 1 else 'O' for cell in row]))
        print("0 1 2 3 4 5 6")  # Cột số
        print(f"Current turn: {'Computer' if (self.first_player and self.pos.turn == 0) or (not self.first_player and self.pos.turn == 1) else 'Player'}")

    def draw_grid(self):
        self.canvas.delete("all")
        cell_width = 100
        cell_height = 100
        for i in range(6):
            for j in range(7):
                x1 = j * cell_width
                y1 = i * cell_height
                x2 = x1 + cell_width
                y2 = y1 + cell_height
                self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="black")
                if self.board[i][j] == 1:  # Computer
                    self.canvas.create_oval(x1 + 10, y1 + 10, x2 - 10, y2 - 10, fill="red")
                elif self.board[i][j] == 2:  # Player
                    self.canvas.create_oval(x1 + 10, y1 + 10, x2 - 10, y2 - 10, fill="yellow")

    def board_move(self, col, turn):
        for i in range(5, -1, -1):
            if self.board[i][col] == 0:
                self.board[i][col] = 1 if turn == 0 else 2
                return i
        return None

    def check_game_over(self):
        if self.pos.terminal:
            self.print_board()
            if self.pos.winner == 0:
                messagebox.showinfo("Game Over", "Computer wins!")
                print("Game Over: Computer wins!")
            elif self.pos.winner == 1:
                messagebox.showinfo("Game Over", "You win!")
                print("Game Over: Player wins!")
            else:
                messagebox.showinfo("Game Over", "It's a draw!")
                print("Game Over: Draw!")
            self.root.quit()
            return True
        return False

    def computer_turn(self):
        if self.pos.terminal:
            return
        if (self.first_player and self.pos.turn == 0) or (not self.first_player and self.pos.turn == 1):
            with self.lock:
                print("\nComputer is thinking...")
                move = self.strategy(self.pos)
                row = self.board_move(move, self.pos.turn)
                if row is not None:
                    print(f"Computer moves to column {move}")
                    self.pos = self.pos.move(move)
                    self.draw_grid()
                    self.print_board()  # In trạng thái bảng sau nước đi của bot
                    if self.check_game_over():
                        return
            self.root.after(500, self.player_turn)
        else:
            self.root.after(100, self.computer_turn)

    def player_turn(self):
        if self.pos.terminal:
            return
        if (self.first_player and self.pos.turn == 1) or (not self.first_player and self.pos.turn == 0):
            return
        self.root.after(100, self.player_turn)

    def on_click(self, event):
        if self.pos.terminal:
            return
        if (self.first_player and self.pos.turn == 1) or (not self.first_player and self.pos.turn == 0):
            col = event.x // 100
            if 0 <= col < 7 and self.board[0][col] == 0:
                with self.lock:
                    row = self.board_move(col, self.pos.turn)
                    if row is not None:
                        print(f"\nPlayer moves to column {col}")
                        self.pos = self.pos.move(col)
                        self.draw_grid()
                        self.print_board()  # In trạng thái bảng sau nước đi của người chơi
                        if self.check_game_over():
                            return
                self.root.after(500, self.computer_turn)

def main():
    root = tk.Tk()
    app = Connect4GUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()