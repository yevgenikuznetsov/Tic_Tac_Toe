# tic_tac_toe
The classic game with two modes: against another player or the compute.

Vs. the computer, you will try to beat the implementation of minimax algorithem.

## Minimax algorithem

Minimax is a backtracking algorithm that is used in decision making and game theory to find the optimal move for a player, assuming that your opponent also plays optimally. It is widely used in two player turn-based games such as Tic-Tac-Toe

In Minimax the two players are called maximizer and minimizer. The maximizer tries to get the highest score possible while the minimizer tries to do the opposite and get the lowest score possible.

Every board state has a value associated with it. In a given state if the maximizer has upper hand then, the score of the board will tend to be some positive value. If the minimizer has the upper hand in that board state then it will tend to be some negative value. The values of the board are calculated by some heuristics which are unique for every type of game.


<img  src="/screenshots/minimax_sample1.png" alt="Sample 1" width="400" style="max-width:100%;">
