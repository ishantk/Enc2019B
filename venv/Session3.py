"""

    Conditional Constructs:
        if/else
        Nested if/else
        Ladder if/else

"""

"""
isInternetConnected = False

if isInternetConnected:
    print("You can browse Internet")
else:
    print("Connect to Internet and Please Try Again")

num1 = 10
num2 = 20

if num1 > num2:
    print("num1 is greatest")
else:
    print("num2 is greatest")

"""

isInternetConnected = False
isGPSConnected = True

# Nested if/else
"""
if isInternetConnected:
    print("You can browse Internet")
    if isGPSConnected:
        print("You can Navigate using Google Maps")
    else:
        print("Connect to GPS and Please Try Again")
else:
    print("Connect to Internet and Please Try Again")
"""

if isInternetConnected and isGPSConnected:
    print("You can Navigate using Google Maps")
else:
    print("Connect to Internet/GPS and Please Try Again")

num1 = 1
num2 = 10
num3 = 50

# Assignment: Implement the correct logic !!

"""
if num1 > num2:
    if num1 > num3:
        print("num1 is greatest")
    else:
        print("num3 is greatest")
else:
    if num2 > num3:
        print("num2 is greatest")
    else:
        print("num3 is greatest")
"""

# Assignment: Complete the correct logic !!
if num1>num2 and num1>num3:
    print("num1 is greatest")
else:
    print("num1 is not greatest")


# Ladder if/else
# OLA App
microCab = 1
miniCab = 2
sedan = 3
bike = 4
auto = 5

print("===========")
print("1 for Micro")
print("2 for Mini")
print("3 for Sedab")
print("4 for Bike")
print("5 for Auto")
print("===========")

userChoice = int(input("What Kind of Cab would you like to book ? Enter Your Choice: "))
if userChoice == microCab:
    print("Micro Cab Booked. Cab Arriving Soon !!")
elif userChoice == miniCab:
    print("Mini Cab Booked. Cab Arriving Soon !!")
elif userChoice == sedan:
    print("Sedan Cab Booked. Cab Arriving Soon !!")
elif userChoice == bike:
    print("Bike Booked. Cab Arriving Soon !!")
elif userChoice == auto:
    print("Auto Booked. Cab Arriving Soon !!")
else:
    print("Please Enter a Valid Choice")



physics = int(input("Enter Marks for Physics"))
chemistry = int(input("Enter Marks for Chemistry"))
maths = int(input("Enter Marks for Maths"))

average = (physics + chemistry + maths)//3

if average >= 80:
    print("Grade A Awarded for Average of",average)
elif average >=70 and average < 80:
    print("Grade B Awarded for Average of", average)
elif average >=60 and average < 70:
    print("Grade C Awarded for Average of", average)
elif average >=50 and average < 60:
    print("Grade D Awarded for Average of", average)
elif average >=40 and average < 50:
    print("Grade E Awarded for Average of", average)
else:
    print("Grade F Awarded for Average of", average)
