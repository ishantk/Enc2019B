import numpy as np
arr = np.genfromtxt("CityTemps.csv", delimiter=",")
print(arr)

print(arr.shape)
print(arr.ndim)

print(arr[1][2])

np.savetxt("CityTemps1.csv", arr, delimiter=",")
print(">> File Created")

# Data Analysis
# Using numpy read CityTemps.csv and tell which city is the coldest and which city is the hottest
# Determine Hottest and Coldest City for 2014 and 2015 separately !!