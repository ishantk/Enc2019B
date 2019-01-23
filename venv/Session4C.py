# Functions are Reference Types

# Creating or Defining a Function
def fun():
    print("This is hello from fun")


# Execution of Function
fun()

# Printing name of Function -> HashCode
print("fun is:",fun)
print("id of fun is:",hex(id(fun)))

# Reference Copy
fVar = fun
print("fVar is:",fVar) # Printing fVar will also give you HashCode which will be same as of fun
print("id of fVar is:",hex(id(fVar)))

# Execute fVar
fVar()


def fVar():
    print("This is Awesome")

print("fVar is:",fVar)
print("fun is:", fun)