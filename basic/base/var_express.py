#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description: 输出表达式格式化
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
    # print(u'测试中文配置')
    # print(len('\xe4\xb8\xad\xe6\x96\x87'))
    # print(len(u'中文'.encode('utf-8')))

    # print(ord('A'), ord('姚'), chr(25991), '中文'.encode('utf-8'))

    # print(len('中文'))
    # print('中文'.encode('utf-8')) # 其实长度6个
    # print(len(b'\xe4\xb8\xad\xe6\x96\x87')) # 中文编码后二进制字节
    # print(len('中文'.encode('utf-8')))

    # 3. 字符串格式化表达式
    # print('Hello %s' % 'world')
    # print('he micale %d, %s, %1.2f, %x' % (100, 'string content', 1.0, 100))
    # print('%10d %%' % 3)


def str_encode():
    # # 1. 字符表示方式
    # s = '𩰡𠜎𪚥𫐄'
    # print(len(s), ord(s[1]))
    # print(chr(132878))
    # print('\u4e2d\u6587')

    # 2. 字符转换
    print('中文'.encode('utf-8'))
    print(r'中文')
    print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
    print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))


if __name__ == '__main__':
    # var_demo()
    str_encode()

