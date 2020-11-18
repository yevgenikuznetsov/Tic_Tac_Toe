from enum import Enum
from tkinter import *
from tkinter import messagebox
from MinimaxAlphaBetaAgent import *

class Mark(Enum):
    X = 2
    O = 4
    EMPTY = 8

#when click on ecupied cell, undo delets one cell
#when you exit game board, you cant create new one
class TicTacBoard:

    def __init__(self, gameWindow,game_mode):
        self.game_mode = game_mode
        self.b1 = Button(gameWindow, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: self.b_click(self.b1, 0, 0))
        self.b2 = Button(gameWindow, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: self.b_click(self.b2, 0 ,1))
        self.b3 = Button(gameWindow, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: self.b_click(self.b3, 0 ,2))
        self.b4 = Button(gameWindow, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: self.b_click(self.b4, 1 ,0))
        self.b5 = Button(gameWindow, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: self.b_click(self.b5, 1 ,1))
        self.b6 = Button(gameWindow, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: self.b_click(self.b6, 1, 2))
        self.b7 = Button(gameWindow, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: self.b_click(self.b7, 2, 0))
        self.b8 = Button(gameWindow, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: self.b_click(self.b8, 2, 1))
        self.b9 = Button(gameWindow, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: self.b_click(self.b9, 2, 2))
        self.newGame = Button(gameWindow, text="New Game", font=("Helvetica", 10),anchor="n", padx=2, pady=10, bg="SystemButtonFace", command=lambda: self.playNewGame())
        self.undoB = Button(gameWindow, text="Undo", font=("Helvetica", 10), padx=10,anchor="n", pady=10,bg="SystemButtonFace", command=lambda: self.undo())

        self.locationOnScreen()

        self.boardMatrix = [[Mark.EMPTY.value for x in range(3)] for y in range(3)]
        self.turnToPlay = Mark.X
        self.moves = []
        self.count = 0
        #undo - only one step
        self.numOfUndoFirst = 0
        self.numOfUndoSecond = 0

    def undo(self):

        self.count -= 2

        print("count" + str(self.count) + "turn" + str(self.get_turn_to_play()) + "first" + str(self.numOfUndoFirst) + "second" + str(self.numOfUndoSecond) + "\n")

        if self.get_turn_to_play() == Mark.X:
            if self.numOfUndoFirst >= 3:
                messagebox.showerror("Tic Tac Toe", "You can't do undo more than 3 times")
            else:

                lastMove = self.moves.pop()
                self.deleteStep(lastMove[0], lastMove[1], lastMove[2])
                lastMove = self.moves.pop()
                self.deleteStep(lastMove[0], lastMove[1], lastMove[2])
                #it should be O turn
                self.turnToPlay = Mark.X
                self.numOfUndoSecond += 1

        else:
            if self.numOfUndoSecond >= 3:
                messagebox.showerror("Tic Tac Toe", "You can't do undo more than 3 times")
            else:
                lastMove = self.moves.pop()
                self.deleteStep(lastMove[0], lastMove[1], lastMove[2])
                lastMove = self.moves.pop()
                self.deleteStep(lastMove[0], lastMove[1], lastMove[2])

                self.turnToPlay = Mark.O
                self.numOfUndoSecond += 1


    def deleteStep(self, b, cordinationX, cordinationY):
        b.config(text=" ")
        self.boardMatrix[cordinationX][cordinationY] = " "


    def get_turn_to_play(self):
        return self.turnToPlay

    def locationOnScreen(self):
        self.b1.grid(row =0, column=0)
        self.b2.grid(row=0, column=1)
        self.b3.grid(row=0, column=2)

        self.b4.grid(row=1, column=0)
        self.b5.grid(row=1, column=1)
        self.b6.grid(row=1, column=2)

        self.b7.grid(row=2, column=0)
        self.b8.grid(row=2, column=1)
        self.b9.grid(row=2, column=2)

        self.newGame.grid(row=3, column=0)
        self.undoB.grid(row=3, column=2)

    def get_possible_moves(self):
        possibleMoves = []
        for x in range(0, 3):
            for y in range(0, 3):
                if self.boardMatrix[x][y] is Mark.EMPTY.value:
                    possibleMoves.append((x, y))
        return possibleMoves

    def checkIfWin(self, row, col):

        if row == 0 and col == 0 or row == 1 and col == 1 or row == 2 and col == 2:
            if self.boardMatrix[0][0] == self.boardMatrix[1][1] == self.boardMatrix[2][2]:
                return True

        if self.boardMatrix[row][0] == self.boardMatrix[row][1] == self.boardMatrix[row][2]:
            return True
        if self.boardMatrix[0][col] == self.boardMatrix[1][col] == self.boardMatrix[2][col]:
            return True

        return False

    def __switch_players(self):
        self.turnToPlay = Mark.X if self.turnToPlay is Mark.O else Mark.O

    def turnOffButtons(self):

        self.b1.config(state="disable")
        self.b2.config(state="disable")
        self.b3.config(state="disable")
        self.b4.config(state="disable")
        self.b5.config(state="disable")
        self.b6.config(state="disable")
        self.b7.config(state="disable")
        self.b8.config(state="disable")
        self.b9.config(state="disable")

    def playNewGame(self):
        self.b1.config(text=" ", state="normal")
        self.b2.config(text=" ", state="normal")
        self.b3.config(text=" ", state="normal")
        self.b4.config(text=" ", state="normal")
        self.b5.config(text=" ", state="normal")
        self.b6.config(text=" ", state="normal")
        self.b7.config(text=" ", state="normal")
        self.b8.config(text=" ", state="normal")
        self.b9.config(text=" ", state="normal")

        # like the init method - method: init_games_attributes

        self.boardMatrix = [[Mark.EMPTY.value for x in range(3)] for y in range(3)]
        self.count = 0
        self.turnToPlay = Mark.X

        self.numOfUndoSecond = 0
        self.numOfUndoFirst = 0

    def two_player_mode_click(self, b, row, col):
        self.moves.append([b, row, col, self.get_turn_to_play()])

        if b["text"] == " " and self.get_turn_to_play() == Mark.X:
            b["text"] = "X"
            self.boardMatrix[row][col] = 'X'
            self.turnToPlay = Mark.O
            self.count += 1
        elif b["text"] == " " and self.get_turn_to_play() == Mark.O:
            b["text"] = "O"
            self.boardMatrix[row][col] = 'O'
            self.turnToPlay = Mark.X
            self.count += 1
        else:
            messagebox.showerror("Tic Tac Toe", "Hey! That box already been selected")
        # need to add tie

        if self.checkIfWin(row, col):
            if self.get_turn_to_play() == Mark.X:
                messagebox.showerror("Tic Tac Toe", "O Win")
                self.turnOffButtons()
            else:
                messagebox.showerror("Tic Tac Toe", "X Win")
                self.turnOffButtons()

        if self.count == 9:
            messagebox.showerror("Tic Tac Toe", "There is no winner")
            self.turnOffButtons()


    def one_player_mode_click(self, b, row, col):
        self.two_player_mode_click(b, row, col)
        move = self.agent.choose(self.model, False)[0]
        move-=1
        AIrow=row/3
        AIcol=col%3
        self.moves.append([b, AIrow,AIcol, self.get_turn_to_play()])
        b["text"] = "O"
        self.boardMatrix[AIrow][AIcol] = 'O'
        self.turnToPlay = Mark.X
        self.count += 1

        # TODO why do we need b and row/col we can switch to b["row"], b["col"]
    def b_click(self, b, row, col):
        if self.game_mode == 2:
            self.two_player_mode_click(b, row, col)
        else:
            self.one_player_mode_click(b, row, col)

