from colorama import Fore, Style
import math


class SortedElement:
    def __init__(self):
        self.pathLen = -1
        self.f = -1
        self.state = []
        self.visited = False
        self.index = -1
        self.h = -1
        self.parent = None
        self.children = []

    def __lt__(self, other):
        if self.f != other.f:
            return self.f < other.f
        else:
            return self.h < other.h


class AStarAlgorithmNQueens:
    def __init__(self, length):
        self.len = length
        self.dim = int(math.sqrt(length))

    def stateToKey(self, state):
        return ','.join(str(e) for e in state)

    def printState(self, state, parentState):
        print(Style.RESET_ALL, end='')
        for i in range(0, len(state)):

            if state[i] != parentState[i]:
                print(Fore.RED, end='')

            print(state[i], end=' ')

            if state[i] != parentState[i]:
                print(Style.RESET_ALL, end='')

            if (i + 1) % self.dim == 0:
                print()

    def printState2(self, state):
        for index, val in enumerate(state):
            print(str(val), end=' ')
            if (index + 1) % self.dim == 0:
                print()

    def printPathBackwards(self, minF, levelBackwards=0):
        if minF.parent is not None:
            print(f'{levelBackwards}')
            self.printState(minF.state, minF.parent.state)
            self.printPathBackwards(minF.parent, levelBackwards + 1)
        else:
            print(f'{levelBackwards}')
            self.printState2(minF.state)

    def countAtDepth(self, initial, depth):
        se = SortedElement()
        se.state = initial
        se.pathLen = 0
        se.visited = False

        visited = {}
        statesBeforeRequired = []

        for i in range(0, depth + 1):
            if i == 0:
                statesBeforeRequired.append([])
                visited[self.stateToKey(initial)] = True
                statesBeforeRequired[i].append(initial)
            elif i <= depth:
                statesBeforeRequired.append([])
                for j, state in enumerate(statesBeforeRequired[i - 1]):
                    newStates = self.expand(statesBeforeRequired[i - 1][j])
                    for newState in newStates:
                        key = self.stateToKey(newState)
                        if key not in visited:
                            visited[key] = True
                            statesBeforeRequired[i].append(newState)
            print(f'States as depth {i}:{len(statesBeforeRequired[i])}')

    def aStarGraphSearch(self, initial):
        graph = SortedElement()
        graph.state = initial
        graph.h = self.h(initial)
        graph.f = graph.h
        graph.pathLen = 0
        graph.visited = False

        fDict = {}
        fList = []

        fList.append(graph.f)
        fDict[graph.f] = []
        fDict[graph.f].append(graph)

        visited = set()
        key = self.stateToKey(graph.state)
        visited.add(key)
        index = 1
        while True:
            minF = None
            minF = self.selectStateToExpand(fDict, fList, minF)

            if minF is None:
                print(f'Goal state is not reachable. Nodes visited: {index}')
                break
            else:
                minF.index = index
                minF.visited = True
                if minF.h == 0:
                    print(f'Minimal path length - {minF.pathLen}; nodes visited: {index}')
                    self.printPathBackwards(minF)
                    break
                else:
                    newStates = self.expand(minF.state)
                    for val in newStates:
                        key = self.stateToKey(val)
                        if str(key) not in visited:
                            se = SortedElement()
                            se.pathLen = minF.pathLen + 1
                            se.h = self.h(val)
                            se.f = se.h + se.pathLen
                            se.state = val
                            se.parent = minF
                            minF.children.append(se)

                            if se.f not in fDict:
                                fDict[se.f] = []
                                fList.append(se.f)
                                fList.sort()

                            fDict[se.f].append(minF.children[len(minF.children) - 1])
                            fDict[se.f].sort()
                            visited.add(key)

                index += 1

    def selectStateToExpand(self, fDict, fList, minF):
        for i, val in enumerate(fList):
            found = False
            while len(fDict[val]) > 0:
                if fDict[val][0].visited:
                    del fDict[val][0]
                else:
                    minF = fDict[val][0]
                    found = True
                    break

            if found:
                break
        return minF

    def expand(self, state):
        res = []
        for i, val in enumerate(state):
            if val == 1:
                y = i // self.dim
                x = i - y * self.dim
                # if y is 0, queen can go down
                if y == 0:
                    newState = state[:]
                    # check whether or not another queen is blocking move
                    if newState[i + self.dim] == 0:
                        newState[i + self.dim] = 1
                        newState[i] = 0
                        res.append(newState)

                # if y is N-1, queen can go up
                if y == self.dim - 1:
                    newState = state[:]
                    # check whether or not another queen is blocking move
                    if newState[i - self.dim] == 0:
                        newState[i - self.dim] = 1
                        newState[i] = 0
                        res.append(newState)

                # if 0 < y < N-1, queen can go up or down
                if 0 < y < self.dim - 1:
                    # check whether or not another queen is blocking move
                    newState = state[:]
                    if newState[i + self.dim] == 0:
                        newState[i + self.dim] = 1
                        newState[i] = 0
                        res.append(newState)

                    # check whether or not another queen is blocking move
                    newState = state[:]
                    if newState[i - self.dim] == 0:
                        newState[i - self.dim] = 1
                        newState[i] = 0
                        res.append(newState)

                # if x is 0, queen can go right
                if x == 0:
                    # check whether or not another queen is blocking move
                    newState = state[:]
                    if newState[i + 1] == 0:
                        newState[i + 1] = 1
                        newState[i] = 0
                        res.append(newState)

                # if x is N-1, queen can go left
                if x == self.dim - 1:
                    # check whether or not another queen is blocking move
                    newState = state[:]
                    if newState[i - 1] == 0:
                        newState[i - 1] = 1
                        newState[i] = 0
                        res.append(newState)

                # if 0 < x < N-1, queen can go right or left
                if 0 < x < self.dim - 1:
                    # check whether or not another queen is blocking move
                    newState = state[:]
                    if newState[i + 1] == 0:
                        newState[i + 1] = 1
                        newState[i] = 0
                        res.append(newState)

                    # check whether or not another queen is blocking move
                    newState = state[:]
                    if newState[i - 1] == 0:
                        newState[i - 1] = 1
                        newState[i] = 0
                        res.append(newState)

        return res

    def h(self, state):
        res = 0
        for i, val in enumerate(state):
            if val == 0:
                continue

            y = i // self.dim
            x = i - y * self.dim

            for j, nestedVal in enumerate(state):
                if i == j or nestedVal == 0:
                    continue

                y1 = j // self.dim
                x1 = j - y1 * self.dim
                # row or column or diagonal
                if x == x1 or y == y1 or abs(x1 - x) == abs(y1 - y):
                    res += 1

        return res
