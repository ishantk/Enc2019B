class Parent:
    def showVehcile(self):
        print("Vehicle is Maruti Swift")

class Child(Parent): # Child(Parent) -> Linking (IS-A)
    def showVehcile(self):
        print("Vehicle is Honda City")


print(Parent.__dict__)
print(Child.__dict__)

ch = Child()
ch.showVehcile()

print(ch.__dict__)