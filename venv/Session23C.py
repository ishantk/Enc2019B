import pandas as pd

nums1 = [10, 20, 30, 40, 50]
nums2 = [11, 22, 33, 44, 55]

emp1 = {"eid":101, "name":"john", "salary":30000}
emp2 = {"eid":201, "name":"sia", "salary":40000}

employees = [
    {"eid":101, "name":"Mike", "salary":40000},
    {"eid":201, "name":"Leo", "salary":50000},
    {"eid":301, "name":"Fionna", "salary":60000}
]

print(nums1)
print(emp1)
print(employees)

# Create a DataFreame
df1 = pd.DataFrame([nums1,nums2])
df2 = pd.DataFrame([emp1,emp2])

print()
print(df1)
print()
print(df2)

print()

df3 = pd.DataFrame(employees)
print(df3)

print()

print(df3["eid"])
print(df3["eid"][1])