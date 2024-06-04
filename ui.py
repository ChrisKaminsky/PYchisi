import curses
class UI():
    def __init__(self):
        self.visualBoard = self.__generatePrimaryVisualBoard()

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

    def getBoardString(self):
        str = ""
        for linijka in self.visualBoard:
            str = str + "".join(linijka) + "\n"
        return str

    def generateVisualBoard(self,board):
        for element in board.cords:
            if element[1] != []:
                self.visualBoard[element[0][0]][element[0][1]] = element[1][0]
            else:
                self.visualBoard[element[0][0]][element[0][1]] = "●"

    def drawScreen(self,board,prompt,promptType):
        self.board = board
        self.prompt = prompt
        self.promptType = promptType
        #wrapper trzeba zrobic w init
        #tutaj trzeba rysowac tylko window od planszy

        #albo inaczej
        #bedzie to jedna funkcja z argumentem do promptu
        # i z ifem ktory sprawdza czy to komunikat czy pytanie
        curses.wrapper(self.__drawScreen)

    def __drawScreen(self, stdscr):
        stdscr.erase()

        board_win = curses.newwin(15,50,5,20)
        board_win.erase()

        board_str = self.getBoardString()
        board_win.addstr(0,0,board_str)
        ###czmeu to nie dzial
        board_win.refresh()
        stdscr.refresh()
        stdscr.getch()

es = UI()
es.drawScreen(1,1,1)