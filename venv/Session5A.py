
x = 10

def fun():
    # x = 20 -> creating another container x in frame of fun
    global x
    x = 21 # -> use x of main
    print("x is:",x)

fun()
print("x is:", x)