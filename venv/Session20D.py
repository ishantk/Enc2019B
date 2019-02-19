print(">> App Started")

try:
    numbers = [10, 20, 30, 40, 50]
    print("numbers[0] is:",numbers[0])
    num1 = int(input("Enter Number1: "))
    num2 = int(input("Enter Number2: "))
    num3 = num1/num2
    print("Division is:",num3)

# except ZeroDivisionError as ref:
#     print("Error Occurred: ",ref)
# except IndexError as ref:
#     print("Error Occurred: ",ref)

except Exception as eRef: # Exception is parent class of all the Exceptions in Python | RTP
    print("Error Occurred: ", eRef)
finally:
    print(">>This must be executed")

print(">> App Finished")

# In Python we have error which occur only at run time !!
# Run Time Error is also known as Exception !!
# When exception comes, program is terminated abnormally !! App never finishes !!
# App has Crashed !!

# So, as remedy we can use try and except keywords !!