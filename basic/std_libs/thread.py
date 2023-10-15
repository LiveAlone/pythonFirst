#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'qjyao'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description: 线程相关demo
'''
import threading
import time


# 新线程执行的代码:
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


def thread_demo():
    print("thread %s is running " % threading.current_thread().name)
    t = threading.Thread(target=loop, name='LoopThread')
    t.start()
    t.join()
    print('thread %s ended.' % threading.current_thread().name)


balance = 0
lock = threading.Lock()


def change_it(n):
    # GIL 解释所并不能保证线程安全
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(2000000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()


def thread_lock_demo():
    t1 = threading.Thread(target=run_thread, args=(5,))
    t2 = threading.Thread(target=run_thread, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)


if __name__ == '__main__':
    # thread_demo()
    thread_lock_demo()


