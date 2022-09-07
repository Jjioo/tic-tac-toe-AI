import random
from termcolor import colored


class TicTacTow:

    def __init__(self, board: dict):
        self.board = board
        self.player = colored('X', 'red')
        self.bot = colored('O', 'green')

    def printBoard(self, board) -> None:
        print(board[1] + colored('|', 'yellow') + board[2] + colored('|', 'yellow') + board[3])
        print('-+-+-')
        print(board[4] + colored('|', 'yellow') + board[5] + colored('|', 'yellow') + board[6])
        print('-+-+-')
        print(board[7] + colored('|', 'yellow') + board[8] + colored('|', 'yellow') + board[9])
        print(colored("-----", 'yellow'))

    def spaceIsFree(self, position: int) -> bool:
        if self.board[position] == ' ':
            return True
        return False

    def insertLetter(self, letter, position):
        if self.spaceIsFree(position):
            self.board[position] = letter
            self.printBoard(self.board)

            if (self.checkDraw()):
                print('draw!!')
                exit(0)

            if (self.checkWin()):
                if letter == 'X':
                    print('you win !!')
                    exit(0)
                else:
                    print('bot win !!')
                    exit(0)

            return

        else:
            print('cant insert here !!')
        position = input("enter position! :")
        self.insertLetter(letter, int(position))

    def insertLetterBot(self, letter, position):
        if self.spaceIsFree(position):
            self.board[position] = letter
            self.printBoard(self.board)

            if (self.checkDraw()):
                print('draw!!')
                exit(0)

            if (self.checkWin()):
                if letter == 'X':
                    print('bot win !!')
                    exit(0)
                else:
                    print('you win !!')
                    exit(0)
            return

        else:
            print("")
        position = random.randint(1, 9)
        self.insertLetterBot(letter, position)

    def checkDraw(self) -> bool:
        for key in self.board.keys():
            if self.board[key] == ' ':
                return False
        else:

            return True

    def checkWin(self) -> bool:
        if (self.board[1] == self.board[2] and self.board[1] == self.board[3] and self.board[1] != ' '):
            return True
        elif (self.board[4] == self.board[5] and self.board[4] == self.board[6] and self.board[4] != ' '):
            return True
        elif (self.board[7] == self.board[8] and self.board[7] == self.board[9] and self.board[7] != ' '):
            return True
        elif (self.board[1] == self.board[4] and self.board[1] == self.board[7] and self.board[1] != ' '):
            return True
        elif (self.board[2] == self.board[5] and self.board[2] == self.board[8] and self.board[2] != ' '):
            return True
        elif (self.board[3] == self.board[6] and self.board[3] == self.board[9] and self.board[3] != ' '):
            return True
        elif (self.board[1] == self.board[5] and self.board[1] == self.board[9] and self.board[1] != ' '):
            return True
        elif (self.board[7] == self.board[5] and self.board[7] == self.board[3] and self.board[7] != ' '):
            return True
        else:
            return False

    def checkWinMark(self, mark) -> bool:
        if (self.board[1] == self.board[2] and self.board[1] == self.board[3] and self.board[1] == mark):
            return True
        elif (self.board[4] == self.board[5] and self.board[4] == self.board[6] and self.board[4] == mark):
            return True
        elif (self.board[7] == self.board[8] and self.board[7] == self.board[9] and self.board[7] == mark):
            return True
        elif (self.board[1] == self.board[4] and self.board[1] == self.board[7] and self.board[1] == mark):
            return True
        elif (self.board[2] == self.board[5] and self.board[2] == self.board[8] and self.board[2] == mark):
            return True
        elif (self.board[3] == self.board[6] and self.board[3] == self.board[9] and self.board[3] == mark):
            return True
        elif (self.board[1] == self.board[5] and self.board[1] == self.board[9] and self.board[1] == mark):
            return True
        elif (self.board[7] == self.board[5] and self.board[7] == self.board[3] and self.board[7] == mark):
            return True
        else:
            return False

    def playerMove(self):
        dig :list[str] = ['1','2','3','4','5','6','7','8','9']
        position = input("enter position for 'X'! :")
        while position not in dig:
            position = input("enter position for 'X'! :")
        self.insertLetter(self.player, int(position))
        return

    def compMove(self):
        best_score = -1000
        best_move = 0

        for key in self.board.keys():
            if self.board[key] == ' ':
                self.board[key] = self.bot
                score = self.minimax(self.board, 0, False)
                self.board[key] = ' '
                if (score > best_score):
                    best_score = score
                    best_move = key
        self.insertLetter(self.bot, best_move)
        return

    def minimax(self, board, depth, isMaximazing):
        if self.checkWinMark(self.bot):
            return 100
        elif self.checkWinMark(self.player):
            return -100
        elif self.checkDraw():
            return 0
        if isMaximazing:
            best_score = -1000
            for key in board.keys():
                if board[key] == ' ':
                    board[key] = self.bot
                    score = self.minimax(board, 0, False)
                    board[key] = ' '
                    if (score > best_score):
                        best_score = score
            return best_score
        else:
            best_score = 800
            for key in board.keys():
                if board[key] == ' ':
                    board[key] = self.player
                    score = self.minimax(board, 0, True)
                    board[key] = ' '
                    if score < best_score:
                        best_score = score
            return best_score




board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '
         }

board1 = {1: '1', 2: '2', 3: '3',
          4: '4', 5: '5', 6: '6',
          7: '7', 8: '8', 9: '9'
          }
t = TicTacTow(board=board)
t1 = TicTacTow(board=board1)

t.printBoard(board1)
while not t.checkWin():

    t.playerMove()

    t.compMove()