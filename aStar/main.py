from aStarNPuzzle import *
from aStarNQueens import *

# A star for N puzzle problem
# print('Running A* for N Puzzle...')
# puzzle = AStarAlgorithmNPuzzle()
# initialState = [8, 1, 7, 4, 5, 6, 2, 0, 3]
# puzzle.aStarGraphSearch(initialState)
# initialState2 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# puzzle.countAtDepth(initialState2, 32)

# A star for N Queens problem
print('Running A* for N Queens...')
# TODO: 5x5 can be done by visiting only 17 nodes, right now it visits 24
initialState = [
    1, 1, 1, 1, 1,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
]
queens = AStarAlgorithmNQueens(len(initialState))
queens.aStarGraphSearch(initialState)
