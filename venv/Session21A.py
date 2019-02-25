import numpy as np

a = [10, 20, 30, 40, 50]
arr1 = np.array(a)

print("arr1 is:",arr1)
print("arr1 shape:",arr1.shape) # 5,

b = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
arr2 = np.array(b)

print("arr2 is:",arr2)
print("arr2 shape:",arr2.shape) # 3,3

arr3 = np.array([[[10, 20, 30], [40, 50, 60], [70, 80, 90]], [[10, 20, 30], [40, 50, 60], [70, 80, 90]]])
print("arr3 is:",arr3)
print("arr3 shape:",arr3.shape) # 2,3,3

print(">>>>>>>>>")

arr4 = np.ones(8)
print(arr4)
print(arr4.shape)

arr5 = arr4.reshape(2, 2, 2)
print(arr4)
print(arr4.shape)

print(">>>>>>>>>")

print(arr5)
print(arr5.shape)

print(">>>>>>>>>")

arr6 = arr5.ravel()
print(arr6)
print(arr6.shape)

# Assignment :
# > 1. Ask User about 4by4 Chess Board or 8by8 Chess Board
"""
    0   0   0   0
    0   0   0   0   
    0   0   0   0
    0   0   0   0
    
# > 2. Place the Queen by replacing 0 with 1    
    1   0   0   0
    0   1   0   0
    0   0   0   1
    1   0   0   0
    
"""

# > 3. Any row must have only 1 Queen
# > 4. No 2 Queens can come in 1 Column
# > 5. No 2 Queens can come in Diagonal (Left and Right)