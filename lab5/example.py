from abc import ABC, abstractmethod
from enum import Enum, auto
from functools import wraps



class Candy(ABC):
    def __init__(self, name, mass, amount):
        self.name = name
        self.mass = mass
        self.amount = amount

    @abstractmethod
    def price(self):
        pass


class Sweet:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value

class Chocolate(Sweet):
    def __init__(self, name, price, cocoa):
        super().__init__(name, price)
        self.cocoa = cocoa



class A:
    def who(self):
        return "A"


class B(A):
    def who(self):
        return "B -> " + super().who()


class C(A):
    def who(self):
        return "C -> " + super().who()


class D(B, C):
    def who(self):
        return "D -> " + super().who()

# D - C - B - A  MRO