import curses
from curses import wrapper

class CursesApp:
    def __init__(self):
        self.min_height = 20
        self.min_width = 50
        self.text = "Twoj terminal jest za maly, powieksz go"
        self.hello_text = "hello"
        self.custom_text = "sdfigr"

    def main(self, stdscr):
        # Inicjalizacja par kolorów
        curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
        kolor1 = curses.color_pair(1)
        green = curses.color_pair(2)

        # Pobierz rozmiary terminala
        height, width = stdscr.getmaxyx()

        # Oblicz pozycję początkową, aby tekst był wycentrowany
        center_y = height // 2
        center_x = (width - len(self.text)) // 2

        # Sprawdź, czy terminal jest wystarczająco duży
        if height < self.min_height or width < self.min_width:
            stdscr.clear()
            stdscr.addstr(center_y, center_x, self.text, curses.A_BLINK)
            stdscr.refresh()
            stdscr.getch()
        else:
            # Jeśli terminal jest wystarczająco duży, wyświetl teksty
            stdscr.clear()
            stdscr.addstr(10, 10, self.hello_text, curses.A_BLINK)
            stdscr.addstr(30, 30, self.custom_text, kolor1)
            stdscr.refresh()
            stdscr.getch()

    def run(self):
        wrapper(self.main)

if __name__ == "__main__":
    app = CursesApp()
    app.run()
