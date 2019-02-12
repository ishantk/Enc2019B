file = open("Session16A.py","r")
data = file.read(15)
print(type(data))        # str
print(data)              # 1st 15 characters

data = file.read(10)     # next 10 characters after 15 characters
print(data)

file.close()             # Shall close the opened file and release memory resources
print("Is file closed?",file.closed)