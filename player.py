from abc import ABC, abstractmethod

class Player():
    def __init__(self, symbol,startpos,endpos):
        self.pawnsInBase = 4
        self.startPos = startpos
        self.endPos = endpos
        self.symbol = symbol
        self.onBoard = []
    @abstractmethod
    def move(self):
        pass

    def getFromBase(self):
        if self.pawnsInBase > 0:
            self.pawnsInBase -= 1
            self.onBoard.append(self.startPos)


    def returnToBase(self,pos):
        if self.pawnsInBase < 4:
            self.pawnsInBase += 1
            self.onBoard.remove(pos)

    def winPawn(self,pos):
        self.winningPawns += 1
        self.onBoard.remove(pos)

