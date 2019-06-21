# coding: UTF-8

class Card:

    def __init__(self, rank:str):
        self.disp = rank
        self._parse_rank(rank)
        self.point = 0
        self.set_point(self.rank)

    def __str__(self):
        return self.disp


    def _parse_rank(self, rank:str):
        suit_rank = rank.split('|')
        self.suit = suit_rank[0]
        self.rank = int(suit_rank[1])

    def set_point(self,rank):
        if rank > 10:
            self.point = 10
        else:
            self.point = rank


class Ace(Card):
    def __str__(self):
        return self.disp

    def set_point(self,rank):
        self.point = rank