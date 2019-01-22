num = int(input("Enter a Number: "))
# Print Table of a Number
i = 1
print(num,i,"'s are",(num*i))
i = i + 1
print(num,i,"'s are",(num*i))
i = i + 1
print(num,i,"'s are",(num*i))
i = i + 1
print(num,i,"'s are",(num*i))
i = i + 1
print(num,i,"'s are",(num*i))
i = i + 1
print(num,i,"'s are",(num*i))
i = i + 1
print(num,i,"'s are",(num*i))
i = i + 1
print(num,i,"'s are",(num*i))
i = i + 1
print(num,i,"'s are",(num*i))
i = i + 1
print(num,i,"'s are",(num*i))

# Iteration is doing some job again and again
# Loops : while and for loop

print()
print("===============")
num = int(input("Enter a Number: "))
i = 1

while i<=10:
    print(num, i, "'s are", (num * i))
    i = i + 2

print()
print("===============")
num = int(input("Enter a Number: "))

# range gives us a range of numbers
# range(starting point, ending point+1, step) # By default step is 1
# for i in range(1, 11):
# for i in range(1, 11, 1):
for i in range(1, 11, 2):
    print(num, i, "'s are", (num * i))



