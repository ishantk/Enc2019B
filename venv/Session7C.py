name1 = "John Watson"
print("name1 is",name1)
print(type(name1))
print("Hex id of name1 is",hex(id(name1)))
# Strings are IMMUTABLE | They cannot be Changed or Modified
# Modification of a String results into a new String
# name1 = name1.upper()
name2 = name1.upper()

print("name1 is",name1)
print("name2 is",name2)

print("Hex id of name1 is",hex(id(name1)))
print("Hex id of name2 is",hex(id(name2)))

del name1
del name2

str1 = "Hello World"
str2 = "Hello World"

print(hex(id(str1)))
print(hex(id(str2)))

# if str1 == str2:
if str1 is str2:
    print("str1 == str2")
else:
    print("str1 != str2")

names = "John, Jennie, Jim, Jack, Joe"
length = len(names)
# print("Length of string names is",length)
print("Length of string names is",len(names))
print(names[0])
print(names[length-1])
print(names[-5])
# print(names[length]) # Error
print()

print(list(range(-1, -(length+1), -1)))

for i in range(-1, -(length+1), -1):
    print(names[i], end="")

print()
# newNames = names.split(" ")
newNames = names.split(",")
print(newNames)
print(type(newNames))

for n in newNames:
    print(n.strip())

print("==Slicing==")
# String Slicing
# names = "John, Jennie, Jim, Jack, Joe"
print(names[0 : 3])
print(names[3 : 6])
print(names[3 : ])
print(names[ : 5])

print("******")
print(names[-4 : ])
print("******")
print(names[ : -3])

modifiedNames = names.replace('J','K')
# modifiedNames = names.replace('Jo','Ka')
print(modifiedNames)

email = "john@example.com"
password = "john123345fdre"

fileName = "someSong.mp3"

if email.__contains__("@") and email.__contains__("."):
    print("Valid Email")
else:
    print("Enter a Valid Email")

if len(password) < 10:
    print("Enter a Valid Password")
else:
    print("Password is Correctly Entered")

if fileName.endswith(".mp3"): # We also have startsWith
    print("Its an Audio File")

name = input("Enter Your Name: ")
print(name)

data = "\u0905 {} is {} years old and lives in {} and earns \u20b9 30000".format(name, 30, "Redwood Shores")
print(data)

# Assignment: John -> Hindi