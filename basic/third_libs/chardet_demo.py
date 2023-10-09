#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'qjyao'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description:
'''
import chardet

if __name__ == '__main__':
    # 1. 自动检测字符串内容
    print(chardet.detect(b'Hello, world!'))
    print(chardet.detect("离离原上草，一岁一枯荣".encode('utf-8')))
    print(chardet.detect("离离原上草，一岁一枯荣".encode('gbk')))
    print(chardet.detect('最新の主要ニュース'.encode('euc-jp')))
