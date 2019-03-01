from aStar import *

print('Running A* Graph search...')
asa = AStarAlgorithm()
initialState = [8, 1, 7, 4, 5, 6, 2, 0, 3]
asa.aStarGraphSearch(initialState)
initialState2 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
asa.countAtDepth(initialState2, 32)
