# Amazon/Flipkart/Snapdeal

"""
class LedTv:

    def __init__(self, pid, name, brand, price, screenSize, technology):
        self.pid = pid
        self.name = name
        self.brand = brand
        self.price = price
        self.screenSize = screenSize
        self.technology = technology

    def showLedTvDetails(self):
        print("====",self.pid," | ",self.name,"====")
        print("Brand", self.brand)
        print("Price", self.price)
        print("Screen", self.screenSize)
        print("Tech", self.technology)

class Mobile:

    def __init__(self, pid, name, brand, price, screenSize, os, ram, memory):
        self.pid = pid
        self.name = name
        self.brand = brand
        self.price = price
        self.screenSize = screenSize
        self.technology = technology
        self.os = os
        self.ram = ram
        self.memory = memory

    def showMobileDetails(self):
        print("====", self.pid, " | ", self.name, "====")
        print("Brand", self.brand)
        print("Price", self.price)
        print("Screen", self.screenSize)
        print("Tech", self.technology)
        print("OS", self.os)
        print("RAM", self.ram)
        print("Memory", self.memory)

class Shoe:

    def __init__(self, pid, name, brand, price, shoeSize, color):
        self.pid = pid
        self.name = name
        self.brand = brand
        self.price = price
        self.shoeSize = shoeSize
        self.color = color

    def showShoeDetails(self):
        print("====", self.pid, " | ", self.name, "====")
        print("Brand", self.brand)
        print("Price", self.price)
        print("Size", self.shoeSize)
        print("Color", self.color)
"""

# Common Code | Generalization
class Product:

    def __init__(self, pid, name, brand, price):
        self.pid = pid
        self.name = name
        self.brand = brand
        self.price = price

    def showProductDetails(self):
        print("====",self.pid," | ",self.name,"====")
        print("Brand", self.brand)
        print("Price", self.price)

# Inheritance : LedTv IS-A Product | Product is Parent and LedTv is Child
class LedTv(Product):

    def __init__(self, pid, name, brand, price, screenSize, technology):
        Product.__init__(self, pid, name, brand, price)
        self.screenSize = screenSize
        self.technology = technology

    def showLedTvDetails(self):
        Product.showProductDetails(self)
        print("Screen", self.screenSize)
        print("Tech", self.technology)

class Mobile(Product):

    def __init__(self, screenSize, os, ram, memory):
        self.screenSize = screenSize
        self.os = os
        self.ram = ram
        self.memory = memory

    def showMobileDetails(self):
        print("Screen", self.screenSize)
        print("OS", self.os)
        print("RAM", self.ram)
        print("Memory", self.memory)

class Shoe(Product):

    def __init__(self, shoeSize, color):
        self.shoeSize = shoeSize
        self.color = color

    def showShoeDetails(self):
        print("Size", self.shoeSize)
        print("Color", self.color)



p1 = Product(101, "iPhoneX", "Apple", 80000)
p1.showProductDetails()

print(p1.__dict__)
print(Product.__dict__)

print("****************")

l1 = LedTv(101, "Bravia", "Sony", 50000, 50, "OLED")
l1.showLedTvDetails()
# l1.showProductDetails()


print(l1.__dict__)
print(LedTv.__dict__)

