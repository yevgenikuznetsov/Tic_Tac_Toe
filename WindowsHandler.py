from TicTacBoard import *
import tkinter as tk


class WindowsHandler:
    open_windows = 0
    NUMBER_OF_OPEN_WINDOWS = 1

    def __init__(self):
        """ 
        The constructor for WindowsHandler class.     
        """
        self.gameWindow = None
        self.windowsIsOpen = False
        self.game_mode = 0

    def close_window(self, massage):
        """
        Close secondary window

        Parameters:
            massage (Lable): Display errors if present on the main screen
        """
        self.open_windows -= 1
        self.windowsIsOpen = False
        massage.config(text="")

        self.gameWindow.destroy()

    def change_window_or_open_new_window(self, game_mode, massage):
        """
        The function open now game.
        Checks if the game in the secondary window is the same as the game the player wants to play

        Parameters:
            game_mode (int): Player vs Player mode OR Player vs Computer mode
            massage (Lable): Display errors if present on the main screen
        """
        if not self.windowsIsOpen:
            self.game_mode = game_mode
            self.openNewWindow(game_mode, massage)

        else:
            if game_mode != self.game_mode:
                self.close_window(massage)
                self.game_mode = game_mode

            self.openNewWindow(game_mode, massage)

    def openNewWindow(self, game_mode, message_lable):
        """ 
        The function create new tic-tac-toe game board depending on the mode of the game 
        (Player vs Player OR Player vs Computer) 
  
        Parameters: 
         game_mode (int): Player vs Player mode OR Player vs Computer mode    
        """
        self.windowsIsOpen = True

        if self.open_windows >= self.NUMBER_OF_OPEN_WINDOWS:
            message_lable.config(text="You can't open same game")
        else:
            self.gameWindow = tk.Tk()
            self.open_windows += 1

            self.gameWindow.wm_protocol("WM_DELETE_WINDOW", lambda: self.close_window(message_lable))
            self.gameWindow.title("Tic Tac Toe")

            TicTacBoard(self.gameWindow, game_mode)

            self.gameWindow.mainloop()

