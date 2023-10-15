#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

import logging

'''
description:  异常处理方式
'''


def exception_demo():

    # 1. try - except - else - finally. 代码块处理关系。 定义else进行逻辑块封装
    try:
        print("none")
        raise RuntimeError("err")
    except RuntimeError as e:
        logging.exception(e)
    else:
        print("else not error")
    finally:
        print("finally no error")

    # try:
    #     raise NameError('HiThere')
    # except NameError as e:
    #     print('An exception flew by!')
    #     raise RuntimeError('runtime error') from e


if __name__ == '__main__':
    exception_demo()
