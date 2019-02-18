# import datetime
import datetime as dt


# today = datetime.datetime.today()
# print(today)
today = dt.datetime.today()
print(today)

tomorrow = dt.datetime(2019, 2, 19, 12, 12, 12, 234)
print(tomorrow)

howMany = tomorrow - today
print(howMany)