#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'qjyao'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description:
'''
import requests


def requests_first():
    # # 1. get 请求，post 文件上传方式
    # rs = requests.get("https://www.google.com/")
    # print(rs.status_code)
    # print(rs.encoding)
    # # print(rs.content)
    # # print(rs.text)

    url = ""
    upload_files = {'file': open('report.xls', 'rb')}
    r = requests.post(url, files=upload_files)


if __name__ == '__main__':
    requests_first()
