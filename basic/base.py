#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description:  基础语法流程控制
'''


def fluent():
    """
    流程控制语法
    :return:
    """
    # 1. if else 语法
    # x = int(input("Please enter an integer: "))
    # if x < 0:
    #     x = 0
    #     print('Negative changed to zero')
    # elif x == 0:
    #     print('Zero')
    # elif x == 1:
    #     print('Single')
    # else:
    #     print('More')

    # 2. for 循环语法
    # words = ['cat', 'window', 'defenestrate']
    # for w in words:
    #     print(w, len(w))

    # for i in range(5):
    #     print(i)

    # for i in range(5, 10, 2):
    #     print(i)

    # for n in range(2, 10):
    #     for x in range(2, n):
    #         if n % x == 0:
    #             print(n, 'equals', x, '*', n//x)
    #             break
    #     else:
    #         print(n, 'is a prime number')
    #
    # for n in range(2, 10):
    #     if n % 2 == 0:
    #         print('Found an even number', n)
    #         continue
    #     print('Found a odd number', n)


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


def exception_demo():
    # while True:
    #     try:
    #         x = int(input("Please enter a number: "))
    #         break
    #     except ValueError:
    #         print("Oops!  That was no valid number.  Try again...")

    # raise Exception('spam', 'eggs')

    # try:
    #     raise NameError('HiThere')
    # except NameError as e:
    #     print('An exception flew by!')
    #     raise RuntimeError('runtime error') from e

    try:
        raise KeyboardInterrupt
    finally:
        print('Goodbye, world!')


if __name__ == '__main__':
    print("main")
    # fluent()
    # match_case_demo()
    exception_demo()
    print("done")
