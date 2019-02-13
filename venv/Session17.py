import mysql.connector

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

    def saveCustomerinDb(self):
        sql = "insert into Customer values(null, '{}', '{}', {}, '{}')".format(self.name, self.phone, self.age,
                                                                               self.address)
        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="Enc2019")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        print(">> Student Saved")

cRef1 = Customer(0, "Fionna", "+91 99999 77777", 22, "Country Homes")
cRef1.showCustomer()
cRef1.saveCustomerinDb()