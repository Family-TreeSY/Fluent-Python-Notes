---
title: Fluent Python Notes
date: 2018-07-02 17:03:09
tags: Python
---

### **流畅的Python学习笔记**

#### **Chapter One**

变量名类似____xxx____，以双下划线开头，双下划线结尾的就是特殊变量，特殊方法的存在是为了被Python解释器调用的

例如  ____getitem____  这里我们查找key来得出value，d['a']背后的动作就是____getitem____方法

```python
# -*- coding:utf-8 -*-
d = {'a': 1, 'b': 2, 'c': 3}
print(d['a'])

print(d.__getitem__('a'))

print(d['a'] == d.__getitem__('a'))

```

执行结果：

```python
1
1
True
```

#### **Python风格纸牌**
namedtuple()用来创建一个自定义的tuple对象，它和tuple一样都是不可变的，它可以用属性而不是索引来引用tuple的元素


```python
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
        """
        return self._cards[position]


beer_card = Card('7', 'diamonds')
# 用属性来调用tuple的元素
print(beer_card.rank)
print(beer_card.suit)

# 创建实例
deck = FrenchDeck()
# 输出deck长度
print(len(deck))

# 索引出第一张牌
print(deck[0])
# 索引出最后一张纸牌
print(deck[-1])
```

执行结果：

```python
7
diamonds
52
Card(rank='2', suit='spades')
Card(rank='A', suit='hearts')
```

##### **随机抽取一张纸牌**

这里用random.choice来随机生成一张纸牌
```python
from random import choice


print(choice(deck))
print(choice(deck))
```

执行结果：

```python
Card(rank='9', suit='spades')
Card(rank='Q', suit='clubs')
```


##### **切片（slicing）**

____getitem____()方法把[]交给了self._cards，所以类得对象是支持切片操作的

- 索引出前三张牌
- 抽出索引是12的那张牌，然后每隔13张牌拿一张


```python
print(deck[:3])
print(deck[12::13])
```

执行结果：


```python
[Card(rank='2', suit='spades'), Card(rank='3', suit='spades'), Card(rank='4', suit='spades')]
[Card(rank='A', suit='spades'), Card(rank='A', suit='diamonds'), Card(rank='A', suit='clubs'), Card(rank='A', suit='hearts')

```


##### **迭代**

实现____getitem____()后，这一副牌就是可迭代的了
```python
for card in deck:
	print(card)
```


执行结果：

```python
Card(rank='2', suit='spades')
Card(rank='3', suit='spades')
Card(rank='4', suit='spades')
Card(rank='5', suit='spades')
Card(rank='6', suit='spades')
Card(rank='7', suit='spades')
Card(rank='8', suit='spades')

.............
.............
```

也可以反向迭代，使用reversed()方法


```python
for card in reversed(deck):
	print(card)
```



##### **IN运算符**
迭代通常都是隐式的，一个集合类型没有实现____contains____方法，那么in运算符就会按顺序做一次迭代搜索

```python
print(Card('Q', 'hearts') in deck)
print(Card('7', 'beasts') in deck)
```


##### **字符串表示形式**

____str____， ____repr____两者都是字符串表示形式

两者的区别：
____str____是在str()函数被使用，或是在print函数打印一个对象的时候被调用的，是给终端用户看的

____repr____，如果一个对象没有____str____函数，而Python又需要调用它的时候，解释器会用____repr____作为替代，它又可以方便我们调试和记录日志



欢迎访问[Treehl的博客](https://family-treesy.github.io/)
[GitHub](https://github.com/Family-TreeSY/Fluent-Python-Notes)