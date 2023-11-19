#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description: 
'''


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


def lib_func_demo():
    # abs
    # f = abs
    # print(f(-10))
    # print(abs.__name__)

    # map filter
    # for it in map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]):
    #     print(it)
    #
    # for it in filter(lambda x: x % 2 == 1, range(1, 20)):
    #     print(it)

    print(sorted([36, 5, -12, 9, -21], key=abs))


if __name__ == '__main__':
    # 1. 默认参数定义
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

    # 2. 参数支持lambda 表达式
    # lambda_demo()

    # 3. 参数支持类型定义
    # ham_eggs('spam')

    # 4. 官方函数执行
    lib_func_demo()
