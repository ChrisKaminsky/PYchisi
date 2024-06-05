from menu import *
from gameloop import *

minScreenHeight = 20
minScreenWidth = 80

game = Menu(minScreenHeight,minScreenWidth)
numberOfPlayers = game.run()

game = GameLoop(numberOfPlayers[0],numberOfPlayers[1])
game.run()
