# In python every .py files is called a module
# We can import a module in another module using import statement

"""
import Session20B
Session20B.sysDemo()
Session20B.show()
"""

"""
import Session20B as s20    #Alias
s20.sysDemo()
s20.show()
"""

"""
from Session20B import *
sysDemo()
show()
"""

"""
from Session20B import sysDemo
sysDemo()
# show() -> this isn't imported
"""

from mypack import one
from mypack import two

one.hello()
two.bye()


# Assignment : Try exploring what can work with mypack as in above import statements