# def addNumbers(num1, num2):
#     sum = num1 + num2
#     print("sum is",sum)

"""
def addNumbers(numbers):

    sum = 0

    for n in numbers:
        sum = sum + n

    print("sum is",sum)

nums = (10, 20, 30, 40, 50, 60, 70)
addNumbers((10, 20, 30, 40, 50, 60, 70))
"""

# * -> Makes input Parameter to take multiple values
# def addNumbers(*args):
def addNumbers(*numbers):

    print(numbers)
    print(type(numbers))
    sum = 0

    for n in numbers:
        sum = sum + n

    print("sum is",sum)

addNumbers(10, 20, 30, 40, 50, 60, 70)

# ** -> makes input Parameter to take multiple values as dictionary pair
def fun(**kwargs):
    print(kwargs)
    print(type(kwargs))

fun(a=10, b=20, c=30, name="John")

def show(*args, **kwargs):
    print(args)
    print(kwargs)

show("A", "B", a=10, b=20)

# Hw: Explore possible combinations of args in kwargs