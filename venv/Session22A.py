import numpy as np

# Read numpy data from file
arr = np.loadtxt("data.txt")
print(arr)
print(type(arr))
print(arr.shape)
print(arr.ndim)

# How we can create a 3-D Array in File and Load it in numpy !!

print("============")

# Write numpy data in file
arr = np.arange(10, 200, 10)
print(arr)
print(arr.shape)
print(arr.ndim)
np.savetxt("data1.txt", arr)
print("==Data Writen==")

# How we can create a 3-D Array using numpy and save it in file !!
# Why is data stored as exponents and how can we save it as decimals !! -> StackOverflow !!

# Continuation:
# n-Queen Problem
# Read ChessBoard from File
# Write Position of Queens in txt file using numpy !!