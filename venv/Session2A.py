# Operators in Python

# Arithmetic Operators :
a = 10
b = 3
c = a + b
d = a - b
e = a * b
f = a / b
g = a % b
h = a // b
i = 2 ** 5 # 2 pow 5

print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)

# Conditional Operators
# >, <, >=, <=, ==, !=

age = 2
gender = "M"
print(age > 18)
print(gender == """M""")

# Logical Operators
# and or not
print(age>18 and gender=="M")
print(age>18 or gender=="M")

# Bitwise Operators
# &, |, ^
# num1 = 8            # 1 0 0 0
# num2 = 10           # 1 0 1 0

num1 = 7            # 0 1 1 1
num2 = 11           # 1 0 1 1

num3 = num1 & num2  # 1 0 0 0

num4 = num1 | num2  # 1 0 1 0

num5 = num1 ^ num2  # 0 0 1 0

print(num3)
# print(bin(num3))
print(num4)

print(num5)

# Shift Operators

# Right Shifting -> Divide by 2 pow num
# x = 12          # 1 1 0 0
x = 15            # 1 1 0 1
y = 5
z = x >> y        # 1 1 0 0 >> 2 -> _ _ 1 1 -> 0 0 1 1
print("z is",z)

# Left Shift ->  Multiply by 2 pow num
p = x << y      # 0 0 0 0 1 1 0 1 << 3  -> 0 1 1 0 1 0 0 0
print("p is",p)

# 1024 512 256 128 64 32 16 8 4 2 1

a1 = 12
a2 = a1 >> 2
a3 = a2 << 2

print(a1)
print(a2)
print(a3)

num = -13                # 0 0 0 0 1 0 1 1
result = num >> 2        # 0 0 0 0 0 0 1 0

# 11    -> 1 0 1 1
# -11   -> 0 1 0 0
#                1
#          0 1 0 1 -> -11

#          _ _ 0 1

#          1 1 0 1
#          0 0 1 0
#                1
#          0 0 1 1 -> -3

print("Result is",result)

# -2, -5, -4, -8, 0

a1 = 10
a2 = 10

print(a1 is a2)
print(a1 is not a2)

# Program -> 345 -> 3+4+5 -> 12 | 111 -> 1+1+1 -> 3 | 876 -> 8+7+6 = 21 |


