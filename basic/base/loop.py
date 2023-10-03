#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description: 流程控制
'''


def if_demo():
    age = int(input("input your age:"))
    if age >= 18:
        print('your age is old: ', age)
    else:
        print('your age is young: ', age)


def loop_demo():
    names = ['Michael', 'Bob', 'Tracy']
    for name in names:
        print(name)


def match_case_demo():
    point = (1, 2)
    match point:
        case (0, 0):
            print('Origin')
        case (0, y):
            print(f'Y axis, y = {y}')
        case (x, 0):
            print(f'X axis, x = {x}')
        case (x, y):
            print(f'X: {x}, Y: {y}')
        case _:
            print('Not match')


if __name__ == '__main__':
    # if_demo()
    # loop_demo()
    match_case_demo()
