import mysql.connector

# Model : which will hold data
class Customer:

    def __init__(self, cid, name, phone, age, address):
        self.cid = cid
        self.name = name
        self.phone = phone
        self.age = age
        self.address = address

    def showCustomer(self):
        print("==", self.cid, "|", self.name, "==")
        print("Name", self.name)
        print("Phone", self.phone)
        print("Age", self.age)
        print("Address", self.address)
        print("==============")

# DAO or Data Access Object : Used to perform DB Operations
# CRUD Operations -> Create Retrieve Update and Delete
class DBHelper:

    def saveCustomerInDB(self, cRef):
        sql = "insert into Customer values(null, '{}', '{}', {}, '{}', 10)".format(cRef.name, cRef.phone, cRef.age,
                                                                               cRef.address)
        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="Enc2019")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        print(">> Customer Saved")

    def updateCustomerInDB(self, cRef):
        sql = "update Customer set name = '{}', phone='{}', age={}, address = '{}' where cid = {}".format(cRef.name, cRef.phone, cRef.age,
                                                          cRef.address, cRef.cid)
        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="Enc2019")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        print(">> Customer Updated")

    def deleteCustomerFromDB(self, cid):
        sql = "delete from Customer where cid = {}".format(cid)
        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="Enc2019")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        print(">> Customer Deleted")

    def fetchCustomersFromDB(self):
        sql = "select * from Customer"
        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="Enc2019")
        cursor = con.cursor()
        cursor.execute(sql)

        """
        row = cursor.fetchone()
        print(">>",row)
        row = cursor.fetchone()
        print(">>", row)
        row = cursor.fetchone()
        print(">>", row)
        """

        rows = cursor.fetchall()
        # print(rows)
        # print(type(rows))
        for row in rows:
            # print(row)
            cRef = Customer(row[0], row[1], row[2], row[3], row[4])
            cRef.showCustomer()
            print()

# cRef1 = Customer(0, "Fionna", "+91 99999 77777", 22, "Country Homes")
# cRef1.showCustomer()

# cRef1 = Customer(3, "Fionna Flynn", "+91 88888 77777", 28, "Country Homes North")

# dbRef = DBHelper()
# dbRef.saveCustomerInDb(cRef1)
# dbRef.updateCustomerInDb(cRef1)

cRef1 = Customer(0, "Kia", "+91 88999 77777", 22, "Clover Homes")
cRef2 = Customer(5, "Kim Watson", "+91 99899 99777", 30, "Clover Heights")

# cRef1.showCustomer()
# cRef2.showCustomer()

dbHelper = DBHelper()
# dbHelper.saveCustomerInDB(cRef1)
# dbHelper.saveCustomerInDB(cRef2)

# dbHelper.updateCustomerInDB(cRef2)
# dbHelper.deleteCustomerFromDB(2)

# dbHelper.fetchCustomersFromDB()

# Phase-I
# ---------
# 1. You have to ask customer phone number
# 2. Enter Shopping Amount

# loyalty points + 10 percent of shopping amount
# update Customer.... where phone = '....'
# -------

# # Phase-II
# ----------
# If phone number is not in the table, we will ask customer about more details to add customer in db

# Phase-III
# ---------
# Redeem
# If shopping amount is greater than 500 we can redeem customer loyalty points
# We have to update table again and this time it shall be - operation
# We will ask customer how many point you wish to redeem ?
