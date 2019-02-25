# Import Numpy Library
import numpy as np

#List Creation
numbers = [10, 20, 30, 40, 50]
print(numbers)
print(type(numbers))

print()

# arr1 = np.array([10, 20, 30, 40, 50])         # List as input
# arr1 = np.array((10, 20, 30, 40, 50))         # Tuple as input
# arr1 = np.array({10, 20, 30, 40, 50, 20})     # Set as Input
arr1 = np.array(numbers)
print(arr1)
print(type(arr1))

employees = {101:"John", 201:"Jennie", 301:"Jim"}
arr2 = np.array(employees)
print(arr2)
print(type(arr2))

