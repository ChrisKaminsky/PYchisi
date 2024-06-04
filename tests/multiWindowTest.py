import curses

def main(stdscr):
    stdscr.clear()
    stdscr.addstr(10,10, "Murzyns", curses.A_BLINK)
    stdscr.refresh()
    stdscr.getch()

es = curses.wrapper(main)

