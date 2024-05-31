import curses
from curses import wrapper

def main(stdscr):
    stdscr.clear()
    y = 35
    x = 150
    stdscr.addstr(y,x,f"{y},{x}")
    stdscr.refresh()
    stdscr.getch()

wrapper(main)

# standard loop is clearing drawing something and refreshing :)
# najpierw jest zawsze height a potem width
# windows sie przydadza