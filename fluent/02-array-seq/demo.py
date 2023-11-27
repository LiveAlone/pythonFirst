#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

import array
import collections

'''
description: 
'''


def cv(c):
    print("running")
    return ord(c)


if __name__ == '__main__':
    # symbols = "hello world"
    # codes = [ord(c) for c in symbols]
    # print(codes)

    # 元组生成器
    # codes = tuple(cv(c) for c in symbols)
    # array.array('I', (cv(c) for c in symbols))
    # for c in (cv(c) for c in symbols):
    #     print(c)

    # 剩余元素处理
    # a, b, *c = range(10)
    # print(a, b, c)

    # 集合命名方式
    # City = collections.namedtuple('City', 'name country population coordinates')
    # tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
    # print(tokyo)
    # print(City._fields)

    # 切片执行
    # ll = [v for v in range(20)]
    # print(ll)
    # ll[5:10] = [1]
    # print(ll)

    # ll = (1, 2, 3)
    # print(id(ll))
    # ll *= 5
    # print(ll)
    # print(id(ll))

    fruits = ['grape', 'raspberry', 'apple', 'banana']
    print(sorted(fruits))
    print(fruits)
    fruits.sort()
    print(fruits)
