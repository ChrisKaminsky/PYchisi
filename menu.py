import curses
class Menu:
    def __init__(self,y,x):
        self.numberOfAiPlayers = 0
        self.numberOfHumanPlayers = 0
        self.min_height = y
        self.min_width = x
        self.errorText = "Twój terminal jest zbyt mały, powiększ okno :)"
        self.inputHumanText = "Podaj liczbę graczy lokalnych (1-4)"
        self.inputHumanErrorText = "Podaj poprawną ilość graczy lokalnych (1-4)"
        self.inputAiText = f"Podaj liczbę graczy AI (0-{4-self.numberOfHumanPlayers})"
        self.inputAiErrorText = f"Podaj poprawną ilość graczy AI (0-{4-self.numberOfHumanPlayers})"
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
        return (self.numberOfHumanPlayers, self.numberOfAiPlayers)

    def __drawScreen(self, stdscr):
        stdscr.erase()
        height, width = stdscr.getmaxyx()
        curses.init_pair(1,curses.COLOR_YELLOW, curses.COLOR_BLACK)
        YELLOW_AND_BLACK = curses.color_pair(1)

        if self.min_width > width or self.min_height > height:
            center_y = height // 2
            center_x = (width - len(self.errorText)) // 2
            stdscr.erase()
            stdscr.addstr(center_y,center_x,self.errorText,YELLOW_AND_BLACK | curses.A_BLINK)
            stdscr.refresh()
            stdscr.getch()
        else:
            stdscr.attron(YELLOW_AND_BLACK)
            stdscr.border()
            y_center_offset = 3
            title_lines = self.title.strip().splitlines()
            start_y = (height // 2) - (len(title_lines) // 2) - y_center_offset
            for i, line in enumerate(title_lines):
                start_x = (width // 2) - (len(line) // 2)
                stdscr.addstr(start_y + i, start_x, line)
            stdscr.attroff(YELLOW_AND_BLACK)
            stdscr.refresh() # ta linijka naprawie window, nie jestem pewien dlaczego

            prompt_height = 3
            prompt_width = 50
            prompt_y = start_y + len(title_lines) + 2
            prompt_x = (width // 2) - (prompt_width // 2)

            prompt_win = curses.newwin(prompt_height, prompt_width, prompt_y, prompt_x)
            prompt_win.box()
            prompt_win.addstr(1, 1, self.inputHumanText, curses.A_BOLD)
            prompt_win.refresh()

            while True:
                key = stdscr.getkey()
                if self.__inputChecker(key,"Human"):
                    self.numberOfHumanPlayers = int(key)
                    break
                prompt_win.erase()
                prompt_win.box()
                prompt_win.addstr(1,1, self.inputHumanErrorText, curses.A_BOLD)
                prompt_win.refresh()

            if self.numberOfHumanPlayers != 4:
                prompt_win.erase()
                prompt_win.box()
                prompt_win.addstr(1, 1, self.inputAiText, curses.A_BOLD)
                prompt_win.refresh()

                while True:
                    key = stdscr.getkey()
                    if self.__inputChecker(key,"Ai"):
                        self.numberOfAiPlayers = int(key)
                        break
                    prompt_win.erase()
                    prompt_win.box()
                    prompt_win.addstr(1,1,self.inputAiErrorText, curses.A_BOLD)
                    prompt_win.refresh()

            stdscr.refresh()

    def __inputChecker(self, arg, type):
        try:
            i = int(arg)
            if type == "Human":
                return i in {1,2,3,4}
            elif type == "Ai":
                return (i in {0,1,2,3,4}) and (self.numberOfHumanPlayers+i <= 4)
        except ValueError:
            return False
