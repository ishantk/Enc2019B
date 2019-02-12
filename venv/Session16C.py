file = open("mystudents.xml","r")
data = file.readlines()
for line in data:
    print(line)

file.close()

"""
file = open("/Users/ishantkumar/Downloads/logo.png","r")
data = file.read()
print(data)
"""
