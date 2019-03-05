import requests
import json

# Read a Web Page
# response = requests.get("https://twitter.com/dna")
# url = "http://www.json-generator.com/api/json/get/chQLxhBjaW?indent=2"
cityName = "Ludhiana"
url = "https://openweathermap.org/data/2.5/weather?q={}&appid=b6907d289e10d714a6e88b30761fae22".format(cityName)
response = requests.get(url)
# response = requests.get(url, verify=False) Do not check SSL Certificate
print(response.text)

print()

"""
data = json.loads(response.text)
print(data["bookstore"])
print(data["bookstore"][1]["name"])
"""

data = json.loads(response.text)
#1 Please Show Weather Information of Ludhiana below:
#2 Parse News : https://newsapi.org/