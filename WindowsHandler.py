from TicTacBoard import *
from tkinter import messagebox
import tkinter as tk


#####################################################################################################################
# Singleton Realization:                                                                                            #
# Once the player has selected the type of game he wants to play it will not be possible to open a new game window. #
# Only after the player close the game window it will be possible to select another game type or the same type game.#
#####################################################################################################################
class WindowsHandler:
    # The number of instances of the object at a given moment
    _number_of_times = 0

    def __init__(self):
        self.moves = []
        self.gameWindow = None

    # close currently window
    def close_window(self):
        #_number_of_times Decreases by 1
        WindowsHandler._number_of_times -= 1
        self.gameWindow.destroy()

    def openNewWindow(self, game_mode):
        # Check if there is already an instance of the object - If so you can not create another one
        if WindowsHandler._number_of_times >= 1:
            messagebox.showerror("Tic Tac Toe", "You can't open more than one window")
        # If no new instance of the object is created and _number_of_times Increases by 1
        else:
            self.gameWindow = tk.Tk()
            WindowsHandler._number_of_times += 1

            self.gameWindow.wm_protocol("WM_DELETE_WINDOW", lambda: self.close_window())
            self.gameWindow.title("Tic Tac Toe")

            TicTacBoard(self.gameWindow, game_mode)

            self.gameWindow.mainloop()

