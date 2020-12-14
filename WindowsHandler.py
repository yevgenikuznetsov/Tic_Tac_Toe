from Singelton import *
from tkinter import *
from TicTacBoard import *
from tkinter import messagebox

import tkinter as tk


class WindowsHandler:
    def __init__(self):
        self.moves = []
        self.government = None
        self.gameWindow = None

    def openNewWindow(self, game_mode):
        self.government = Singleton()

        if not self.government.openNewWindow:

            self.gameWindow = tk.Tk()

            self.gameWindow.title("Tic Tac Toe")
            TicTacBoard(self.gameWindow, game_mode)

            self.gameWindow.mainloop()
