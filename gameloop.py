from board import *
from ui import *
from player import *
from playable import *
from ai import *
import curses

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
                        "@":[(7,18),(7,16),(7,14),(7,12)],
                        "&":[(11,11),(10,11),(9,11),(8,11)]}
        self.playersId = {"#": 0,
                         "$": 1,
                         "@": 2,
                         "&": 3}
        self.avilablePlayers = ["#","$","@","&"]
        self.players = []
        self.board = Board()
        self.ui = UI()
        self.winner = ""

        for i in range(human):
            symbol = self.avilablePlayers[0]
            self.players.append(Playable(symbol,self.colorCodes[symbol],self.startPos[symbol],self.endPos[symbol]))
            self.avilablePlayers.pop(0)
        for i in range(ai):
            symbol = self.avilablePlayers[0]
            self.players.append(Ai(symbol,self.colorCodes[symbol],self.startPos[symbol],self.endPos[symbol]))
            self.avilablePlayers.pop(0)

    def __endScreen(self, stdscr):
        stdscr.erase()
        height, width = stdscr.getmaxyx()
        curses.init_pair(1,curses.COLOR_YELLOW, curses.COLOR_BLACK)
        YELLOW_AND_BLACK = curses.color_pair(1)
        win_str = f"Wygrał gracz {self.winner}!!!"

        center_y = height // 2
        center_x = (width - len(win_str)) // 2
        stdscr.erase()
        stdscr.addstr(center_y,center_x, win_str, YELLOW_AND_BLACK | curses.A_BLINK)
        stdscr.refresh()
        stdscr.getch()


    def run(self):
        Break = False
        while True:
            if Break:
                break
            for gracz in self.players:
                kill = gracz.move(self.board,self.ui)
                if kill != None: # kill to krotka ("#",indeksOnBoard)
                    self.players[self.playersId[kill[0]]].returnToBase(kill[1],self.board)
                    self.ui.drawScreen(self.board,"Zbiłeś pionka przeciwnika",0)
                if len(gracz.endPos) == 0:
                    Break = True
                    self.winner = self.colorCodes[gracz.symbol]
                    break
        curses.wrapper(self.__endScreen)

