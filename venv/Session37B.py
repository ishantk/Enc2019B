import threading
import time
"""
class MyTask:
    def executeTask(self):
        for i in range(1, 11):
            print("** MyTask **",i)
"""
# IS-A Relation MyTask is a Thread
class MyTask(threading.Thread):
    def run(self):
        for i in range(1, 11):
            time.sleep(1)
            print("** MyTask **",i)

# main thread will execute the below jobs in a sequence
# when we will run our python module as application

# Job 1
print("==App Started==")

# Job 2
mRef = MyTask()

# Job 3
# mRef.executeTask()
mRef.start()

#Job 4
for i in range(1, 11):
    time.sleep(2)
    print("== Main ==", i)

# Job 5
print("==App Finished==")
