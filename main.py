from game import *

g = Game()
g.initBoard()
g.printBoard()

exit = False
while not g.finish:
    g.nextMove(g.makeMove())
    g.printBoard()
print("Player with {} win!".format(g.winner.disc))
