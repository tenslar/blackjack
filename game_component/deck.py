# coding: UTF-8
import random
import math

# TODO カードはカードオブジェクトで管理したい
card_list = [
            '♠|1','♠|2','♠|3','♠|4','♠|5','♠|6','♠|7','♠|8','♠|9','♠|10','♠|11','♠|12','♠|13',
            '♣|1','♣|2','♣|3','♣|4','♣|5','♣|6','♣|7','♣|8','♣|9','♣|10','♣|11','♣|12','♣|13',
            '◆|1','◆|2','◆|3','◆|4','◆|5','◆|6','◆|7','◆|8','◆|9','◆|10','◆|11','◆|12','◆|13',
            '♥|1','♥|2','♥|3','♥|4','♥|5','♥|6','♥|7','♥|8','♥|9','♥|10','♥|11','♥|12','♥|13',
            # 1,2,3,4,5,6,7,8,9,10,
            # 1,2,3,4,5,6,7,8,9,10,
            # 1,2,3,4,5,6,7,8,9,10,
]


def fisher_yates_shuffle(source):
    """
    要素数が n の配列 a を、
    配列 source をランダムにシャッフルしたコピーで初期化する
    (配列の添字はともに0から始まる)
    https://ja.wikipedia.org/wiki/フィッシャー–イェーツのシャッフル#「取り出し」アルゴリズム

    Parameters
    ----------
    source : list
        コピー元配列

    Returns
    -------
    a : list
        sourceをシャッフルしたコピー
    """
    source_length = len(source)
    n = range(source_length)
    a = [0] * source_length

    # i を 0 から n - 1 まで増加させながら、以下を実行する
    for i in n:
        # j に 0 以上 i 以下のランダムな整数を代入する
        j = math.floor(random.random() * (i + 1))
        if i != j:
            # もしも j と i が等しくないならば
            # a[i] に a[j] を代入する
            a[i] = a[j]
        # a[j] に source[i] を代入する
        a[j] = source[i]

    return a


class Deck(object):
    """デッキ。山札。

    Attributes
    ----------
    cards : list
        デッキに含まれるカード群
    """
    def __init__(self):
        print(type(card_list))
        self.cards = fisher_yates_shuffle(card_list)

    def draw(self):
        """
        カードを1枚引く

        Returns
        -------
        int
            カード
        """
        card = self.cards.pop()
        return card

    def open(self):
        """
        デッキを公開する

        Returns
        -------
        list
            デッキ内のカードリスト
        """
        return self.cards

