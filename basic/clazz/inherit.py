#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

from typing import Iterable

'''
description: 
'''


class Animal(object):
    def run(self):
        print('Animal is running')


class Dog(Animal):
    def run(self):
        print('Dog is running')


class Cat(Animal):
    def run(self):
        print('Cat is running')


def animal_run(animal):
    animal.run()


def test_animal():
    # # 1. 定义抽象接口
    # animal_run(Animal())
    # animal_run(Dog())
    # animal_run(Cat())

    # # 2. 类型判断
    # print(isinstance(Animal(), Animal))

    # 3. 对象属性获取方式
    dog = Dog()
    print(dir(dog))
    print(dog.__class__)
    print(dog.__class__.__name__)
    # 获取函数属性
    print(hasattr(dog, 'run'))
    getattr(dog, 'run')()

    print(type(123))
    print(type('123'))
    print(isinstance('123', Iterable))
    print(type(dog))


def add_method():
    # 1. 自定义扩展方法
    def set_age(self, age):
        self.age = age

    from types import MethodType
    dog = Dog()
    dog.set_age = MethodType(set_age, dog)
    dog.set_age(2)
    print(dog.age)


if __name__ == '__main__':
    test_animal()
    # add_method()
