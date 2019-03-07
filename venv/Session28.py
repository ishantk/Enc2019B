import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/india/top-rated-indian-movies/"
response = requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")

# tags = soup.find_all("td",class_="titleColumn")
tags = soup.find_all("td",class_="ratingColumn")

movies = []

for tag in tags:
    data = tag.text
    print(data.strip())
    movies.append(data)
    print("---------")

print("=====")
print(movies)
print("=====")

# 1. Extract > Name, Year and Rating
# 2. Saving the same data in a csv file name, year, rating
# 3. India / USA
# 4. Draw Line Graphs for both countries and observe trend (Year VS Ratings)