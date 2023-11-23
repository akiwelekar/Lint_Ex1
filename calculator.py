"""Module providing a calculator function printing python version."""


def add(x,y):
    """Function printing python version."""
    return x+y

def substract(x, y):
    """Function printing python version."""
    return x-y

def multiply(x, y):
    """Function printing python version."""
    return x*y

def divide(x,y):
    """Function printing python version."""
    return x/y

def max_1(x,y,z):
    """Function printing python version."""
    m = x
    if y>m :
        m=y
    if z>m :
        m=z
    return m


print("Sum of 10 and 5 is===   ",  add(10,5))
print("Substraction of 10 and 5 is===   ",  substract(10,5))
print("multiplication of 10 and 5 is===   ",  multiply(10,5))
print("division of of 10 and 5 is===   ",  divide(10,5))
print("max of 17, 10 and 5 is ===   ",  max_1(17,10,5))
