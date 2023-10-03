#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description: 数据变量表达式
'''


def var_demo():
    """ 变量表达式 """

    # 1. 基础变量表达式
    # print("""test condition
    # hehe""")
    # print(1.23e10)
    # print("yaoqijun", "hello world")
    # print(True and False)
    # print(10 / 3, 10 // 3)

    # 2. 字符串表达式
    print(u'测试中文配置')
    print(len('\xe4\xb8\xad\xe6\x96\x87'))
    print(len(u'中文'.encode('utf-8')))

    # 3. 字符串格式化表达式
    print('Hello %s' % 'world')
    print('he micale %d, %s, %1.2f, %x' % (100, 'string content', 1.0, 100))
    print('%10d %%' % 3)


def express_demo():
    # 1. 判断表达式是否为空
    # v = None
    v = []
    if v:
        print('v is not None')
    else:
        print('v is None')


if __name__ == '__main__':
    # var_demo()
    express_demo()

