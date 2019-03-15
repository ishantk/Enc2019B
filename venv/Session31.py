import matplotlib.pyplot as plt
from scipy import stats

X = [1, 2, 3, 4, 5]
Y = [2, 4, 5, 4, 5]

"""
Equation of Line:
Y = b0 + b1X
We need to find value of b0 and b1

Y = 2.2 + (0.6)X

"""

data = stats.linregress(X, Y)

print("b1 is:",data[0]) # b1
print("b0 is:",data[1]) # b0

plt.xlabel('X') # Independent Variable
plt.ylabel('Y') # Dependent Variable
plt.grid(True)
# plt.plot(X, Y)
plt.plot(X, Y, "o")
plt.show()