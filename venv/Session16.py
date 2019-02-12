# File Handling
# Write and Read in Files !!

file = open("Session15D.py","r")
print(type(file))

fileContents = file.read() # read() -> reads all the contents from file
print(type(fileContents))  # str
print(fileContents)

# Re-Read the File !!
fileContents = file.read()
print("====")
print(fileContents) # Nothing to show
# Once a file is read, it will not be re-read

"""
    1. open the file
    2. read the file
    3. once read, we cannot read it again

"""