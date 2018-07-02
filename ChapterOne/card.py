# -*- coding:utf-8 -*-
import collections


Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        """
        初始化纸牌
        """
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        """
        返回这套字牌的长度
        """
        return len(self._cards)

    def __getitem__(self, position):
        """
        1、返回索引的位置
        2、__getitem__把[]操作self._cards,所以自动支持切片操作
        3、类对象是可以迭代的
        """
        return self._cards[position]


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


beer_card = Card('7', 'diamonds')
# print(beer_card.rank)
# print(beer_card.suit)

deck = FrenchDeck()
# print(len(deck))
# print(deck[0])
# print(deck[-1])
# print('------------------')

# 排序
for card in sorted(deck, key=spades_high):
    print(card)


# for card in deck:
#     print(card)
#
#
# print('--------------------')
#
# for card in reversed(deck):
#     print(card)
#
# print('---------------------')
#
#
# from random import choice
#
#
# print(choice(deck))
# print(choice(deck))
# print('--------------------')
#
# print(deck[:3])
# print(deck[12::13])
#
# print('---------------------')
#
# print(Card('Q', 'hearts') in deck)
# print(Card('7', 'beasts') in deck)
