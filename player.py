from monte_carlo import Monte_carlo


class Human(object):
    def __init__(self, disc):
        self.disc = disc

    def play(self):
        move = input("Choose a column: ")
        return move


class Computer(object):
    def __init__(self, disc):
        self.disc = disc

    def play(self, game):
        mc = Monte_carlo()
        return mc.moveChoice(game)
