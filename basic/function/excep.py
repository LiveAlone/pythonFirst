#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description: 
'''


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
    exception_demo()
