"""
    A:1
    B:2
    .
    .
    Z:26

    Input: ABC
    1+2+3 = 6

    Hello = ?
    Awesome = ?
    Hello+Awesome =?
    Hello-Awesome =?
    Hello*Awesome =?
    Hello/Awesome =?

    string -> slicing/indexing
    name = "John"
    name[0] -> J
"""

alphabets = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9, "J":10, "K":11, "L":12}
word1 = input("Enter 1st Word").upper()
word2 = input("Enter 2nd Word").upper()

sum1 = 0
sum2 = 0

for ch in word1:
    sum1 = sum1 + alphabets[ch]

for ch in word2:
    sum2 = sum2 + alphabets[ch]

print("Sum1 is:",sum1)
print("Sum2 is:",sum2)

print("Add Operation:",sum1+sum2)
print("Subtract Operation:",sum1-sum2)
print("Multiply Operation:",sum1*sum2)
print("Divide Operation:",sum1//sum2)

"""
Further, Display the corresponding word 
eg: sum is: 32
    word will be CB
    
    if 0 -> SPACE
    if Negative -> Ignore -ve sign     
"""

