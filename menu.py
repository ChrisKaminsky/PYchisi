import curses
class menu:
    def __init__(self,y,x):
        self.numberOfPlayers = 0
        self.min_height = y
        self.min_width = x
        self.title = '''
██████╗ ██╗   ██╗ ██████╗██╗  ██╗██╗███████╗██╗
██╔══██╗╚██╗ ██╔╝██╔════╝██║  ██║██║██╔════╝██║
██████╔╝ ╚████╔╝ ██║     ███████║██║███████╗██║
██╔═══╝   ╚██╔╝  ██║     ██╔══██║██║╚════██║██║
██║        ██║   ╚██████╗██║  ██║██║███████║██║
╚═╝        ╚═╝    ╚═════╝╚═╝  ╚═╝╚═╝╚══════╝╚═╝
'''

    def run(self):
        curses.wrapper(self.__drawScreen)
        return self.numberOfPlayers

    def __drawScreen(self,stdscr):
        stdscr.clear()
        stdscr.addstr(10,10,self.title)
        stdscr.refresh()
        stdscr.getch()

es = menu(100,50)

print(es.run())