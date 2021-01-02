from tkinter import *
from TicTacToeButton import *
from MinimaxAlphaBetaAgent import MinimaxAlphaBetaAgent


class TicTacBoard:

    def __init__(self, game_window, game_mode):
        """ 
        The constructor for TicTacBoard class. 
  
        Parameters: 
         game_window (WindowsHandler): New tic-tac-toe game board 
         game_mode (int): Player vs Player mode OR Player vs Computer mode    
        """
        self.game_mode = game_mode

        self.newGame = Button(game_window, text="New Game", font=("Helvetica", 10), anchor="n", padx=2, pady=10, bg="SystemButtonFace", command=lambda: self.playNewGame())
        self.undoB = Button(game_window, text="Undo", font=("Helvetica", 10), padx=10, anchor="n", pady=10, bg="SystemButtonFace", command=lambda: self.undoPerson(), state="disable")
        self.player_turn_lab = Label(game_window, text="X's turn")
        self.massage = Label(game_window, text="")

        self.question = Label(game_window, text="You want to start?")
        self.yes = Button(game_window, text="Yes", command=lambda: self.start_play_with_pc(1))
        self.no = Button(game_window, text="No", command=lambda: self.start_play_with_pc(0))

        self.buttonMatrix = [[0 for row in range(3)] for col in range(3)]

        for row in range(3):
            for col in range(3):
                self.buttonMatrix[row][col] = TicTacButton(Button(game_window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda row=row, col=col:self.b_click(row, col)), Mark.EMPTY)

        self.locationOnScreen(game_mode)

        self.turnToPlay = Mark.X
        self.moves = []
        self.count = 0
        self.numOfUndoFirst = 0
        self.numOfUndoSecond = 0
        self.agent = MinimaxAlphaBetaAgent()
        self.win = False
        self.firstPlayer = 0

    def undo(self, mark):
        """
        The function reverses the last move
        
        Parameters:
        mark (Mark): The player that has to do move again 
        """
        last_move = self.moves.pop()
        self.deleteStep(last_move)
        self.turnToPlay = mark

    def start_play_with_pc(self, turn):
        """
            Window setting for a game pc vs player
            If the computer starts the game, His first move was made here
        Parameters:
            turn (int): the user value if he want to play first in the game with pc
        """
        self.firstPlayer = turn

        self.yes.grid_forget()
        self.no.grid_forget()

        for row in range(3):
            for col in range(3):
                self.buttonMatrix[row][col].button.config(text=" ", state="normal")

        if self.firstPlayer == 0:

            self.question.config(text="X-PC, O-You")

            move = self.agent.choose(self, 9 - self.count, False)[0]
            self.two_player_mode_click(move[0], move[1], 0)
        else:
            self.question.config(text="O-PC, X-You")

        self.question.grid(row=0, column=1)

    def undoBoardAI(self):
        """
            The minimax algorithm uses this function, to find best move
        """
        if self.get_turn_to_play() == Mark.X:
            self.undo(Mark.O)

        else:
            self.undo(Mark.X)

    def undoPerson(self):
        """
            Create undo after the users press on undo button
        """
        if self.count == 0:
            self.undoB.config(state="disable")

        if self.get_turn_to_play() == Mark.X:
            if self.game_mode == 2:
                self.check_and_undo_for_person_game(self.numOfUndoFirst, Mark.O, "O's turn")
                self.numOfUndoFirst += 1
            else:
                self.check_and_undo_for_pc_game(self.numOfUndoFirst, Mark.O, Mark.X, "X's turn")
                self.numOfUndoFirst += 1
        else:
            if self.game_mode == 2:
                self.check_and_undo_for_person_game(self.numOfUndoSecond, Mark.X, "X's turn")
                self.numOfUndoSecond += 1
            else:
                self.check_and_undo_for_pc_game(self.numOfUndoSecond, Mark.X, Mark.O, "O's turn")
                self.numOfUndoSecond += 1

    def check_and_undo_for_person_game(self, num_of_undo, mark, text_lable):
        """
            The function check if user can do undo in person vs person game
            If so, the function performs the undo
        Parameters:
            num_of_undo (int): The number of times the user press undo
            mark (int): Represents a user queue
            text_lable (string): Informer of who's the turn
        """
        if num_of_undo >= 3:
            self.massage.config(text="Impossible move", foreground="red")
        else:
            self.count -= 1
            self.undo(mark)

            self.player_turn_lab.config(text=text_lable)

    def check_and_undo_for_pc_game(self, num_of_undo, first_mark, second_mark, text_lable):
        """
            The function check if user can do undo in person vs pc game
            If so, the function performs the undo
        Parameters:
            num_of_undo (int): The number of times the user press undo
            mark (int): Represents a user queue or pc queue
            text_lable (string): Informer of who's the turn
        """
        if num_of_undo >= 1:
            self.massage.config(text="Impossible move", foreground="red")
            self.undoB.config(state="disable")
        else:
            self.count -= 2
            self.undo(first_mark)
            self.undo(second_mark)

            self.player_turn_lab.config(text=text_lable)

    def deleteStep(self, last_move):
        """
        The function deletes the last move made from the tic-tac-toe game board 
        
        Parameters:
        last_move (int[2]): The last move made on tic-tac-toe game board 
        """
        self.buttonMatrix[last_move[0]][last_move[1]].button.config(text=" ")
        self.buttonMatrix[last_move[0]][last_move[1]].mark = Mark.EMPTY

    def get_turn_to_play(self):
        return self.turnToPlay
        """
        The function 
        
        Parameters:
        row (int): row value of the position of player’s move
        col (int): column value of the position of player’s move
        ai (int): 
        """

    def locationOnScreen(self, game_mode):
        if game_mode == 1:
            self.question.grid(row=0)

            self.yes.grid(row=1, column=0)
            self.no.grid(row=1, column=2)

            self.turnOffButtons()

        for i in range(3):
            for j in range(3):
                self.buttonMatrix[i][j].button.grid(row=i+2, column=j)

        self.newGame.grid(row=5, column=0)
        self.player_turn_lab.grid(row=5, column=1)
        self.undoB.grid(row=5, column=2)
        self.massage.grid(row=6, column=1)

    def get_possible_moves(self):
        """
        Find all valid next moves
          
        Returns:
        int[2]: possible_moves, List of moves in int[2] of {row, col} or empty list if gameover
        """
        possible_moves = []
        for x in range(0, 3):
            for y in range(0, 3):
                if self.buttonMatrix[x][y].mark is Mark.EMPTY:
                    possible_moves.append((x, y))
        return possible_moves

    def checkIfWin(self):
        """
        The function has all the winning combinations. All it does is,
        it checks whether any of the winning combinations is satisfied by the current player’s positions.
          
        Returns:
        int: The score of the board
            (10) - The maximizer has upper hand
            (-10) - The minimizer has upper hand
        """
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
        """
        The function switchs the current player, after every successful move
        """
        self.turnToPlay = Mark.X if self.turnToPlay is Mark.O else Mark.O

    def turnOffButtons(self):
        """
        The function disables the buttons after the game is over
        """
        for row in range(3):
            for col in range(3):
                self.buttonMatrix[row][col].button.config(state="disable")

    def playNewGame(self):
        """
        The function creates tic-tac-toe game board
        """
        for row in range(3):
            for col in range(3):
                self.buttonMatrix[row][col].button.config(text=" ", state="normal")
                self.buttonMatrix[row][col].mark = Mark.EMPTY

        self.undoB.config(state="disable")
        self.player_turn_lab.config(text="X's turn")
        self.massage.config(text="")

        self.count = 0
        self.turnToPlay = Mark.X
        self.numOfUndoSecond = 0
        self.numOfUndoFirst = 0

        self.win = False

        if self.game_mode == 1:
            self.renew_screen()

    def renew_screen(self):
        self.question.grid(row=0)
        self.question.config(text="You want to start?")

        self.yes.grid(row=1, column=0)
        self.no.grid(row=1, column=2)

        self.turnOffButtons()

    def two_player_mode_click(self, row, col, ai):
        """
        The function 
        
        Parameters:
        row (int): row value of the position of player’s move
        col (int): column value of the position of player’s move
        ai (int): 
        """
        self.massage.config(text="")

        if self.buttonMatrix[row][col].mark is Mark.EMPTY:
            if self.get_turn_to_play() == Mark.X:

                self.buttonMatrix[row][col].mark = Mark.X

                if ai == 0:
                    self.buttonMatrix[row][col].button["text"] = "X"
                    self.count += 1

                self.moves.append([row, col])
                self.turnToPlay = Mark.O
                self.player_turn_lab.config(text="O's turn")

            elif self.get_turn_to_play() == Mark.O:

                self.buttonMatrix[row][col].mark = Mark.O

                if ai == 0:
                    self.buttonMatrix[row][col].button["text"] = "O"
                    self.count += 1

                self.moves.append([row, col])
                self.turnToPlay = Mark.X
                self.player_turn_lab.config(text="X's turn")

        else:
            self.massage.config(text="Impossible move", foreground="red")

    def one_player_mode_click(self,  row, col):
        """
        The function 
        
        Parameters:
        row (int): row value of the position of player’s move
        col (int): column value of the position of player’s move
        """
        self.two_player_mode_click(row, col, 0)
        self.undoB.config(state="normal")

        if self.firstPlayer == 0:
            move = self.agent.choose(self, 9 - self.count, False)[0]
            self.two_player_mode_click(move[0], move[1], 0)
            self.IsWin()

            if not self.win:
                self.no_winner()

        else:
            if not self.no_winner():
                move = self.agent.choose(self, 9 - self.count, True)[0]
                self.two_player_mode_click(move[0], move[1], 0)
                self.IsWin()


    def no_winner(self):
        """
        Check if the game ends in a draw
        """
        if self.count == 9:
            self.massage.config(text="There is no winner", foreground="red")
            self.turnOffButtons()
            self.undoB.config(state="disable")

            return True

    def b_click(self, row, col):
        """
        The function recognizes the position of player’s move
        
        Parameters:
        row (int): row value of the position of player’s move
        col (int): column value of the position of player’s move
        """
        if self.game_mode == 2:
            self.two_player_mode_click(row, col, 0)

            self.undoB.config(state="normal")

            self.IsWin()

            if not self.win:
                self.no_winner()
        else:
            self.one_player_mode_click(row, col)

    def IsWin(self):
        """
        The function announces the winner of the game
        """
        if self.checkIfWin() != 0:
            self.win = True

            self.undoB.config(state="disable")

            if self.get_turn_to_play() == Mark.X:
                self.massage.config(text="O Win", foreground="blue")
                self.turnOffButtons()
            else:
                self.massage.config(text="X Win", foreground="blue")
                self.turnOffButtons()

