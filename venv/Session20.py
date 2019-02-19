import json

# Dictionary !!
employee = {"eid":101, "name":"John Watson", "age":30, "salary":50000}
print(employee)
print(type(employee))

print()

# Role of dumps is to get dictionary data structure as string/text
jsonData = json.dumps(employee)
print(jsonData)
print(type(jsonData))

print()

# Role of loads is to get string/text data and convert it to dictionary structure
emp = json.loads(jsonData)
print(emp)
print(type(emp))