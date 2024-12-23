import csv
import requests
from bs4 import BeautifulSoup

url = "https://www.yahoo.co.jp/"
res = requests.get(url)

soup = BeautifulSoup(res.content, "html.parser")
print(soup.text)

topics = soup.find(id = "Topics")
print(topics.text)

with open("info.csv", "w", newline="", encoding="utf_8") as f:
    writer = csv.writer(f)
    for elem in topics.find_all("a"):
        writer.writerow([elem.text, elem.get("href")])
