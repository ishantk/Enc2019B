file = open("Session16.py","r")
# line = file.readline()
# print(line)

"""
    readline() reads a single line from file
    re-executing readLine() will read the next line
"""

lines = file.readlines()
print(type(lines)) # lines -> is a list of lines
print(lines)

for line in lines:
    print(line)