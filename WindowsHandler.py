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
        """ 
        The constructor for WindowsHandler class.     
        """
        self.moves = []
        self.gameWindow = None

    def close_window(self):
        WindowsHandler._number_of_times -= 1
        self.gameWindow.destroy()

    def openNewWindow(self, game_mode):
        """ 
        The function create new tic-tac-toe game board depending on the mode of the game 
        (Player vs Player OR Player vs Computer) 
  
        Parameters: 
         game_mode (int): Player vs Player mode OR Player vs Computer mode    
        """
        if WindowsHandler._number_of_times >= 1:
            messagebox.showerror("Tic Tac Toe", "You can't open more than one window")
        else:
            self.gameWindow = tk.Tk()
            WindowsHandler._number_of_times += 1

            self.gameWindow.wm_protocol("WM_DELETE_WINDOW", lambda: self.close_window())
            self.gameWindow.title("Tic Tac Toe")

            TicTacBoard(self.gameWindow, game_mode)

            self.gameWindow.mainloop()

