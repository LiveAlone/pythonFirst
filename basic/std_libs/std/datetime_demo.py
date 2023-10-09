#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'qjyao'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description:
'''

from datetime import datetime, timedelta, timezone


def datetime_demo():
    # # dt = datetime.now()
    # dt = datetime(2015, 4, 19, 12, 20)
    # print(dt, dt.timestamp())

    # # datatime 和 string 之间相互转换
    # cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
    # # print(cday)
    # print(datetime.now().strftime('%a, %b %d %H:%M'))

    # 1. 通过timedelta 设置时间跨度
    # now = datetime.now()
    # now10 = now + timedelta(hours=1)
    # print(now, now10)

    # 2. 时区设置
    tz_utc_8 = timezone(timedelta(hours=8))
    now = datetime.now()
    # now = datetime.utcnow()
    print(now)
    dt = now.astimezone(tz_utc_8)
    print(dt)


if __name__ == '__main__':
    datetime_demo()
