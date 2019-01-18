# Containers : They will help to store data
# Single Value Container
# a is name of container and 10 is data. We need not to specify type

# Write Operation !!
a = 10
b = 20
c = 2.2

# Update Operation
a = 30

d = 30

# Read Operation
print("a is",a)
print("b is",b)
print("c is",c)
print("d is",d)

# If you anytime wish to know type of any container just use type()
print(type(a))
print(type(b))
print(type(c))
print(type(d))

# If you wish to see hashCode of Container use id()
# HashCode is a decimal value
# 123 -> Decimal Format -> 100*1 + 10*2 + 1*3
# We can represent a number in binary, octa as well as hexa
print("HashCode of a is",id(a))
print("HashCode of b is",id(b))
print("HashCode of c is",id(c))
print("HashCode of d is",id(d))

print("HashCode of a in hexadecimal is", hex(id(a)))
print("HashCode of a octal is", oct(id(a)))
print("HashCode of a binary is", bin(id(a)))


# Delete Operation
del a
del b

# PS: Whatever we write in our .py file,will be executed by Python Interpreter
#     A process will be created which will have main thread
#     main thread will execute jobs in a sequence i.e. one after other

# Errors as a and b does not exist anymore
# print("a is",a)
# print("b is",b)

# e = 'A'
# e = "A"
e = """A"""
print("e is",e)
print("type of e is",type(e))
f = "A"

print("id of e is",id(e))
print("id of f is",id(f))

# PS: a, b, c, d, e and f are Containers !!
#     They are called Reference Variables
# In Python Every Storage Container is Reference Type