import requests
import threading # we shall be able to create concurrent/asynchronous programming
                 # we can make several tasks to run parallely

url = "http://www.json-generator.com/api/json/get/chQLxhBjaW?indent=2"

# This method will fetch data from web service.
# This can take time !! Because its an Internet based operation !!
# As well we cna have tasks which can take more time !!
def getDataFromWebService():
    response = requests.get(url)
    print(">> Response:",response.text)

    jsonResponse = response.json()
    books = jsonResponse["bookstore"]

    for book in books:
        print(">> ",book["name"])

# Inheritance or IS-A Relation
class BookFetchTask(threading.Thread):

    def run(self):
        response = requests.get(url)
        print(">> Response:", response.text)

        jsonResponse = response.json()
        books = jsonResponse["bookstore"]

        for book in books:
            print(">> ", book["name"])


print(">> App Started")

# getDataFromWebService()
task = BookFetchTask()
task.start() # internally execute run method

# Below written code will be blocked
# App is in a hang state (Due to Long Running Operations)

for i in range(1,11):
    print(">> i is:",i)

print(">> App Finished")

