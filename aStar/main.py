from aStarNPuzzle import *

# A star for N puzzle problem

print('Running A* Graph search...')
asa = AStarAlgorithm()
# initialState = [8, 1, 7, 4, 5, 6, 2, 0, 3]
# initialState = [1, 2, 0, 4, 3, 5, 6, 7, 8]  # cannot reach goal state
# initialState = [1, 0, 2, 4, 3, 5, 6, 7, 8]  # cannot reach goal state
initialState = [1, 2, 5, 3, 4, 8, 6, 0, 7]  # takes correct amount of steps, but nodes visited could be 2 less
asa.aStarGraphSearch(initialState)
initialState2 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# asa.countAtDepth(initialState2, 32)
