#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

from collections import deque

'''
description: 3. 数据结构
'''


def list_demo():
    # ls = [1, 2, 3]
    # print(ls)

    # ls = list(map(lambda x: x**2, range(10)))
    # ls = squares = [x**2 for x in range(10)]
    # print(ls)

    # ls = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
    # print(ls)

    queue = deque(["Eric", "John", "Michael"])
    queue.append("Terry")
    queue.append("Graham")
    print(queue.popleft())
    print(queue)


def matrix_reverse():
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]
    matrix_rev = [[row[i] for row in matrix] for i in range(4)]
    print(matrix_rev)


def tuple_demo():
    t = 12345, 54321, 'hello!'
    print(t)


def collection_demo():
    # basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
    # print(basket)
    # print('orange' in basket)
    # print('crabgrass' in basket)

    a = set('abracadabra')
    b = set('alacazam')
    print(a)
    print(b)
    print(a - b)
    print(a | b)
    print(a & b)
    print(a ^ b)


def map_demo():
    # tel = {'jack': 4098, 'sape': 4139}
    # print(tel['jack'])
    # print(tel['yao'])  # error not exists

    # dc = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
    # dc = {x: x**2 for x in (2, 4, 6)}
    dc = dict(sape=4139, guido=4127, jack=4098)
    print(dc)


def loop_condition():
    # knights = {'gallahad': 'the pure', 'robin': 'the brave'}
    # for k, v in knights.items():
    #     print(k, v)

    # for i, v in enumerate(['tic', 'tac', 'toe']):
    #     print(i, v)
    #
    # questions = ['name', 'quest', 'favorite color']
    # answers = ['lancelot', 'the holy grail', 'blue']
    # for q, a in zip(questions, answers):
    #     print('what is your {0}? It is {1}.'.format(q, a))
    pass


if __name__ == '__main__':
    # list_demo()
    # matrix_reverse()
    # tuple_demo()
    # collection_demo()
    # map_demo()
    loop_condition()
