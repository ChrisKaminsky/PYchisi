class Board():
    def __init__(self):
        self.cords = self.__generate()

    def __generate(self):
        wyn = []
        plik = open("drawings/cords.txt")
        for linijka in plik.readlines():
            linijka = linijka.strip().split()
            wyn.append(((int(linijka[0]), int(linijka[1])), []))
        plik.close()
        return wyn
