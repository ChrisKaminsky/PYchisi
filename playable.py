from player import *

class Playable(Player):
    def __init__(self,symbol,startpos,endpos):
        super().__init__(symbol,startpos,endpos)

    def move(self):
        pass