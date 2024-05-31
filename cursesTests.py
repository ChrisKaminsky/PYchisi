import curses
from curses import wrapper

def main(stdscr):
    curses.init_pair(1,curses.COLOR_BLUE,curses.COLOR_YELLOW)
    curses.init_pair(2,curses.COLOR_GREEN,curses.COLOR_BLACK)
    kolor1 = curses.color_pair(1)
    green = curses.color_pair(2)

    height, width = stdscr.getmaxyx()

    text = "Twoj terminal jest za maly, powieksz go"

    center_y = height // 2
    center_x = (width - len(text)) // 2

    min_height = 40
    min_width = 100

    if height < min_height or width < min_width:
        stdscr.clear()
        stdscr.addstr(center_y, center_x, text, kolor1 | curses.A_BLINK)
        stdscr.refresh()
        stdscr.getch()
    else:
        stdscr.clear()
        stdscr.addstr(10,140,"hello", curses.A_BLINK)
        stdscr.addstr(30,30,"sdfigr",kolor1)
        stdscr.refresh()
        stdscr.getch()

wrapper(main)

# standard loop is clearing drawing something and refreshing :)
# najpierw jest zawsze height a potem width
# windows sie przydadza