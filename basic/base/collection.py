#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

from collections import deque
from collections.abc import Iterable

'''
description: 集合类型
'''


def list_tuple_demo():
    # # 1. list 列表类型
    # classmates = ['Michael', 'Bob', 'Tracy']
    # print(len(classmates), classmates[1])

    # # 2. tuple
    # t2 = ('a', 'b', ['A', 'B'])
    # print(t2[2][0])
    # print(t2[2][1])

    # # 3. 迭代生成器
    # g = (x * x for x in range(10))
    # print(g)
    # print(next(g))
    # print(next(g))

    # 4. 通过迭代器构建list, list函数和[] 方式
    # ls = list(map(lambda x: x**2, range(10)))
    # ls = [x ** 2 for x in range(10)]
    # ls = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
    # print(ls)

    # 5. 高效率queue
    # queue = deque(["Eric", "John", "Michael"])
    # queue.append("Terry")
    # queue.append("Graham")
    # print(queue.popleft())
    # print(queue)

    # 6. demo matrix revert
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]
    matrix_rev = [[row[i] for row in matrix] for i in range(4)]
    print(matrix_rev)


def dict_demo():
    # tel = {'jack': 4098, 'sape': 4139}
    # print(tel['jack'])
    # print(tel['yao'])  # error not exists

    # dc = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
    # dc = {x: x**2 for x in (2, 4, 6)}
    dc = dict(sape=4139, guido=4127, jack=4098)
    print(dc)


def collection_action():
    # a = set('abracadabra')
    # b = set('alacazam')
    # print(a)
    # print(b)
    # print(a - b)
    # print(a | b)
    # print(a & b)
    # print(a ^ b)

    # 1. loop 循环方式
    # knights = {'gallahad': 'the pure', 'robin': 'the brave'}
    # for k, v in knights.items():
    #     print(k, v)
    #
    # for i, v in enumerate(['tic', 'tac', 'toe']):
    #     print(i, v)

    questions = ['name', 'quest', 'favorite color']
    answers = ['lancelot', 'the holy grail', 'blue']
    for q, a in zip(questions, answers):
        print('what is your {0}? It is {1}.'.format(q, a))


if __name__ == '__main__':
    list_tuple_demo()
    # dict_demo()
    # collection_action()
