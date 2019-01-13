import os


class TicTackToeGame:
    board = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
    player1Turn = True
    draw = False

    def __init__(self):
        self.player1, self.player2 = self.chooseSymbol()
        print(f'Player one is {self.player1}')
        print(f'Player two is {self.player2}')

    def chooseSymbol(self):
        symbol = input('Player 1 choose X or O: ').upper()
        while symbol != 'X' and symbol != 'O':
            symbol = input('Player 1 choose X or O: ').upper()

        if symbol == 'X':
            returnValues = ['X', 'O']
        else:
            returnValues = ['O', 'X']

        return returnValues

    def printBoard(self):
        os.system('cls||clear')
        for row in self.board:
            for index, field in enumerate(row):
                print(f'{self.printField(index, field)}', end='')
            print('')

    def printField(self, index, field):
        if index < 2:
            return f' {field} |'
        else:
            return f' {field} '

    def inputValue(self):
        value = int(input('Enter a number where to place your marker:\n'))

        if 9 >= value >= 7:
            row = 0
        elif 6 >= value >= 4:
            row = 1
        else:
            row = 2

        value = (value + 2) % 3

        if self.board[row][value] != 'X' and self.board[row][value] != 'O':
            if self.player1Turn:
                self.board[row][value] = 'X'
            else:
                self.board[row][value] = 'O'
        else:
            self.printBoard()
            self.printPlayersAction('turn')
            print('Choose a different field')
            self.inputValue()

        self.printBoard()

    def checkWinner(self):
        self.inputValue()
        checkFieldsFilled = 0
        checkValue = 'X' if self.player1Turn else 'O'

        # check row
        for row in self.board:
            checkValueTimes = 0
            for index, field in enumerate(row):
                if field == checkValue:
                    checkValueTimes += 1

            if checkValueTimes == 3:
                return True

        # check diagonal
        if self.board[1][1] == checkValue:
            if self.board[0][0] == checkValue and self.board[2][2] == checkValue:
                return True
            if self.board[2][0] == checkValue and self.board[0][2] == checkValue:
                return True

        # check columns
        for rowIndex, row in enumerate(self.board):
            checkValueTimes = 0
            for index, field in enumerate(row):
                if self.board[index][rowIndex] == checkValue:
                    checkValueTimes += 1

                if checkValueTimes == 3:
                    return True

        # check for draw
        for row in self.board:
            for field in row:
                if field == 'X' or field == 'O':
                    checkFieldsFilled += 1

        if checkFieldsFilled == 9:
            self.draw = True
            return True

        self.player1Turn = not self.player1Turn
        return False

    def startGame(self):
        self.printBoard()
        startGame = True
        while startGame:
            self.printPlayersAction('turn')
            startGame = not self.checkWinner()
        else:
            if self.draw:
                print('It\'s a draw')
            else:
                self.printPlayersAction('won')

            print('Play again? Type y or Y to play again:')
            if input().lower() == 'y':
                self.board = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
                self.startGame()

    def printPlayersAction(self, action):
        if self.player1Turn:
            print(f'Player 1 {action}')
        else:
            print(f'Player 2 {action}')
