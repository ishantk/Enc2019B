class Order:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def showOrder(self):
        print("====",self.name,"====")
        print("Price:\u20b9",self.price)
        print("Quantity:", self.quantity)

# Add Orders
# PromoCodes: XXAA15, EETT40, BOGO
# We can apply Promo Code only if Minimum Dishes are 3
# Validation of Correct Promo Code !!
# Suggest which promo code is better for you !!