def square(x):
    return x*x

lRef = lambda x : x*x

L1 = [10, 11, 34, 21, 33]


# result = map(square, L1)
result = map(lRef, L1)

print(result)
print(type(result))
print(list(result)) # Convert map into list

L2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

lm1 = lambda n : n%2 == 2
# print("Result: ",lm1(7))

result = map(lm1, L2)
print(list(result)) # ?

result = filter(lm1, L2)
print(result)
print(type(result))
print(list(result))

X = [10, 20, 30, 40, 50, 67]
Y = [11, 22, 33, 44, 55]

lm2 = lambda P, Q : P + Q
# print(lm2(10,20))

result = map(lm2, X, Y)
print(list(result))

# punjabPopulation = [10, 20, 30, 40, 50]
punjabPopulation = [12345, 23412, 45221, 67543, 12311, 32345]

lm3 = lambda x,y : x+y
# import functools
from functools import reduce
result = reduce(lm3, punjabPopulation)
print(result)

print()

employees = [
              {"eid":101, "name":"John", "salary":10000},
              {"eid":201, "name":"Jennie","salary":12000},
              {"eid":301, "name":"Fionna","salary":13000}
            ]
lm4 = lambda emps : emps["eid"]
result = map(lm4, employees)
print(list(result))

# in dictionary of employee we will have a salary attribute.
# give bonus of n+1 %age to every employee
# Lets say baseBonusPercentage is: 10
# 1st employee : 10, 2nd Employee : 11, 3rdEmployee : 12 .....
# 10000 -> 11000 .. .. ...
# Use Lambda Expression and map function to solve problem
