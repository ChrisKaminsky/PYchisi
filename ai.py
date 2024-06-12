from player import *
from random import randint

class Ai(Player):
    def __init__(self,symbol,name,startpos,endpos):
        super().__init__(symbol,name,startpos,endpos)
        self.callToAction = "Kliknij dowolny przycisk żeby rzucić kostką"
        self.wrongMove = "Niedozwolny ruch, 2 pionki nie mogą być na jednym polu"
        self.baseQuestion = "Czy chcesz wystawić pionek z bazy? [T,N]"

    def move(self, board, ui):
        ui.drawScreen(board, f"Gracz {self.name} (AI), ilość pionków w bazie: {self.pawnsInBase}", 0)
        cube = randint(1, 6)
        ui.drawScreen(board, f"Wylosowana liczba to {cube}", 0)

        if (cube == 6 or cube == 1) and len(board.cords[self.startPos][1]) == 0 and self.pawnsInBase > 0:
            decNum = randint(1,10)
            decision = decNum <= 7
            if len(self.onBoard) == 0:
                decision = True
            if decision:
                self.getFromBase(board)
                ui.drawScreen(board, f"Gracz {self.name} (AI), wystawił pionek z bazy.", 0)
                return None

        elif (cube == 6 or cube == 1) and len(board.cords[self.startPos][1]) > 0 and self.pawnsInBase > 0:
            if board.cords[self.startPos][1][0] != self.symbol:
                enemy = board.cords[self.startPos][1][0]
                decNum = randint(1, 10)
                decision = decNum <= 7
                if len(self.onBoard) == 0:
                    decision = True
                if decision:
                    self.getFromBase(board)
                    ui.drawScreen(board, f"Gracz {self.name} (AI), wystawił pionek z bazy.", 0)
                    return (enemy, self.startPos)

        if len(self.onBoard) > 0:
            decNum = randint(1, 10)
            if decNum <= 6:
                odp = 0
            else:
                odp = randint(0, len(self.onBoard)-1)

            for pionek in self.onBoard:
                if pionek[1] + cube > 39:
                    self.winPawn(pionek[0], board, ui)
                    ui.drawScreen(board, f"Gracz {self.name}, doszedł do końca planszy", 0)
                    return None

            new_index = (self.onBoard[odp][0] + cube) % len(board.cords)
            try:
                if board.cords[new_index][1][0] == self.symbol:
                    ui.drawScreen(board, "Wykonano nieprawidłowy ruch, dwa pionki nie mogą być na tym samym polu", 0)
                    return None
                elif len(board.cords[(self.onBoard[odp][0] + cube) % len(board.cords)][1]) > 0:
                    enemy = board.cords[(self.onBoard[odp][0] + cube) % len(board.cords)][1][0]
                    self.movePawn(odp, cube, board)
                    return (enemy, new_index)
            except:
                self.movePawn(odp, cube, board)
                return None





