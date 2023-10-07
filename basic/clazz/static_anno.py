#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'qjyao'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description: 静态方法定义注解
'''


class A(object):
    def foo(self, x):
        print("executing foo(%s,%s)" % (self, x))
        print('self:', self)

    @classmethod
    def class_foo(cls, x):
        print("executing class_foo(%s,%s)" % (cls, x))
        print('cls:', cls)

    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)" % x)


def static_md():
    # 1. object 对象级别。 2. class 类对象级别。 3. 静态函数定义
    a = A()
    print(a.foo)
    print(a.class_foo)
    print(a.static_foo)

    # 2. 调用方式
    # 函数调用
    a.foo(1)
    A.foo(a, 1)

    # 类函数调用
    a.class_foo(1)
    A.class_foo(1)
    a.static_foo(1)
    A.static_foo(1)


if __name__ == '__main__':
    static_md()
