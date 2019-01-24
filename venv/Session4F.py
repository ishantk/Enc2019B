# def addNumbers(num1, num2):
def addNumbers(num1 = 1, num2 = 3): # Default Inputs
    num3 = num1 + num2
    return num3

result = addNumbers(10, 20)
print("Result is:",result)

print("Result is:",addNumbers(11, 22))
print("Result is:",addNumbers(num1=17, num2=27))
print("Result is:",addNumbers(num2=17, num1=27))
# print("Result is:",addNumbers()) # Error
print("Result is:", addNumbers())
print("Result is:", addNumbers(12))
print("Result is:", addNumbers(num2=7))

# Assignment:
# Create a Function:
# 1 2 3 4 5 6 7 8 9 10... -> Loop
# 1 + 3 + 5 + . . . . -> adding up odd numbers
# 2 + 4 + 6 + . . . . -> adding up even numbers
# Who is greater ? Sum of Odd Numbers or Sum of Even Numbers

# n represents how many numbers ?
def fun(n):
    sumOdd = 0
    sumEven = 0
    # if whoIsGreatest value is set to 1 -> Odd is Greater
    # else for value 2 -> Even is Greater
    whoIsGreatest = 0


    for num in range(1, n+1):
        if num%2 == 0:
            sumEven = sumEven + num
        else:
            sumOdd = sumOdd + num


    if sumOdd > sumEven:
        whoIsGreatest = 1
    else:
        whoIsGreatest = 2

    return whoIsGreatest


result = fun(123)

if result is 1:
    print("Sum of Odds is Greater")
else:
    print("Sum of Evens is Greater")