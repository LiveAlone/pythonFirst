#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description: 
'''
import multiprocessing
import os
import time
import random
import subprocess


# 定义一个函数，作为新进程的任务
def task(process_name):
    print(f"Task running in process {process_name}, PID: {os.getpid()}")
    time.sleep(5)  # 模拟一些任务


def process_demo():
    print("main process run...")

    # 创建两个新进程，分别执行 task 函数
    p1 = multiprocessing.Process(target=task, args=("Process 1",))
    p2 = multiprocessing.Process(target=task, args=("Process 2",))

    # 启动进程
    p1.start()
    p2.start()

    # 等待进程结束
    p1.join()
    p2.join()

    print("All processes finished.")


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


def pool_process_demo():
    print("main process run...")

    # 创建包含 4 个进程的进程池
    pool = multiprocessing.Pool(processes=4)

    # 执行 8 个任务
    for i in range(8):
        msg = f"hello {i}"
        pool.apply_async(long_time_task, (msg,))

    print("main add all task")
    # 关闭进程池，表示不能在往进程池中添加进程
    pool.close()
    # 等待进程池中的所有进程结束
    pool.join()
    print("All processes finished.")


def subprocess_demo():
    print('$ nslookup www.python.org')
    r = subprocess.call(['nslookup', 'www.python.org'])
    print('Exit code:', r)


if __name__ == '__main__':
    # process_demo()
    # pool_process_demo()
    subprocess_demo()
