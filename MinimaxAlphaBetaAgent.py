from math import inf
from TicTacToeButton import *
from TicTacBoard import *

class MinimaxAlphaBetaAgent():

    def __init__(self):
        return

    def minimax_alpha_beta(self, state, depth, alpha, beta, isMax):
        """
        Search, recursively, the best move that leads the Max player to win or not lose (draw).
        It consider the current state of the game and the available moves at that state,
        then for each valid move it plays (alternating min and max) until it finds a terminal state
        
         Parameters:
         state (): The current state of the board
         depth (int): Of this node from the start of the minimax search
         alpha (int): The minimum score that the maximizing player is assured of 
         beta (int): The maximum score that the minimizing player is assured of
         isMax ():         

         Returns:
        (int,(int,int)): bestValue[0] : the best value that found
                         bestValue[1] : the position of the best value
         """
        if state.checkIfWin() or depth is 0:
            return -1,  state.checkIfWin()- depth 
        if isMax:
            bestValue = -1, -inf
        else:
            bestValue = -1, inf
        for s in state.get_possible_moves():
            row = s[0]
            col = s[1]
            player = Mark.X if isMax else Mark.O
            state.two_player_mode_click(row,col,1)
            value = s, self.minimax_alpha_beta(state, depth - 1, alpha, beta, not isMax)[1]
            state.undoBoardAI()
            if isMax:
                bestValue = max(bestValue, value, key=lambda i: i[1])
                alpha = max(alpha, bestValue[1])
                if alpha >= beta:
                    break
            else:
                bestValue = min(bestValue, value, key=lambda i: i[1])
                beta = min(beta, value[1])
                if alpha >= beta:
                    break
        return bestValue

    def choose(self, state,depth, player):
        """
        
         Parameters:
         state (): The current state of the board
         depth (int): of this node from the start of the minimax search
         player (): 
         
         Returns:
         minimax_alpha_beta: The best value that found and the position of the best value
         """
        return self.minimax_alpha_beta(state, depth, -inf, inf, player)

