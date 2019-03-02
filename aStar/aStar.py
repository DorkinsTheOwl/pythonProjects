from colorama import Fore, Style


class SortedElement:
    pathLen = -1
    f = -1
    state = []
    visited = False
    index = -1
    h = -1
    parent = None
    children = []

    def sort(self, other):
        if self.f != other.f:
            return self.comparison(self.f, other.f)
        else:
            return self.comparison(self.h, other.h)

    def comparison(self, num1, num2):
        if num1 == num2:
            return 0
        if num1 > num2:
            return 1
        if num1 < num2:
            return -1


class AStarAlgorithm:
    def __init__(self):
        self.dim = 3
        self.len = self.dim * self.dim

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
                print('Goal state is not reachable')
                break
            else:
                minF.index = index
                minF.visited = True
                if minF.h == 0:
                    print(f'Minimal path length - {minF.pathLen}; nodes visited: {str(index)}')
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
                            # se.children gets populated for no reason
                            se.children = []  # not sure why I have to do this since I don't add anything to children

                            if str(se.f) not in fDict:
                                fDict[se.f] = []
                                fList.append(se.f)
                                fList.sort()

                            # for i, val in fDict[se.f]:
                            #     print(f'{val.f}', end=' ')
                            fDict[se.f].append(minF.children[len(minF.children) - 1])
                            # print(minF.children[len(minF.children) - 1])
                            print(f'minF children count in while: {len(minF.children) - 1}')
                            fDict[se.f].sort(key=graph.sort)
                            visited.add(key)

                index += 1

    def selectStateToExpand(self, fDict, fList, minF):
        for i in range(0, len(fList)):
            found = False
            while len(fDict[fList[i]]) > 0:
                if fDict[fList[i]][0].visited:
                    del fDict[fList[i]][0]
                else:
                    minF = fDict[fList[i]][0]
                    found = True
                    break

            if found:
                break
        print(f'minF: {len(minF.children)}')
        return minF

    def expand(self, state):
        if len(state) != self.len:
            raise Exception(f'State does not have {str(self.len)} parameters')
        res = []
        for i, val in enumerate(state):
            if val == 0:
                y = i // self.dim
                x = i - (y * self.dim)

                if y - 1 >= 0:
                    newState = state[:]
                    newState[i] = newState[(y - 1) * self.dim + x]
                    newState[(y - 1) * self.dim + x] = 0
                    res.append(newState)

                if y + 1 < self.dim:
                    newState = state[:]
                    newState[i] = newState[(y + 1) * self.dim + x]
                    newState[(y + 1) * self.dim + x] = 0
                    res.append(newState)

                if x - 1 >= 0:
                    newState = state[:]
                    newState[i] = newState[y * self.dim + x - 1]
                    newState[y * self.dim + x - 1] = 0
                    res.append(newState)

                if x + 1 < self.dim:
                    newState = state[:]
                    newState[i] = newState[y * self.dim + x + 1]
                    newState[y * self.dim + x + 1] = 0
                    res.append(newState)

        return res

    def h(self, state):
        if len(state) != self.len:
            raise Exception(f'State does not have {str(self.len)} parameters')

        res = 0
        for i in range(0, len(state)):
            y = i // self.dim
            x = i - (y * self.dim)

            ys = state[i] // self.dim
            xs = state[i] - (ys * self.dim)

            res += abs(y - ys) + abs(x - xs)

        return res
