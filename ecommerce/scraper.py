import requests
from bs4 import BeautifulSoup
import csv
import re

url = "https://books.toscrape.com/catalogue/page-1.html"

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
books = soup.find_all("article", class_="product_pod")

rows = []

for book in books:
    title = book.h3.a.get("title", "").strip()

    raw_price = book.find("p", class_="price_color").text
    price = re.sub(r"[^\d.]", "", raw_price)

    rating = book.find("p", class_="star-rating")["class"][1]

    availability = book.find(
        "p", class_="instock availability"
    ).text.strip()

    rows.append([title, price, rating, availability])

print(f"Total records scraped: {len(rows)}")

# ✅ WRITE CSV WITHOUT PANDAS (NO ERRORS POSSIBLE)
with open("books_data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Price", "Rating", "Availability"])
    writer.writerows(rows)

print("✅ CSV file created successfully: books_data.csv")
