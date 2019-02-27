import pandas as pd
import numpy as np

# List
numbers = [10, 20, 30, 40, 50]
print(numbers)

print()

# Numpy Array
arr = np.array([10, 20, 30, 40, 50])
print(arr)

print()

# Pandas Series
series1 = pd.Series([10, 20, 30, 40, 50])
print(series1)

# Create Series from List
series2 = pd.Series(numbers)
print(series2)

# Create Series from Numpy Array
series3 = pd.Series(arr)
print(series3)