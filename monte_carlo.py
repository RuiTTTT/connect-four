from copy import deepcopy
from random import choice


class Monte_carlo(object):
    def moveChoice(self, game):
        round = 500
        moves = game.getMove()
        winRatio = dict.fromkeys(moves, 0)
        for i in range(round):
            initMove = choice(moves)
            currentResult = self.trial(game, initMove)
            if currentResult:
                winRatio[initMove] += 1
        for key in winRatio.keys():
            winRatio[key] /= round
        return sorted(winRatio.items(), key=lambda v: v[1], reverse=True)[0][0]

    def trial(self, game, initMove):
        g = deepcopy(game)
        player = g.turn
        g.nextMove(initMove)
        while not g.finish:
            validMove = g.getMove()
            if validMove == []:
                return 0
            g.nextMove(choice(validMove))
        if g.winner == player:
            return True
        else:
            return False
