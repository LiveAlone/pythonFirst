#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

from functools import reduce

'''
description: 函数定义相关测试
'''


def std_demo():
    # 1. 官方函数库
    # print(abs(-100))
    # print(max(1, 2, 3, 4, 5))
    # print(int('123'), int(True))

    # 2. 内置函数构建
    print(map(str, [1, 2, 3, 4]))
    print(reduce(lambda a, b: a + b, [1, 2, 3, 4, 5]))


def x_type(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')

    if x >= 0:
        return x
    else:
        return -x


def default_param():
    # 1. 默认参数
    # def enroll(name, gender, age=6, city='Beijing'):
    #     print('name:', name)
    #     print('gender:', gender)
    #     print('age:', age)
    #     print('city:', city)
    #
    # # enroll('test', 1, 7, '123')
    # # enroll('Sarah', 'F')
    # # enroll('Bob', 'M', 7)
    # enroll('Adam', 'M', city='Tianjin')

    # def add_end(L=[]):
    #     L.append('END')
    #     return L
    #
    # print(add_end())
    # print(add_end())

    # 2. 可变参数
    def func(a, b, c=0, *args, **kw):
        print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

    func(1, 2)
    func(1, 2, c=3)
    func(1, 2, 3, 'a', 'b')
    func(1, 2, 3, 'a', 'b', x=99)
    kw = {'city': 'Beijing', 'job': 'Engineer'}
    func(1, 2, 3, *[1, 2, 3], **{'city': 'Beijing', 'job': 'Engineer'})


if __name__ == '__main__':
    std_demo()

    # print(x_type(100))
    # print(x_type(-100))
    # print(x_type('100'))

    # default_param()
