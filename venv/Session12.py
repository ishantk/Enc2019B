class Counter:

    # PROPERTY OF CLASS
    myCount = 1

    def __init__(self):
        # self.count -> PROPERTY OF OBJECT
        self.count = 1
        Counter.myCount = 1

    def incrementCount(self):
        self.count = self.count + 1
        Counter.myCount = Counter.myCount + 1

    def showCount(self):
        print("count is:",self.count,"and myCount is:",Counter.myCount)

c1 = Counter() # Object Construction
c2 = Counter() # Object Construction
c3 = c1        # Reference Copy | Not an Object Construction

c1.incrementCount()
c2.incrementCount()
c3.incrementCount()

c4 = Counter()


c1.showCount() # count is: 3 and myCount is: 101
c2.showCount() # count is: 2 and myCount is: 101
c3.showCount() # count is: 3 and myCount is: 101
c4.showCount() # count is: 1 and myCount is: 101