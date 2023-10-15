#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'qjyao'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description:
'''
import collections


if __name__ == '__main__':
    # # 1. namedtuple
    # Point = collections.namedtuple('Point', ['x', 'y'])
    # p = Point(1, 2)
    # print(p, isinstance(p, Point))
    #
    # # 2. deque 提高访问效率
    # q = collections.deque(['a', 'b', 'c'])
    # q.append('x')
    # q.appendleft('y')
    # print(q)

    # 3. default dict
    # dd = collections.defaultdict(lambda: 'N/A')
    # dd["key1"] = "yqj"
    # print(dd["key1"], dd["key2"])

    # 按照插入有序本身进行排序
    # od = collections.OrderedDict([('a', 1), ('b', 2), ('c', 3)])
    # print(od)

    c = collections.Counter()
    for ch in 'programming':
        c[ch] = c[ch] + 1
    print(c)
