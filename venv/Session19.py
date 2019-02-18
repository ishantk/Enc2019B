import os

"""
path = os.getcwd()
print("CWD is:",path)

os.chdir("/Users/ishantkumar/Downloads")

path = os.getcwd()
print("CWD now is:",path)

os.mkdir("/Users/ishantkumar/Downloads/PythonToday")
print("Directory Created")

"""

"""
# Change the Path First !!
os.chdir("/Users/ishantkumar/Downloads")
os.rmdir("/Users/ishantkumar/Downloads/PythonToday")
print("Directory Removed")
"""

"""
print("OS Name:",os.name)
print("User:",os.getlogin())
print("Process ID:",os.getppid())
"""

"""
path = os.path.join("/Users/ishantkumar/Downloads","CPP2018Batch")
print("path is:",path)

newPath = os.path.split(path)
print("newPath is:",newPath)
"""

"""
path = os.getcwd()
print("path is:",path)

newPath = os.path.split(path)
print("newPath is:",newPath)
"""

"""
path = os.path.join("/Users/ishantkumar/Downloads","students2019.json")
print("path is:",path)
print("Is path Existing?:",os.path.exists(path))
print("Is it a Directory?:",os.path.isdir(path))
print("Is it a File?:",os.path.isfile(path))
"""

path = "/Users/ishantkumar/Downloads"
if os.path.isdir(path):
    files = os.walk(path)
    allFiles = list(files)
    # print(allFiles)
    for f in allFiles:
        print(f)

# Assignment1:  List all the images in your computer !!
#               Along with image name, also print the size of image file !!
#               Print Date Time Stamp of Image File when it was create on your system !!
#               Images which are 2 years older from now, suggest user to take backup in some Cloud Storage !!

# Assignment2:  List all the files in the system which user has not used from last 1 year
#               Ask him/her to delete files ?? If yes!! Delete them !!

# Step towards creation of Anti-Virus !!
# Assignment3:  Detect the Virus Files (extensions) and Delete them !!

