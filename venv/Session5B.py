a = 10
b = a   # Value Copy

x = [10, 20, 30, 40, 50]
y = x   # Reference Copy

b = 21
x[1] = 111

print(a)      # 10
print(y[1])   #
