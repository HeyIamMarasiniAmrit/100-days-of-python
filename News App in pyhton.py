import requests
import json
query = input("What type of news are you interested in?")
url = f"https://newsapi.org/v2/everything?q={query}&from=2023-02-18&sortBy=publishedAt&apiKey=79309cc134474dd38c17e92111d05004"
r = requests.get(url)
news = json.loads(r.text)
# print(news, type(news))
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("----------------------------------------------")