#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

import math

'''
description: 输入输出文件模块维护
'''


def format_demo():
    # 1. 标准用法
    # year = 2023
    # print(f"this is year {year}")

    # print(f'The value of pi is approximately {math.pi:.10f}.')

    # table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
    # for name, phone in table.items():
    #     print(f'{name:10} ==> {phone:10d}')
    #
    # animals = 'eels'
    # print(f'My hovercraft is full of {animals}.')
    # print(f'My hovercraft is full of {animals!r}.')

    # 2. str.format()
    # print('We are the {} who say "{}!"'.format('knights', 'Ni'))
    # print('{0} and {1}'.format('spam', 'eggs'))
    # print('{1} and {0}'.format('spam', 'eggs'))
    # print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))
    # print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))

    table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
    print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab: {0[Dcab]:d}'.format(table))
    print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

    for x in range(1, 11):
        print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))


def file_demo():
    with open('demo.json', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data)


if __name__ == '__main__':
    # format_demo()
    file_demo()
