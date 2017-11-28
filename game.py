import player


class Game(object):
    def __init__(self):
        self.finish = False
        self.winner = None
        self.player = [None, None]
        self.round = 1
        self.discs = ["X", "O"]
        self.turn = None
        print("Connect Four Game!")

        while self.player[0] == None or self.player[1] == None:
            print("Player A human or computer?")
            selectionA = str(input("Enter c for COMPUTER, h for HUMAN: "))
            if selectionA == 'c':
                self.player[0] = player.Computer(self.discs[0])
            elif selectionA == 'h':
                self.player[0] = player.Human(self.discs[0])
            else:
                print("Invalid input!")
                continue
            print("Player B human or computer?")
            selectionB = str(input("Enter c for COMPUTER, h for HUMAN: "))
            if selectionB == 'c':
                self.player[1] = player.Computer(self.discs[1])
            elif selectionB == 'h':
                self.player[1] = player.Human(self.discs[1])
            else:
                print("Invalid input!")
                continue
        print("Player A go first with X")
        self.turn = self.player[0]

    def initBoard(self):
        self.board = []
        self.height = [int(x) for x in input("Enter height of columns, seperate with space and end by enter: ").split()]
        self.width = len(self.height)
        maxHeight = max(self.height)
        noCount1 = [int(x) for x in input("Enter column row coordinate for no-count cell 1 (e.d. 3 2): ").split()]
        noCount2 = [int(x) for x in input("Enter column row coordinate for no-count cell 2 (e.d. 3 2): ").split()]
        self.noCount1 = [noCount1[0] - 1, noCount1[1] - 1]
        self.noCount2 = [noCount2[0] - 1, noCount2[1] - 1]
        for i in range(self.width):
            self.board.append([])
            for j in range(maxHeight):
                if j < self.height[i]:
                    self.board[i].append(' ')
                else:
                    self.board[i].append('#')
        self.board[noCount1[0] - 1][noCount1[1] - 1] = '.'
        self.board[noCount2[0] - 1][noCount2[1] - 1] = '.'

    def printBoard(self):
        print("Round: " + str(self.round))
        maxHeight = max(self.height)
        for y in range(maxHeight - 1, -1, -1):
            print("\t", end="")
            for x in range(self.width):
                print("| " + str(self.board[x][y]), end=" ")
            print("|")
        for i in range(self.width):
            start = ord('A')
            print("\t  " + chr(start + i), end="")
        print("\n")

    def letterInterprater(self, letter):
        index = ord(letter.lower()) - ord('a')
        return index

    def switchPlay(self):
        if self.turn == self.player[0]:
            self.turn = self.player[1]
        else:
            self.turn = self.player[0]

    def makeMove(self):
        if self.round > sum(self.height):
            print("Draw Game!")
            self.finish = True
            return -1
        if isinstance(self.turn, player.Human):
            move = self.turn.play()
            move = self.letterInterprater(move)
        else:
            move = self.turn.play(self)
        return move

    def nextMove(self, temp):
        if temp == -1:
            return
        move = None
        while move == None:
            if temp >= 0 and temp <= self.width:
                for i in range(self.height[temp]):
                    if self.board[temp][i] == ' ':
                        move = temp
                        self.board[move][i] = self.turn.disc
                        self.round += 1
                        self.endGameDetection(i, move)
                        self.switchPlay()
                        return
                    elif self.board[temp][i] == '.':
                        move = temp
                        self.board[move][i] = self.turn.disc.lower()
                        self.round += 1
                        self.switchPlay()
                        return
                print("Column is full")
                temp = self.makeMove()
            else:
                print("Invalid Input")
                temp = self.makeMove()

    def endGameDetection(self, row, column):
        if (column == self.noCount1[0] and row == self.noCount1[1]) or (
                        column == self.noCount2[0] and row == self.noCount2[1]):
            return
        if self.horizontalDetection(row, column):
            self.finish = True
            self.winner = self.turn
            return
        if self.verticalDetection(row, column):
            self.finish = True
            self.winner = self.turn
            return
        if self.diagonalDetectionA(row, column):
            self.finish = True
            self.winner = self.turn
            return
        if self.diagonalDetectionB(row, column):
            self.finish = True
            self.winner = self.turn
            return

    def horizontalDetection(self, row, column):
        count = 0
        for k in range(column - 1, -1, -1):
            if self.board[k][row] == self.board[column][row]:
                count += 1
            else:
                break
        for k in range(column, self.width):
            if self.board[k][row] == self.board[column][row]:
                count += 1
            else:
                break
        return True if count >= 4 else False

    def verticalDetection(self, row, column):
        count = 0
        for k in range(row, -1, -1):
            if self.board[column][k] == self.board[column][row]:
                count += 1
            else:
                break
        return True if count >= 4 else False

    def diagonalDetectionA(self, row, column):
        count = 0
        j = row
        for i in range(column - 1, -1, -1):
            if self.board[i][j - 1] == self.board[column][row]:
                count += 1
            else:
                break
            j -= 1
            if j < 0: break
        j = row
        for i in range(column, self.width):
            if j >= self.height[i]:
                break
            elif self.board[i][j] == self.board[column][row]:
                count += 1
            else:
                break
            j += 1
        return True if count >= 4 else False

    def diagonalDetectionB(self, row, column):
        count = 0
        j = row
        for i in range(column - 1, -1, -1):
            if j >= self.height[i] - 1:
                break
            elif self.board[i][j + 1] == self.board[column][row]:
                count += 1
            else:
                break
            j += 1
        j = row
        for i in range(column, self.width):
            if j < 0:
                break
            elif self.board[i][j] == self.board[column][row]:
                count += 1
            else:
                break
            j -= 1
        return True if count >= 4 else False

    def getMove(self):
        moves = []
        for i in range(self.width):
            if self.board[i][self.height[i] - 1] == ' ':
                moves.append(i)
        return moves
