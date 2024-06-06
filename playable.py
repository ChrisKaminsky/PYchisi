from player import *
from random import randint

class Playable(Player):
    def __init__(self,symbol,name,startpos,endpos):
        super().__init__(symbol,name,startpos,endpos)
        self.callToAction = "Kliknij dowolny przycisk żeby rzucić kostką"
        self.wrongMove = "Niedozwolny ruch, 2 pionki nie mogą być na jednym polu"
        self.baseQuestion = "Czy chcesz wystawić pionek z bazy? [T,N]"

 #                          0 - komunikat, 1 - pytanie
#                           self.onBoard ma itemki w postaci [4,2] gdzie 4 to indeks board, a 2 to dlugosc pokonana

    def move(self,board,ui):
        ui.drawScreen(board,f"Gracz {self.name}, ilość pionków w bazie: {self.pawnsInBase}",0)
        ui.drawScreen(board,self.callToAction,1)
        cube = randint(1,6)
        ui.drawScreen(board,f"Wylosowana liczba to {cube}",0)

        #jak inny gracz stoi ci na spawnie to sie nie pojawisz zmienic to
        if (cube == 6 or cube == 1) and len(board.cords[self.startPos][1]) == 0 and self.pawnsInBase > 0:
            odp = ui.drawScreen(board, self.baseQuestion, 1)
            while True:
                if odp == "t":
                    self.getFromBase(board)
                    ui.drawScreen(board, f"Gracz {self.name}, wystawił pionek z bazy.", 0)
                    return None
                elif odp == "n":
                    break
                else:
                    odp = ui.drawScreen(board, f"Kliknij T, jeśli chcesz wystawić pionek, lub N żeby wybrać ruch innym pionkiem", 1)

        if len(self.onBoard) > 0:
            pionkiIndeks = [item[0] for item in self.onBoard]
            pionkiCords = [board.cords[x][0] for x in pionkiIndeks]
            i = 1
            pionkiStr = ""
            for cord in pionkiCords:
                pionkiStr = pionkiStr + str(i) + " - " + "(" + str(cord[1]) + "," + str(cord[0]) + ")" + ", "
                i += 1

            check = list(range(1,len(self.onBoard)+1))
            odp = ui.drawScreen(board, f"Wybierz pinonka którym chcesz wykonać ruch: {pionkiStr}", 1)
            while True:
                try:
                    odp = int(odp)
                    if odp in check:
                        break
                    else:
                        odp = ui.drawScreen(board,f"Wybierz pinonka którym chcesz wykonać ruch, wybierając liczbe odpowiadającym odpowiedniemu pionkowi: {pionkiStr}",1)
                except:
                    odp = ui.drawScreen(board, f"Wybierz pinonka którym chcesz wykonać ruch, wybierając liczbe odpowiadającym odpowiedniemu pionkowi: {pionkiStr}", 1)
            odp -= 1

            for pionek in self.onBoard:
                if pionek[1]+cube > 39:
                    self.winPawn(pionek[0],board,ui)
                    ui.drawScreen(board,f"Gracz {self.name}, doszedł do końca planszy",0)
                    return None

            new_index = (self.onBoard[odp][0]+cube) % len(board.cords)
            try:
                #if pole na ktore chce isc jest zajete przez jeden z moich pionkow
                if board.cords[new_index][1][0] == self.symbol:
                    ui.drawScreen(board, "Wykonano nieprawidłowy ruch, dwa pionki nie mogą być na tym samym polu", 0)
                    return None
                #if pole na ktore chce isc jest zajete przez pionek wroga
                elif len(board.cords[(self.onBoard[odp][0]+cube)%len(board.cords)][1]) > 0:
                    enemy = board.cords[(self.onBoard[odp][0] + cube) % len(board.cords)][1][0]
                    self.movePawn(odp,cube,board)
                    return (enemy, new_index)
            except:
                self.movePawn(odp, cube, board)
                return None





