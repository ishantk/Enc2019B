class Student:

    def __init__(self, roll, name, phone, email, std):
        self.roll = roll
        self.name = name
        self.phone = phone
        self.email = email
        self.std = std

    def showStudent(self):
        print("===",self.roll,"===")
        print(self.name,self.phone,self.email,self.std)
        print("=============")


# A list which is empty
students = []
reply = "yes"

while reply == "yes":

    print("Add Student Details")
    roll = int(input("Enter Roll Number: "))
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")
    std = int(input("Enter Standard: "))

    s = Student(roll,name,phone,email,std)

    students.append(s)

    reply = input("Would You like to add another Student ?")

    # s.showStudent()

    # print(reply is "yes")
    # print(reply == "yes")


# This should show data in ascending order of roll number or std as told by user
# What is Average std in school
# Check if phone number is correct or not i.e. it should be >=10 but less than 12
# +91 98765 56789
# Check id email is valid or not
# If even after 3 attempts phone number or email is not correctly written you terminate
for s in students:
    s.showStudent()