import threading
import time

# Thread Synchronization :
# We need it when multiple threads have to access the same object

# Create a Lock Object
lock = threading.Lock()

class Printer:
    def printDocuments(self, name, copies):

        lock.acquire()

        for i in range(1, copies+1):
            time.sleep(.5)
            print(name,"Printed",i,"times")

        lock.release()


class ComputerA(threading.Thread):

    def __init__(self, printer):
        threading.Thread.__init__(self)
        self.printer = printer # Reference Copy

    def run(self):
        self.printer.printDocuments("** PythonAssignment1.pdf",10)



class ComputerB(threading.Thread):

    def __init__(self, printer):
        threading.Thread.__init__(self)
        self.printer = printer # Reference Copy

    def run(self):
        self.printer.printDocuments("## JohnsProfile.pdf",10)


print("==App Started==")
pRef = Printer() # one printer object
# pRef.printDocuments("JohnsProfile.pdf",10)

# Now we have a use case where multiple computers will be accessing the same Printer Object
caRef = ComputerA(pRef)
cbRef = ComputerB(pRef)

caRef.start()
cbRef.start()

print("==App Finished==")
