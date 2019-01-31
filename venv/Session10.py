# Single value Container

# String is IMMUTABLE
name = "John"
name = "Sia"
print(type(name))
print(name)

# Multi Value Container
# LIST is MUTABLE
# Mutable -> We can modify the data

# Homogeneous
names = ["John", "Jennie", "Jim", "Jack", "Joe"]
print(type(names))
print(len(names))
print(names[0])

names[1] = "Sia"
print(names)

# Hetrogeneous
myList = [10, 12.5, "Kim", "This is Awesome"]
print(names)
print(myList)

print(names[2])
print(myList[3])

# Lets Slice List
print(names[2 : 4])
print(names[0 : ])

print(names[ : -2]) #
print(names[-2 : ]) #
print(names[-4 : -2])

# Add Data in List
names.append("Harry") # Append a Value
names.append("George")
names.append("Leo")

print(names)

# Iterate in List
# for i in range(0, len(names)):
#     print(names[i])

for n in names:
    print(n)

newNames = ["Bob", "Charlie"]
names.extend(newNames) # Append a List in other List

print(names)

