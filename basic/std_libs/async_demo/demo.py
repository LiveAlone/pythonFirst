#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'qjyao'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description:
'''
import asyncio
import threading


async def hello():
    print('Hello world! (%s)' % threading.current_thread())
    await asyncio.sleep(1)
    print('Hello again! (%s)' % threading.current_thread())


def demo_hello():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(hello())
    loop.close()


async def demo_tasks():
    loop = asyncio.get_event_loop()
    tasks = [loop.create_task(hello()) for i in range(4)]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    # demo_hello()
    asyncio.run(demo_tasks())
