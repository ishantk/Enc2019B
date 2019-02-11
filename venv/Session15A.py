class Cab:
    def bookCab(self, source, destination):
        print("Cab Booked from",source, "to" ,destination)

class OLAMiniCab(Cab):
    def bookCab(self, source, destination):
        print("OLA Mini Cab Booked from",source, "to" ,destination)

class OLASedanCab(Cab):
    def bookCab(self, source, destination):
        print("OLA Sedan Cab Booked from",source, "to" ,destination)

class OLABike(Cab):
    def bookCab(self, source, destination):
        print("OLA Bike Booked from",source, "to" ,destination)


# Polymorphism : Run Time

typeOfCab = int(input("Enter Type of Cab"))

cRef = Cab()

if typeOfCab == 1:
    cRef = OLAMiniCab()
elif typeOfCab == 2:
    cRef = OLASedanCab()
elif typeOfCab == 3:
    cRef = OLABike()
else:
    print("Booking a Random Cab")


cRef.bookCab("Auribises","MBD Mall")


"""
cRef.bookCab("Auribises","MBD Mall")

print()

cRef = OLAMiniCab()
cRef.bookCab("Auribises","MBD Mall")

print()

cRef = OLASedanCab()
cRef.bookCab("Auribises","MBD Mall")

print()

cRef = OLABike()
cRef.bookCab("Auribises","MBD Mall")
"""

# Program : Create a function to ask user type of cab and then book it !!
#           If user enters an invalid choice book a random cab