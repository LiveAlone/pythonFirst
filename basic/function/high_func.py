#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description: 高阶函数使用
'''


def high_method_params():

    # # 1. 通过高阶函数，完成延迟计算，提高效率
    # def lazy_sum(*args):
    #     def sum():
    #         ax = 0
    #         for n in args:
    #             ax = ax + n
    #         return ax
    #
    #     return sum
    #
    # f1 = lazy_sum(1, 3, 5, 7, 9)
    # f2 = lazy_sum(1, 3, 5, 7, 9)
    # print(f1 == f2)
    # print(f1())
    # print(f2())

    # 2. 函数依赖外部相同变量
    # def count():
    #     fs = []
    #     for i in range(1, 4):
    #         def f():
    #             return i * i
    #         fs.append(f)
    #     return fs

    def count():
        fs = []
        for i in range(1, 4):
            def f(j=i):
                return j * j
            fs.append(f)
        return fs

    f1, f2, f3 = count()
    print(f1())
    print(f2())
    print(f3())


def func_annotation():
    # # 1. 定义修饰函数注解, 日志方式
    # def log(func):
    #     def wrapper(*args, **kw):
    #         print('call %s():' % func.__name__)
    #         return func(*args, **kw)
    #     return wrapper
    #
    # @log
    # def now():
    #     print('2023-12-25')
    #
    # f = now
    # f()
    # print(now.__name__)
    # now()

    # 2. 返回wrapper 支持参数
    def log(text):
        def decorator(func):
            def wrapper(*args, **kw):
                print('%s %s():' % (text, func.__name__))
                return func(*args, **kw)
            return wrapper
        return decorator

    @log('execute')
    def now():
        print('2013-12-25')

    f = now
    f()
    print(now.__name__)
    now()


if __name__ == '__main__':
    # high_method_params()
    func_annotation()
