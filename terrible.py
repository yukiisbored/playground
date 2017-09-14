#!/usr/bin/env python3
import sys
import os
import time
name = 'Yuki'
class Greeter:
    def greet(self):
        print('Hello, world!')
class NameGreeter(Greeter):
    def __init__(self, who='world'):
        self.__who = who
    def greet(self):
        print('Hello, {}!'.format(self.__who))
if __name__ == '__main__':
    Greeter().greet()
    NameGreeter().greet()
    NameGreeter(name).greet()
