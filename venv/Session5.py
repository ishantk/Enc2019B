num = 21

def show(num):
    num = num * 3
    print("num is:",num)


# main thread will perform executions and storage of data
x = 10

# Line  #1, 3 and 9 are created in memory
# Line # 13, 14, 15 and 16 are executions
show(x) # Execution of show will create its own frame in the memory
print("show is:",show)
print("x is:",x)
print("num is:",num)