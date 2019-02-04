class Student:

    schoolName = "NA"

    def __init__(self, roll, name):
        self.roll = roll
        self.name = name

    def showStudent(self):
        print(self.roll,"belongs to",self.name,"and studies in",self.schoolName)

Student.schoolName = "ABC International"

# Property of Class can be accessed by Property of Object (Read Only)
# Property of Object cannot be accessed by Property of Class



s1 = Student(101,"John")
s2 = Student(201,"Jennie")

s1.schoolName = "XYZ International"

s1.showStudent()
s2.showStudent()

print(s1.__dict__)
print(s2.__dict__)
print(Student.__dict__)

# OOPS Assignment
# Create a Program for WhatsApp Status and Group Title