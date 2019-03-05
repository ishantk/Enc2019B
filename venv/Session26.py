import requests
import json

# Read a Web Page
# response = requests.get("https://twitter.com/dna")
url = "http://www.json-generator.com/api/json/get/chQLxhBjaW?indent=2"
response = requests.get(url)
print(response.text)

print()

data = json.loads(response.text)
print(data["bookstore"])
print(data["bookstore"][1]["name"])