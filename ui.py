import curses
from time import sleep
class UI():
    def __init__(self):
        self.visualBoard = self.__generatePrimaryVisualBoard()
        self.special = {(5,1):1,
                       (1,13):2,
                       (9,21):3,
                       (13,9):4,
                       (7, 4): 1,
                       (7, 6): 1,
                       (7, 8): 1,
                       (7, 10): 1,
                       (3, 11): 2,
                       (4, 11): 2,
                       (5, 11): 2,
                       (6, 11): 2,
                       (7, 12): 3,
                       (7, 14): 3,
                       (7, 16): 3,
                       (7, 18): 3,
                       (8, 11): 4,
                       (9, 11): 4,
                       (10, 11): 4,
                       (11, 11): 4}

        self.colors = {"#": 1,
                       "$": 2,
                       "@": 3,
                       "&": 4}
        self.key = None





    def __generatePrimaryVisualBoard(self):
        board = []
        plik = open("drawings/board.txt", "r")
        zawartosc = plik.readlines()
        for linijka in zawartosc:
            linijka = linijka.replace("\n", "")
            temp = []
            for znak in linijka:
                temp.append(znak)
            board.append(temp)
        plik.close()
        return board

    #this is useless
    # def getBoardString(self):
    #     str = ""
    #     for linijka in self.visualBoard:
    #         str = str + "".join(linijka) + "\n"
    #     return str

    def generateVisualBoard(self,board):
        for element in board.cords:
            if element[1] != []:
                self.visualBoard[element[0][0]][element[0][1]] = element[1][0]
            else:
                self.visualBoard[element[0][0]][element[0][1]] = "●"

    def drawScreen(self,board,prompt,promptType):
        self.generateVisualBoard(board)
        self.prompt = prompt
        self.promptType = promptType #0 - komunikat, 1 - pytanie

        curses.wrapper(self.__drawScreen)
        return self.key

    def __drawScreen(self, stdscr):
        curses.init_pair(1,curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        RED = curses.color_pair(1)
        BLUE = curses.color_pair(2)
        GREEN = curses.color_pair(3)
        YELLOW = curses.color_pair(4)
        stdscr.erase()

        stdscr.attron(YELLOW)
        stdscr.border()
        stdscr.attroff(YELLOW)

        board_win = curses.newwin(20, 30,5,20)
        prompt_win = curses.newwin(5,30,5,60)
        stdscr.refresh()

        board_win.erase()
        prompt_win.erase()

        #color test
        # self.visualBoard[5][7] = "#"
        # self.visualBoard[5][9] = "$"
        # self.visualBoard[4][9] = "@"
        # self.visualBoard[3][9] = "&"
        for i, linijka in enumerate(self.visualBoard):
            for j, znak in enumerate(linijka):
                if znak in self.colors.keys():
                    board_win.addch(i, j, znak, curses.color_pair(self.colors[znak]))
                elif (i,j) in self.special.keys():
                    board_win.addch(i, j, znak, curses.color_pair(self.special[(i,j)]))
                else:
                    board_win.addch(i, j, znak)

        if self.promptType == 0:
            prompt_win.addstr(0,0,self.prompt,YELLOW)
            board_win.refresh()
            prompt_win.refresh()
            stdscr.refresh()
            stdscr.getch()
            # sleep(3)
        elif self.promptType == 1:
            prompt_win.addstr(0,0,self.prompt,YELLOW)
            board_win.refresh()
            prompt_win.refresh()
            stdscr.refresh()
            # stdscr.getch()
            self.key = stdscr.getkey()