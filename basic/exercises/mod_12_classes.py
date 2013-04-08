#!/usr/bin/python
#-*- coding: utf-8 -*-
u'''
Exercises MOD 12: Classes
'''


class Craps(object):
    """Simple game of craps."""
    def __init__(self):
        self.state = None
        self.dice = dice.Dice()
        self.playing = False

    def start(self):
        """Play one round of craps until win or lose."""
        self.state = CrapsStateComeOutRoll()
        self.playing = True
        while self.playing:
            self.dice.roll()
            self.state = self.state.evaluate(self, self.dice)
            print 'Dice: %s  New State: %s' % (self.dice, self.state)

    def win(self):
        """Used by CrapsState when the roll was a winner."""
        print "winner"
        self.playing = False

    def lose(self):
        """Used by CrapsState when the roll was a loser."""
        print "loser"
        self.playing = False


class CrapsState(object):
    """Superclass for states of a craps game."""
    def evaluate(self, craps_game, dice):
        raise NotImplementedError

    def __str__(self):
        return self.__doc__


class CrapsStateComeOutRoll(CrapsState):
    """Come out roll rules."""
    pass


class CrapsStatePointRoll(CrapsState):
    """Point roll rules."""
    pass

if __name__ == '__main__':
    crasp = Craps()
    crasp.start()
