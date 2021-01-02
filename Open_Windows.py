from tkinter import *
from WindowsHandler import *
ONE_PLAYER_MODE = 1
TWO_PLAYERS_MODE = 2
NUMBER_OF_OPEN_WINDOWS = 1

mainWindow = Tk()
mainWindow.title("Tic Tac Toe")
mainWindow.geometry("470x300+300+100")

window_text = ""

mainWindowLabel = Label(mainWindow, font=" none 30 bold", text="Tic Tac Toe", pady= 30, padx=10).grid(row=0, column=0)
windowsHandler = WindowsHandler()

massage_lable = Label(mainWindow, font=" none 10 ", text="", pady=30, foreground="red")
massage_lable.grid(row=1)

"""
Defining buttons
"""
playWithComp = Button(mainWindow, text = "PLAY WITH COMPUTER", padx=25, pady=14, command=lambda: windowsHandler.change_window_or_open_new_window(ONE_PLAYER_MODE,massage_lable))
playWithOther = Button(mainWindow, text = "PLAY WITH OTHER PLAYER", padx=25, pady=14, command=lambda: windowsHandler.change_window_or_open_new_window(TWO_PLAYERS_MODE,massage_lable))

"""
Define button in the grid   
"""
playWithComp.grid(row=2, column=0, padx=8, pady=10)
playWithOther.grid(row=2, column=1)


def close_window():
    """
    The function checks if the secondary screen is open
    If the secondary window is open, it is not possible to close the main window
    """
    if not windowsHandler.windowsIsOpen:
        mainWindow.destroy()


mainWindow.wm_protocol("WM_DELETE_WINDOW", lambda: close_window())

# Open Window
mainWindow.mainloop()

