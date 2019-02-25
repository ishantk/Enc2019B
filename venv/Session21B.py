import numpy as np

arr1 = np.arange(10, 31)
print("arr1 is:",arr1)

arr2 = np.arange(10, 31, 3)
print("arr2 is:",arr2)

# arr3 = np.zeros((3,3))
arr3 = np.ones((3,3))
print("arr3 is:",arr3)

arr3[0][2] = 1
print(arr3[0][2])
print(arr3)

print(">>>>>>>")

arr4 = np.linspace(0, 21, 4)
print(arr4)

print(">>>>>>>")

numbers = [11, 22, 33, 44, 55]
arr5 = np.asarray(numbers)

print(arr5)
print(type(arr5))