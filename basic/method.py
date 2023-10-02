#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description: 
'''


def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


def param_outer():
    # 1. 参数外部变量常量赋值
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

    # def f(a, L=None):
    #     if L is None:
    #         L = []
    #     L.append(a)
    #     return L
    #
    # print(f(1))
    # print(f(2))
    # print(f(3))
    pass


def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


def lambda_demo():
    # 4. lambda 表达式
    # def make_incrementor(n):
    #     return lambda x: x + n

    # f = make_incrementor(42)
    # print(f(0))
    # print(f(1))

    # 5. pair key
    pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
    pairs.sort(key=lambda pair: pair[1])
    print(pairs)


def ham_eggs(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", ham_eggs.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs


if __name__ == '__main__':
    # ask_ok('Do you really want to quit? \n')
    # param_outer()

    # 3. 参数替换
    # parrot(1000)
    # parrot(voltage=1000)
    # parrot(voltage=1000000, action='VOOOOOM')
    # parrot(action='VOOOOOM', voltage=1000000)
    # parrot('a million', 'bereft of life', 'jump')
    # parrot('a thousand', state='pushing up the daisies')

    # cheeseshop("Limburger", "It's very runny, sir.",
    #            "It's really very, VERY runny, sir.",
    #            shopkeeper="Michael Palin",
    #            client="John Cleese",
    #            sketch="Cheese Shop Sketch")

    # lambda_demo()
    ham_eggs('spam')