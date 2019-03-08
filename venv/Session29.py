def hello():
    return "Hello"


# Reference Copy !!
h = hello

print(h)
print(type(h))

print(h())
print(hello())

print("++++++++++++++")

def helloAgain():
    yield "Hello 1"
    yield "Hello 2"
    yield "Hello 3"


# Reference Copy
ha = helloAgain
print(ha)
print(type(ha))

print("++++++++++++++")

# Executing ha or helloAgain function will return us a generator
gen = ha()
print(gen)
print(type(gen))

print("++++++++++++++")

print(next(gen))
print(next(gen))
print(next(gen))