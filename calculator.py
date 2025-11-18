"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def square_root(a):
    if a < 0:
        raise ValueError("can't be less than 0")
    return math.sqrt(a)
def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b): # raise ZeroDivisionError if a == 0
    if a == 0:
        raise ZeroDivisionError("Cannot divide by 0!")

def logarithm(a, b):# use math library/raise ValueError

    if a == 1 or a <= 0 or b > 0:
        raise ValueError("can't put those numbers there")
    return math.log(b, a)


def exponent(a, b):
    return a ** b




