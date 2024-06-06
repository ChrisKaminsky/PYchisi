from abc import ABC, abstractmethod

class Player():
    def __init__(self, symbol, name, startpos, endpos):
        self.symbol = symbol
        self.name = name
        self.startPos = startpos
        self.endPos = endpos

        self.pawnsInBase = 4
        self.onBoard = []# tu bede zapisywal pionki w postaci [pos,pokonanaOdleglosc]
    @abstractmethod
    def move(self):
        pass

    #ta tez chyba
    def getFromBase(self,board):
        if self.pawnsInBase > 0:
            self.pawnsInBase -= 1
            board.cords[self.startPos][1].append(self.symbol)
            self.onBoard.append([self.startPos,0])


    #w tych dwoch metodach yrzeba jeszcze usunac z board cords
    def returnToBase(self,index,board):
        if self.pawnsInBase < 4:
            self.pawnsInBase += 1
            board.cords[index][1].pop(0)
            self.onBoard = [item for item in self.onBoard if item[0] != index]

    def movePawn(self,odp,cube,board):
        board.cords[self.onBoard[odp][0]][1].pop(0)  # usun symbol z miejsca
        board.cords[(self.onBoard[odp][0] + cube) % len(board.cords)][1].append(self.symbol)  # dodaj symbol na odpowiednie pole
        self.onBoard[odp][0] = (self.onBoard[odp][0] + cube) % len(board.cords)  # zaktualizuj indeks w self.onBoard
        self.onBoard[odp][1] += cube  # zaktualizuj droge w self.onBoard

    #ta metoda jest dobra
    def winPawn(self,index,board,ui):
        board.cords[index][1].pop(0)
        self.onBoard = [item for item in self.onBoard if item[0] != index]
        ui.visualBoard[self.endPos[-1][0]][self.endPos[-1][1]] = self.symbol
        self.endPos.pop(-1)

