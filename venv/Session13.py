"""
    HAS-A Relationship
    1 to 1 | 1 to many | many to many
    Person HAS-AN Address
    User Has-A PaymentMethod
    Teacher HAS-A Student
    Employee HAS-A Project
    Customer HAS-AN Order
    Driver Has-A Cab
    User HAS-AN Account/Profile


    >> Person HAS-AN Address
    >> Identification of Objects


    >> Objects and Attributes
    1. Person (Object)
        Attributes:
            name
            phone
            email
            gender
            age

    2. Address (Object)
        Attributes:
            adrsLine
            city
            state
            zipCode

    >>Lets Code:

"""

class Person:
    def __init__(self, name, phone ,email ,gender ,age, adrs):
        # LHS : self.name -> Create an attribute name in Object
        # RHS name -> Input to constructor which will hold a value
        # self.name = name -> Assign value of name in name attribute of object
        self.name = name
        self.phone = phone
        self.email = email
        self.gender = gender
        self.age = age
        self.adrs = adrs    # HAS-A Relationship | 1 to 1 | 1 to many

    def showPerson(self):
        print("====", self.name, "====")
        print("Phone:", self.phone)
        print("Email:", self.email)
        print("Gender:", self.gender)
        print("Age:", self.age)
        # print("Adrs:", self.adrs)
        # self.adrs.showAddress()

        # for i in range(0, len(self.adrs)):
        #     self.adrs[i].showAddress()

        # For-Each Loop
        for a in self.adrs:
            a.showAddress()


class Address:
    def __init__(self, adrsLine ,city, state, zipCode):
        self.adrsLine = adrsLine
        self.city = city
        self.state = state
        self.zipCode = zipCode

    def showAddress(self):
        print("====",self.adrsLine,"====")
        print("City:",self.city)
        print("State:", self.state)
        print("Zip:", self.zipCode)

# Below Statements will be an error
# pRef = Person()
# aRef = Address()

aRef = Address("Redwood Shores", "Ludhiana", "Punjab", 141002)
a1 = Address("Pristing Magnum", "Bengaluru", "Karnataka", 520001)
a2 = Address("Country Homes", "Ludhiana", "Punjab", 141002)

# List
addresses = [aRef, a1, a2]

# pRef = Person("John", "+91 99999 88888", "john@example.com", "Male", 30, aRef)



pRef = Person("John", "+91 99999 88888", "john@example.com", "Male", 30, addresses)



print(pRef.__dict__)
print(aRef.__dict__)
print("aRef is:",aRef)

print()
print("****************")
print()

pRef.showPerson()

