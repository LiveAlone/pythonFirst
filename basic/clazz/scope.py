#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'qjyao'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description:
'''


def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]


def param_outer():
    # # 1. 参数外部变量常量赋值
    # i = 5
    #
    # def f(arg=i):
    #     print(arg)
    #
    # i = 6
    # f()

    # 2. 可变参数列表
    # def f(a, L=[]):
    #     L.append(a)
    #     return L

    def f(a, L=None):
        if L is None:
            L = []
        L.append(a)
        return L

    print(f(1))
    print(f(2))
    print(f(3))


if __name__ == '__main__':
    # scope_test()

    # for e in reverse('yaoqijun'):
    #     print(e)

    param_outer()

