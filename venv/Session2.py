# On UI any data which has to be taken as input will be textual i.e. String
# Any output which has to be displayed will be a textual i.e. String
data = input("Enter Some Data: ")
print("Data is",data)
print("Type of Data is",type(data))

# Once we have read the data as text we can convert it to the type we want
num1 = int(data)
print("num1 is",num1,"and type is:",type(num1))

# Lets Write Program for Calculating Sum of 2 nos.

# a, b and c represents model
a = input("Enter Number A: ")
b = input("Enter Number B: ")
c = a + b # logical operation -> controller
print("Sum of",a,"and",b,"is",c)
# Command Line Interface -> view or UI