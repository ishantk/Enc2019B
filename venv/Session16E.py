class Order:

    def __init__(self, oid, restaurant, price):
        self.oid = oid
        self.restaurant = restaurant
        self.price = price

    def orderToCSV(self):
        return "{},{},{}\n".format(self.oid,self.restaurant,self.price)


# Objects Created below are temporary as they are in RAM
o1 = Order(1, "Basant", 1000)
o2 = Order(2, "Bistro", 1200)
o3 = Order(3, "Rishi", 700)

print(o1.orderToCSV())
print(o2.orderToCSV())
print(o3.orderToCSV())

file = open("orders.csv","a")
file.write(o1.orderToCSV())
file.write(o2.orderToCSV())
file.write(o3.orderToCSV())

file.close()

print(">> Orders Saved in File")

# Read orders.csv file and sort the data on the basis of price from lowest to highest