#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description: class 类型定义
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


class MyClass:
    """A simple example class"""
    i = 12345

    def __init__(self):
        self.data = []

    def f(self):
        print(self)
        return 'hello world'


def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]


def generate_express():
    print(sum(i*i for i in range(10)))


if __name__ == '__main__':
    # scope_test()

    # my = MyClass()
    # xf = my.f
    # for i in range(10):
    #     xf()

    # for char in reverse('golf'):
    #     print(char)

    generate_express()
