"""Tic Tac Toe Board Representation"""
import random


class TTTBoard(object):
    COMPUTER_ID = 'o'
    HUMAN_ID = 'x'
    EMPTY = ' '
    board = None

    def __init__(self, our_board):
        try:
            self.board = self.runValidate(self.__unicodeToStr(our_board))
        except ValueError as error:
            raise error

    def runValidate(self, our_board):
        if not len(our_board) == 9:
            raise ValueError('Board should only contain 9 chars')
        return our_board
    

    def possibleMoves(self):
        return [i for i, ltr in enumerate(self.board) if ltr == self.EMPTY]
    
    def makeMove(self):
        if self.decideWinner(self.HUMAN_ID) == True:
            raise ValueError('X already wins')

        board = list(self.board)
        if not self.possibleMoves():
            raise Exception('Could not select any move, Tie')
        else:
            move = random.choice(self.possibleMoves())
            board[move] = self.COMPUTER_ID
            self.board = ''.join(board)
            if self.decideWinner(self.COMPUTER_ID) == True:
                raise Exception('O already wins')
            return self.board
    
    def checkWin(self, token, firstPosition, secondPosition, thirdPosition):
        if self.board[firstPosition] == token and \
        self.board[secondPosition] == token and \
        self.board[thirdPosition] == token:
            return True

    def decideWinner(self, token):
        if self.checkWin(token, 0,1,2):
            return True
        if self.checkWin(token, 3,4,5):
            return True
        if self.checkWin(token, 6,7,8):
            return True
        if self.checkWin(token, 0,4,8):
            return True
        if self.checkWin(token, 2,4,6):
            return True
        if self.checkWin(token, 0,3,6):
            return True
        if self.checkWin(token, 1,4,7):
            return True
        if self.checkWin(token, 2,5,8):
            return True

    def __unicodeToStr(self, unicode_var):
        return str(unicode_var)

