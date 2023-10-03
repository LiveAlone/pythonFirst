#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

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
    # animal_run(Animal())
    # animal_run(Dog())
    # animal_run(Cat())

    # 1. 类型判断
    # print(isinstance(Animal(), Animal))

    dog = Dog()
    # print(dir(dog))
    # print(dog.__class__)
    # print(dog.__class__.__name__)
    # print(hasattr(dog, 'run'))
    getattr(dog, 'run')()


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
    # test_animal()
    add_method()
