import matplotlib.pyplot as plt

X = [1, 2, 3, 4, 5]

Y1 = [n for n in X]
Y2 = [n*n for n in X]
Y3 = [n*n*n for n in X]


# plt.plot(X, Y1, "y")
# plt.plot(X, Y2, "m")
# plt.plot(X, Y3, "b")

# plt.plot(X, Y1, "--")
# plt.plot(X, Y2, "-.")
# plt.plot(X, Y3, ":")

plt.plot(X, Y1, "o")
plt.plot(X, Y2, "^")
plt.plot(X, Y3, "D")

plt.show()


# Use CityTemps.csv and analyzed data on Graphs !!
# Please share analysis on graph in WhatsApp Group !!

