class Student:
    # self is a ref variable which points to object
    # roll, name and age as input to constructor is property of constructor
    def __init__(self, roll, name, age):
        self.roll = roll    # public
        self._name = name   # protected
        self.__age = age    # private -> Name Mangling

    def showStudentDetails(self):
        print("{} belongs to {} and is {} years old".format(self.roll,self._name,self.__age))

    def _hello(self):
        print("This is hello")

    def __bye(self): # -> Name Mangling -> _Student__bye()
        print("This is bye")


s1 = Student(101, "John", 30)
# s1.showStudentDetails() // -> Student.showStudentDetails(s1)
Student.showStudentDetails(s1)

print(s1.roll)
# We can access _name which is protected. We can perform write as well as read operation\\
# But it is not recommended !!
print(s1._name)
s1._name = "John Watson"
s1.showStudentDetails()

print(s1.__dict__)
# print(s1.__age) -> error because name has been mangled
print(s1._Student__age)

s1._hello() # -> Student._hello(s1)
Student._hello(s1)

print(Student.__dict__)

# s1.__bye()
s1._Student__bye() # Student._Student__bye(s1)
Student._Student__bye(s1)

