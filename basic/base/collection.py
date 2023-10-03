#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

from collections.abc import Iterable

'''
description: 集合类型
'''


def list_tuple_demo():
    # 1. list 列表类型
    # classmates = ['Michael', 'Bob', 'Tracy']
    # print(classmates[0], classmates[1], classmates[2])

    # 2. tuple
    # t2 = ('a', 'b', ['A', 'B'])
    # print(t2[2][0])
    # print(t2[2][1])

    print(isinstance('123', Iterable))

    # 3. 迭代生成器
    g = (x * x for x in range(10))
    # print(g)
    print(next(g))
    print(next(g))
    print(next(g))


def dict_demo():
    dict = {'yao': 1, 'qi': 2, 'jun': 666}
    print(dict['yao'])
    print(dict['qi'])

    s = {1, 2, 3, 1, 2}
    print(s)


if __name__ == '__main__':
    list_tuple_demo()
    # dict_demo()
