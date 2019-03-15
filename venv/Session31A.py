import pandas as pd
from scipy import stats

data = pd.read_csv("advertising.csv")
# print(data)
# print(data["TV"])
# print(data["TV"].values)
# print(data["Sales"].values)

X = data["TV"].values
Y = data["Sales"].values

# print(X)
# print(Y)

##############
data = stats.linregress(X, Y)
# print(data[0]) # b1
# print(data[1]) # b0

b0 = data[1]
b1 = data[0]

# Y = b0 + b1X

Y1 = []

for x in X:
    y = b0 + (b1*x)
    Y1.append(y)

print(Y1)

# Proceed Below