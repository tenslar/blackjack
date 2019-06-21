# coding: UTF-8
from enum import Enum, auto
from .card import Card, Ace
import re


class PlayerActionSignal(Enum):
    """
    プレイヤー実行可能アクションシグナル
    """
    HIT = auto()
    STAND = auto()


class Player:
    def __init__(self):
        self.hand = []

    def add(self, card):
        if re.match('\A.\|1\Z', card):
            card = Ace(card)
            if self.point() > 10 :
                card.set_point(1)
            else:
                card.set_point(11)
        else:
            card = Card(card)
        self.hand.append(card)

    def point(self):
        sum_point = 0
        for card in self.hand:
            sum_point += card.point

        return sum_point

    def show(self):
        show = '['
        for card in self.hand:
            show += "{},".format(card)
        show = show.strip(',')
        show += ']'
        return show

class Dealer(Player):
    def first_show(self):
        return "[{}, *]".format(next(iter(self.hand), None))