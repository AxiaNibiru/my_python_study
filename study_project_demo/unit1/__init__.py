import collections

from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


print(Card.__doc__)
print()

beer_card = Card('7', 'diamonds')
print(beer_card)

deck = FrenchDeck()
# 实现了 __len__ 之后，deck可以直接获取长度
print(len(deck))

# 实现了 __getitem__ 之后，deck可以使用下标调用 __getitem__
print(deck[0])
print(deck[1])

# 通过库函数和 __get_item，随机获取某一个元素
print(choice(deck))
print(choice(deck))
print(choice(deck))

# 实现了 __getitem__ 之后，deck可以使用切片
print(deck[:3])
print(deck[12::13])
print(deck[12:13])

# 实现了 __getitem__ 之后，deck变成可迭代的了
for item in deck:
    pass

for item in reversed(deck):
    pass

# 迭代通常是隐式的，譬如说一个集合类型没有实现 __contains__ 方法，那么 in 运算符就会按顺序做一次迭代搜索
print(Card('Q', 'hearts') in deck)
print(Card('7', 'hearts') in deck)

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


# 扑克牌排序
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


for card in sorted(deck, key=spades_high):
    print(card)

# 手动实现一个向量Vector，包含各类操作
from math import hypot


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % self.x, self.y

    def __abs__(self):
        return hypot(self.x, self.y)

    # bool() -> 如果向量的膜返回0，则返回False，否则返回True
    def __bool__(self):
        # return bool(abs(self))
        return bool(self.x or self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


import string
a=string.punctuation


