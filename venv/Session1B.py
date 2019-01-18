# Single Value Container
a = 10
print("a is",a,"type of a is",type(a))

# Multi Value Container

# TUPLE
# Homogeneous
b = 10, 20, 30, 40, 50
print("b is",b,"type of b is",type(b))

# Hetrogeneous
c = 10, 'A', 2.2, "John", 30
print("c is",c,"type of c is",type(c))

d = (10, 20, 30, 40, 50) # d = 10, 20, 30, 40, 50 | One and the same thing
print("d is",d,"type of b is",type(d))

print("HashCode of b is",id(b))
print("HashCode of d is",id(d))

# LIST
e = [10, 20, 30, 40, 50]
f = [10, 20, 30, 40, 50]
g = [10, 'A', 2.2, "John", 30] # Hetrogeneous

print("e is",e,"type of e is",type(e))
print("f is",f,"type of f is",type(f))

print("HashCode of e is",id(e))
print("HashCode of f is",id(f))

# SET
h = {10, 20, 30, 40, 50}
i = {10, 20, 30, 40, 50}
j = {10, 'A', 2.2, "John", 30} # Hetrogeneous

print("h is",h,"type of h is",type(h))
print("i is",i,"type of i is",type(i))
print("j is",j,"type of j is",type(j))

print("HashCode of h is",id(h))
print("HashCode of i is",id(i))

# Multi Value Container : DICTIONARY
myStudents = {101:"John", 201:"Jennie", 301:"Jack", 401:"Jim", 501:"Joe"}
yourStudents = {101:"John", 201:"Jennie", 301:"Jack", 401:"Jim", 501:"Joe"}

print("myStudents is",myStudents,"type of myStudents is",type(myStudents))
print("yourStudents is",yourStudents,"type of yourStudents is",type(yourStudents))

print("HashCode of myStudents is",id(myStudents))
print("HashCode of yourStudents is",id(yourStudents))

# Conclusion: For SVC if data is same in 2 different containers, HashCode will be same
#             For MVC even if data is same in 2 different containers, hash code will be different