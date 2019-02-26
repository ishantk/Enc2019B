import numpy as np

arr = np.arange(10, 51, 3)
print("arr is:",arr)
print("type of arr is:",type(arr))
print("shape arr is:",arr.shape)
print("Size of arr is:",arr.shape[0])

# Access Elements
print(arr[1])
print(arr[-1])

# Slicing
print(arr[3:])
print(arr[:5])
print(arr[3:5])

slices = slice(1, 10, 2) # -> 1, 3, 5, 7, 9
print(slices)
print(type(slices))
print(arr[slices])

arr2D = np.array(([[1,2,3], [4,5,6], [7,8,9]]))
print(arr2D)
print(arr2D.shape)
print("arr2D size is:",arr2D.shape[0])

print(arr2D[0][1])

print(">>>>>><<<<<<")
print(arr2D[0:2])

print(">>>>>><<<<<<")
print(arr2D[0:2, 0:2])
# print(arr2D[0:2, 0:2, 0:2]) -> For 3-D Array

