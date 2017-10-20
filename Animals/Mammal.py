# -*- coding: utf-8 -*-
__author__ = 'NL-lh'


class Mammal(object):
    def __init__(self,a,b):
        self.a=a

        pass
    extremities = 4

    def feeds(self):
        print("milk")

    def proliferates(self):
        pass


class Marsupial(Mammal):
    def proliferates(self):
        print("poach")


class Eutherian(Mammal):
    def proliferates(self):
        print("placenta")
