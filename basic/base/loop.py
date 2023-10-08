#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description: 流程控制
'''


def if_demo():
    # 1. 循环判断方式
    # age = int(input("input your age:"))
    # if age >= 18:
    #     print('your age is old: ', age)
    # else:
    #     print('your age is young: ', age)

    # 2. py自动转换False 类型
    v = []
    if v:
        print("Not None")
    else:
        print("None")


def loop_demo():
    # names = ['Michael', 'Bob', 'Tracy']
    # for name in names:
    #     print(name)

    # for - else 判断不存在时刻
    def validate(my_list):
        for item in my_list:
            if item == 'banana':
                print('i found banana content')
                break
        else:
            raise ValueError('i not found banana exception')

    l = ['apple', 'orange', 'grade', 'banana']
    validate(l)


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
    loop_demo()
    # match_case_demo()
