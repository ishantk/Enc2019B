# Function with a single expression
# Function can have default arguments/inputs
def areaOfCircle(radius=2):
    area = 3.14 * radius * radius
    return area

result = areaOfCircle(3)
print("Result is:",result)
print("Result is:",areaOfCircle(5.33))
print("Result is:",areaOfCircle())
print("Result is:",areaOfCircle(radius=2.5))

# Reference Copy
area = areaOfCircle

print("Result is:",area(11.12))

# Lambda : is a function like a regular function
#          but it is a single expression function
#          it has no name, we just use reference to the lambda function as a name

lRef = lambda radius=1 : 3.14 * radius * radius
lRef1 = lambda length = 10, breadth = 20 : length * breadth

print("Result with lambda is:",lRef(5.33))
print("Result with lambda is:",lRef())
print("Area of Rectangle is:",lRef1())
print("Area of Rectangle is:",lRef1(11,11))