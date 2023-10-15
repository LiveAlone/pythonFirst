#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'qjyao'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description: base64 md5 sha1 
'''
import base64
import hashlib
import hmac


def base64_demo():
    # base64 二进制字节流转换可编辑字符串
    print(base64.b64encode(b'binary\x00string'))
    print(base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))

    print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
    print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))
    print(base64.urlsafe_b64decode('abcd--__'))


def md5_demo():
    # # 1 对比防止篡改
    # md5 = hashlib.md5()
    # md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
    # print(md5.hexdigest())
    #
    # md5 = hashlib.md5()
    # md5.update('how to use md5 in '.encode('utf-8'))
    # md5.update('python hashlib?'.encode('utf-8'))
    # print(md5.hexdigest())

    # 2 sha1
    sha1 = hashlib.sha1()
    sha1.update('how to use sha1 in '.encode('utf-8'))
    sha1.update('python hashlib?'.encode('utf-8'))
    print(sha1.hexdigest())


def hmac_demo():
    # hmac 方式保证, 加入key 方式错误
    message = b'Hello, world!'
    key = b'secret'
    h = hmac.new(key, message, digestmod='MD5')
    print(h.digest())


if __name__ == '__main__':
    # base64_demo()
    # md5_demo()
    pass
