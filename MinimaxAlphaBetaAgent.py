from math import inf
from TicTacToeButton import *
from TicTacBoard import *

class MinimaxAlphaBetaAgent():

    def __init__(self):
        return

    def staticEval(self, state):
        return state.score

    // The algorithm maintains two values, alpha and beta, which respectively represent the minimum score that
    // the maximizing player is assured of and the maximum score that the minimizing player is assured of.
    // state – Current move of player  
    // depth – Scanning depth
    // alpha – Initially, alpha is negative infinity
    // beta – Initially, beta is positive infinity
    // isMax – max player

    def minimax_alpha_beta(self, state, depth, alpha, beta, isMax):
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
                # return s, alpha
            else:
                bestValue = min(bestValue, value, key=lambda i: i[1])
                beta = min(beta, value[1])
                if alpha >= beta:
                    break
                # return s, beta
        return bestValue

    def choose(self, state,depth, player):
        return self.minimax_alpha_beta(state, depth, -inf, inf, player)

