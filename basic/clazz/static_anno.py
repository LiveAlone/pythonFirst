#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'qjyao'
__mail__ = 'yaoqijunmail@foxmail.com'

import collections
from math import hypot

'''
description: 定义抽象方法
'''


class A(object):
    def foo(self, x):
        print("executing foo(%s,%s)" % (self, x))
        print('self:', self)

    @classmethod
    def class_foo(cls, x):
        print("executing class_foo(%s,%s)" % (cls, x))
        print('cls:', cls)

    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)" % x)


def static_md():
    # 1. object 对象级别。 2. class 类对象级别。 3. 静态函数定义
    a = A()
    print(a.foo)
    print(a.class_foo)
    print(a.static_foo)

    # 2. 调用方式
    # 函数调用
    a.foo(1)
    A.foo(a, 1)

    # 类函数调用
    a.class_foo(1)
    A.class_foo(1)
    a.static_foo(1)
    A.static_foo(1)


# 通过内置函数定义卡片
Card = collections.namedtuple('Card', ['rank', 'suit'])


class Desk(object):
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = '方片 黑桃 红桃 梅花'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks
                       for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]

    def __contains__(self, item):
        return item.rank == 'K'


def desk_test():
    # beer_card = Card('7', '红桃')
    # print(beer_card)

    # 1. desk 长度和范围获取
    desk = Desk()
    # print(len(desk))
    # print(desk[28])
    # print(desk[1:6])
    # print(desk[1::4])
    # for card in desk:
    #     print(card)
    # for card in reversed(desk):
    #     print(card)

    # contains 数据包含支持方式
    print(Card('7', '红桃') in desk)
    print(Card('K', '核桃') in desk)


# 重新定义配置函数，支持操作
class Vector(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __repr__(self):
        return 'Vector(%r, %r) ...' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

    def __str__(self):
        return 'Vector(%r, %r) ... str' % (self.x, self.y)


def vector_test():
    v1 = Vector(1, 2)
    v2 = Vector(5, 6)
    print(v2 + v1)
    print(abs(v2))
    print(bool(v1))
    print(bool(Vector(-1, 5)))
    print(v1 * 5)
    print(str(v1))


if __name__ == '__main__':
    # static_md()
    # desk_test()
    vector_test()
