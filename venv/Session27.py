import requests
from bs4 import BeautifulSoup

url = "https://twitter.com/dna"
# url = "https://www.ndtv.com/"
response = requests.get(url)
# print(response.text)

# HTML Parsing i.e. Web Scrapping
soup = BeautifulSoup(response.text, "html.parser")
print("Type of soup is:",type(soup))
print("*************")
# print(soup)
# print(soup.prettify())

print("Fetching Title of Page")
print(soup.title.text)
print("*************")

print()

"""
children = soup.children
for child in children:
    print(child)
    print(">>>>>>>>>>>")
"""

"""
pTags = soup.find_all("p")
for tag in pTags:
    print(tag)
    print(">>>>>><<<<<<")
"""

# divTags = soup.find_all("div")
divTags = soup.find_all("div", class_="js-tweet-text-container")
for tag in divTags:
    # print(tag)
    print(tag.text)
    print(">>>>>><<<<<<")

# Class Assignment : Extract Data from NDTV
# Home Assignment  : Extract Data from CricBuzz
#                    Create a dataset i.e. a .csv file for Indian Team and Australian Team