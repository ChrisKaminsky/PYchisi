from board import *
from ui import *
from player import *
from playable import *
from ai import *

class GameLoop():
    def __init__(self,human,ai):
        self.colorCodes = {"#":"Czerwony",
                        "$":"Niebieski",
                        "@":"Zielony",
                        "&":"Zółty"}
        self.startPos = {"#":0,
                        "$":10,
                        "@":20,
                        "&":30}
        self.endPos = {"#":[(7,4),(7,6),(7,8),(7,10)],
                        "$":[(3,11),(4,11),(5,11),(6,11)],
                        "@":[(7,12),(7,14),(7,16),(7,18)],
                        "&":[(8,11),(9,11),(10,11),(11,11)]}
        self.avilablePlayers = ["#","$","@","&"]
        self.players = []
        self.board = Board()
        self.ui = UI()

        for i in range(human):
            symbol = self.avilablePlayers[0]
            self.players.append(Ai(symbol,self.startPos[symbol],self.endPos[symbol]))
            self.avilablePlayers.pop(0)
        for i in range(ai):
            symbol = self.avilablePlayers[0]
            self.players.append(Ai(symbol,self.startPos[symbol],self.endPos[symbol]))
            self.avilablePlayers.pop(0)


    def run(self):
        #plan jest taki zeby iterowac po klasie players i za kazdym razem odpalac move, sprawdzac tez czy ktos juz nie wygrywa
        pass


