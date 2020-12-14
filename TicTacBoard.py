from tkinter import *
from tkinter import messagebox
from TicTacToeButton import *
from MinimaxAlphaBetaAgent import MinimaxAlphaBetaAgent

#when click on ecupied cell, undo delets one cell
#when you exit game board, you cant create new one
class TicTacBoard:

    def __init__(self, gameWindow,game_mode):

        self.game_mode = game_mode

        self.newGame = Button(gameWindow, text="New Game", font=("Helvetica", 10),anchor="n", padx=2, pady=10, bg="SystemButtonFace", command=lambda: self.playNewGame())
        self.undoB = Button(gameWindow, text="Undo", font=("Helvetica", 10), padx=10,anchor="n", pady=10,bg="SystemButtonFace", command=lambda: self.undoPerson(game_mode) ,state="disable")
        self.playerTurnLable = Label(gameWindow, text="X's turn")


        self.buttonMatrix = [[0 for row in range(3)] for col in range(3)]

        for row in range(3):
            for col in range(3):
                self.buttonMatrix[row][col] =TicTacButton(Button(gameWindow, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda row=row, col=col:self.b_click(row, col)),Mark.EMPTY)


        self.locationOnScreen()

        self.turnToPlay = Mark.X
        self.moves = []
        self.count = 0
        #undo - only one step
        self.numOfUndoFirst = 0
        self.numOfUndoSecond = 0
        self.agent = MinimaxAlphaBetaAgent()

    def undo(self, mark):
        lastMove = self.moves.pop()
        self.deleteStep(lastMove)
        self.turnToPlay = mark

    def undoBoardAI(self):
        self.count -= 1

        if self.get_turn_to_play() == Mark.X:
            self.undo(Mark.O)

        else:
            self.undo(Mark.X)

    def undoPerson(self, state):

        self.count -= 1
        if self.count == 0:
            self.undoB.config(state="disable")

        if self.get_turn_to_play() == Mark.X:
            if self.game_mode == 2:
                if self.numOfUndoFirst >= 3:
                    messagebox.showerror("Tic Tac Toe", "You can't do undo more than 3 times")
                    self.undoB.config(state="disable")
                else:
                    self.undo(Mark.O)

                    self.playerTurnLable.config(text="O's turn")
                    self.numOfUndoFirst += 1
            else:
                if self.numOfUndoFirst >= 1:
                    messagebox.showerror("Tic Tac Toe", "You can't do undo more than 1 times")
                    self.undoB.config(state="disable")
                else:
                    self.undo(Mark.O)
                    self.undo(Mark.X)

                    self.playerTurnLable.config(text="X's turn")
                    self.numOfUndoFirst += 1

        else:
            if self.numOfUndoSecond >= 3:
                messagebox.showerror("Tic Tac Toe", "You can't do undo more than 3 times")
            else:
                self.undo(Mark.X)

                self.playerTurnLable.config(text="X's turn")
                self.numOfUndoSecond += 1

    def deleteStep(self, lastMove):
        self.buttonMatrix[lastMove[0]][lastMove[1]].button.config(text=" ")
        self.buttonMatrix[lastMove[0]][lastMove[1]].mark = Mark.EMPTY

    def get_turn_to_play(self):
        return self.turnToPlay

    def locationOnScreen(self):
        for i in range(3):
            for j in range(3):
                self.buttonMatrix[i][j].button.grid(row =i, column=j)

        self.newGame.grid(row=3, column=0)
        self.playerTurnLable.grid(row=3, column=1)
        self.undoB.grid(row=3, column=2)

    def get_possible_moves(self):
        possibleMoves = []
        for x in range(0, 3):
            for y in range(0, 3):
                if self.buttonMatrix[x][y].mark is Mark.EMPTY:
                    possibleMoves.append((x, y))
        return possibleMoves

    def checkIfWin(self):

        if self.buttonMatrix[0][0].mark== self.buttonMatrix[1][1].mark == self.buttonMatrix[2][2].mark and self.buttonMatrix[0][0].mark !=Mark.EMPTY:
            if self.get_turn_to_play()==Mark.X:
                return 10
            else:
                return -10
        if self.buttonMatrix[0][2].mark == self.buttonMatrix[1][1].mark == self.buttonMatrix[2][0].mark and self.buttonMatrix[0][2].mark != Mark.EMPTY:
            if self.get_turn_to_play() == Mark.X:
                return 10
            else:
                return -10
        for i in range(0, 3):
            if self.buttonMatrix[i][0].mark == self.buttonMatrix[i][1].mark == self.buttonMatrix[i][2].mark and self.buttonMatrix[i][0].mark !=Mark.EMPTY:
                if self.get_turn_to_play() == Mark.X:
                    return 10
                else:
                    return -10
            if self.buttonMatrix[0][i].mark == self.buttonMatrix[1][i].mark == self.buttonMatrix[2][i].mark and self.buttonMatrix[0][i].mark !=Mark.EMPTY:
                if self.get_turn_to_play() == Mark.X:
                    return 10
                else:
                    return -10
        return 0

    def __switch_players(self):
        self.turnToPlay = Mark.X if self.turnToPlay is Mark.O else Mark.O

    def turnOffButtons(self):
        for row in range(3):
            for col in range(3):
                self.buttonMatrix[row][col].button.config(state="disable")
    def playNewGame(self):
        for row in range(3):
            for col in range(3):
                self.buttonMatrix[row][col].button.config(text=" ", state="normal")
                self.buttonMatrix[row][col].mark = Mark.EMPTY

        self.undoB.config(state="disable")
        self.playerTurnLable.config(text="X's turn")

        self.count = 0
        self.turnToPlay = Mark.X
        self.numOfUndoSecond = 0
        self.numOfUndoFirst = 0



    def two_player_mode_click_dummy(self, row, col):

        if self.buttonMatrix[row][col].mark==Mark.EMPTY:
            if self.get_turn_to_play() == Mark.X:

                self.buttonMatrix[row][col].mark= Mark.X

                self.moves.append([row, col])

                self.turnToPlay = Mark.O

                self.playerTurnLable.config(text="O's turn")
                self.count += 1

            elif self.get_turn_to_play() == Mark.O:

                self.buttonMatrix[row][col].mark = Mark.O
                self.moves.append([ row, col])

                self.turnToPlay = Mark.X
                self.playerTurnLable.config(text="X's turn")
                self.count += 1

        else:
            messagebox.showerror("Tic Tac Toe", "Hey! That box already been selected")
        # need to add tie



    def two_player_mode_click(self, row, col):

        if self.buttonMatrix[row][col].mark==Mark.EMPTY:
            if self.get_turn_to_play() == Mark.X:
                self.buttonMatrix[row][col].button["text"] = "X"
                self.buttonMatrix[row][col].mark= Mark.X

                self.moves.append([row, col])

                self.turnToPlay = Mark.O
                self.playerTurnLable.config(text="O's turn")
                self.count += 1

            elif self.get_turn_to_play() == Mark.O:
                self.buttonMatrix[row][col].button["text"] = "O"
                self.buttonMatrix[row][col].mark = Mark.O
                self.moves.append([ row, col])

                self.turnToPlay = Mark.X
                self.playerTurnLable.config(text="X's turn")
                self.count += 1

        else:
            messagebox.showerror("Tic Tac Toe", "Hey! That box already been selected")
        # need to add tie

    def one_player_mode_click(self,  row, col):
        self.two_player_mode_click(row, col)
        self.undoB.config(state="normal")
        move = self.agent.choose(self,9-self.count, True)[0]
        self.two_player_mode_click(move[0],move[1])

    def b_click(self, row, col):
        if self.game_mode == 2:
            self.two_player_mode_click( row, col)

            self.undoB.config(state="normal")

            if self.checkIfWin() != 0:
                if self.get_turn_to_play() == Mark.X:
                    messagebox.showerror("Tic Tac Toe", "O Win")
                    self.turnOffButtons()
                else:
                    messagebox.showerror("Tic Tac Toe", "X Win")
                    self.turnOffButtons()

            if self.count == 9:
                messagebox.showerror("Tic Tac Toe", "There is no winner")
                self.turnOffButtons()
        else:
            self.one_player_mode_click( row, col)

