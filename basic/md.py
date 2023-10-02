#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description: 模块化信息维护
'''

import model.fibo
import sys

if __name__ == '__main__':
    model.fibo.fib(10)
    # print(model.fibo.fib2(10))
    # print(dir(sys))
    print(dir(model.fibo))
