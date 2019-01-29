"""
    Step 1. Think of an Object
    Object      : User
    Attributes  :   name
                    phone
                    email
                    age
                    gender
                    address

"""

# Step 2. Create Class User
# Creating a User Defined(By Developer) Type for Object Called User
# Textual Representation of Object
class User:
    pass

print("User class gives: ",User)

# Step 3:
# Object Construction
# u1 and u2 are not Objects
# They are Reference Variable which will point to Object
u1 = User()
u2 = User()

print("u1 is:",u1)
print("u2 is:",u2)
# print(hex(id(u1)))
# print(hex(id(u2)))

# Writing data in Object and creating attributes of an Object
# name is attribute of User Object and John is its value
u1.name = "John"
u1.phone = "+91 99999 88888"
u1.email = "john@example.com"
u1.age = 30
u1.gender = "Male"
u1.address = "Redwood Shores"

u2.name = "Jennie"
u2.phone = "+91 77777 88888"
u2.email = "jennie@example.com"
u2.vehicle = 2
u2.companyName = "ABC International"

print("Data in u1:",u1.__dict__)
print("Data in u2:",u2.__dict__)

print("Type of u1 is:",type(u1))
print("Type of u2 is:",type(u2))

# PS: For Python OOPS says
#     For Every Object we can have different attributes
#                                  in number
#                                  in name
#                                  in value

# Object is not Standardized !! Data in Object can Vary !!