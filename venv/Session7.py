# What is main ??
# main is a thread !! Execution Context !!
# It will execute instructions in a sequence i.e. one after another !!
# 1st instruction -> Creating Container in Memory
# 2nd instruction -> Execution of Instruction

# By Default whatever code we write in .py file will be executed by main thread

a = 10  # J1
b = [10, 20, 30, 40, 50] # J2

print(a)    # J3
print(b)    # J4

sum = 0     # J5

for elm in b:   # J6
    sum = sum + elm  # execution
    print(elm)
