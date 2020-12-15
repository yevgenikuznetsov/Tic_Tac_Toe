from TicTacBoard import *
from tkinter import messagebox
import tkinter as tk


class WindowsHandler:
    _number_of_times = 0

    def __init__(self):
        self.moves = []
        self.gameWindow = None

    def close_window(self):
        WindowsHandler._number_of_times -= 1
        self.gameWindow.destroy()

    def openNewWindow(self, game_mode):
        if WindowsHandler._number_of_times >= 1:
            messagebox.showerror("Tic Tac Toe", "You can't open more than one window")
        else:
            self.gameWindow = tk.Tk()
            WindowsHandler._number_of_times += 1

            self.gameWindow.wm_protocol("WM_DELETE_WINDOW", lambda: self.close_window())
            self.gameWindow.title("Tic Tac Toe")

            TicTacBoard(self.gameWindow, game_mode)

            self.gameWindow.mainloop()

