#!/usr/bin/python3

import sys
import os
import random
from collections import deque, Counter, OrderedDict
import itertools


class OrderedCounter(Counter, OrderedDict):
    'Counter that remembers the order elements are first encountered'
    def __repr__(self):
#        return '%r' % (list(OrderedDict(self).items()))
        return '%s(%r)' % (self.__class__.__name__, OrderedDict(self))
    def __reduce__(self):
        return self.__class__, (OrderedDict(self),)


class Game():

    hand_size = {2:10, 3:9, 4:8, 5:7}
    score = {}
    score['dumplings'] = {0:0, 1:1, 2:3, 3:6, 4:10, 5:15, 6:15, 7:15, 8:15, 9:15, 10:15}
    score['nigiri'] = {'salmon': 2, 'squid': 3, 'egg': 1, }

    number_of_round = 3

    def __init__(self, player_names):
        self.player_count = len(player_names)
        self.deck = Deck()
        self.round = 0

        self.players = {player:Player(player) for player in player_names}

        self._new_hands()


    def _new_hands(self):
        for player in self.players.values():
            player.hand = self.deck.draw_hand(self.hand_size[self.player_count])

    def show_hands(self, player=None):
        _players = self.players if not player else player

        for player in _players:
            print(f"'{player}' has: {self.players[player].get_counted_hand()}")

class Player():

    def __init__(self, name):
        self.name = name
        self.played_cards = []
        self.hand = None
        self.number_of_pudding = 0
        self.rolls = 0
        self.score = 0

#        self.knowns = [None] * numberOfPlayers

    def get_counted_hand(self):
        return OrderedCounter(self.hand)


class Deck():

    deck_count = {'tempura':14, 'sashimi':14, 'dumplings': 14, 'puddings':10,
    'rolls_2':12, 'rolls_3':8, 'roll_1':6, 'salmon_nigiri':10, 'squid_nigiri':5,
    'egg_nigiri':5, 'wasabi':6, 'chopsticks':4}

    def __init__(self):
        self.cards = [[card_type] * card_count for (card_type, card_count) in self.deck_count.items()]
        self.cards = deque(itertools.chain(*self.cards))
        random.shuffle(self.cards)


    def draw_hand(self, hand_size):
        return [self.cards.popleft() for _i in range(hand_size)]


if __name__ == '__main__':

    random.seed(0)

    number_of_players = int(sys.argv[1])

    playes = 'abcdefghijklmnopqrstuvwxyz'

    my_game = Game(list(playes[0:number_of_players]))

    my_game.show_hands()


