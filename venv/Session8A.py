# Object which is Standardized !!
# We will put a RULE that these many attributes are mandatory

class Product:

    # Constructor
    # When Object is Created
    # self is a Reference Variable which will hold HashCode of Current Object
    def __init__(self, pid, name, price, brand, color):
        self.pid = pid
        self.name = name
        self.price = price
        self.brand = brand
        self.color = color

    # Function
    def showProduct(self):
        print("===Product Detail===")
        print(self.name)
        print(self.price)
        print(self.brand)
        print("====================")

# Object Construction
# p1 is a reference variable. It will Hold HashCode of Object
p1 = Product(101, "iPhoneX", 80000, "Apple", "Black")
p2 = Product(201, "iPhone 7 Plus", 50000, "Apple", "White")

p1.showProduct()
p2.showProduct()

print(p1)
print(p2)

# Adding a new attribute
p2.weight = 10

# Removing an existing attribute
del p1.color

# Updating data for Attrinute
p1.price = 90000

print(p1.__dict__)
print(p2.__dict__)