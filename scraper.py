import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin
import time

# An empty list to contain all the book data
all_books = []

headers = {                 # headers mimic real browser
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36"
        }

def scrape_pages(url):
        response = requests.get(url, headers=headers)    # the actual request that obtains the content from that webpage
        response.encoding = "utf-8"     # sets the encoding for windoes to read special symbols easily
        if response.status_code != 200:
             return None
        return response

def extract_books(response):
    # Parsing the html
    soup = BeautifulSoup(response.text, "lxml")
        
    # 1. Targetting the 'article' tag
    books = soup.find_all("article", class_= "product_pod")

    # Making an empty list for data to be filled in later
    page_books = []
    rating_map = {"One":1, "Two":2, "Three":3, "Four":4, "Five":5}      # Gives a map for converting ratings into numerical forms

    for book in books:
        try:
            # Gets titles and prices of the books
            title = book.h3.a.get("title")
            price = book.find("p", class_="price_color").text
            price = float(price.replace("£", ""))       # this removes the currency symbol so that it's easier to analyze data in future

            # Gets the rating (Eg. Three)
            rating = rating_map[book.find("p", class_="star-rating")["class"][1]]

            # Gets stock availability with whitespace cleanup
            stock = book.find("p", class_="instock availability").text.strip()
                    
            # Gets the URL of the books and create clickable links
            url = book.h3.a.get('href')
            full_url = urljoin("https://books.toscrape.com/catalogue/", url)

            # Append data as a dictionary to our list
            page_books.append({
                "Title": title,
                "Price": price,
                "Rating": rating,
                "Stock": stock,
                "URL": full_url
            })
        except AttributeError:
            print("Skipping a book — missing field")
            continue

    return page_books

# This Saves the Data using pandas, into CSV and JSON
def save_data(all_books):
    df = pd.DataFrame(all_books)
    df.to_csv("books_dataset.csv", index=False, encoding="utf-8-sig")
    df.to_json("books_dataset.json", index=False)
    print("Successfully Exported as .csv and .json!")
    print(df.head())    # displays some initital books data

try:
    for page in range(1,51):   # Scraping 50 pages
            url = f"https://books.toscrape.com/catalogue/page-{page}.html"     # urls for each page
            response = scrape_pages(url)
            if response is None:
                break
            books = extract_books(response)
            all_books.extend(books)
            time.sleep(1)       # prevents sudden load of requests

except requests.ConnectionError:
    print("No internet / couldn't reach site")
except requests.Timeout:
    print("Request timed out")
except requests.HTTPError:
    print("HTTP error occurred")

#  if an exception fires before save_data(), you lose all collected data. A finally clause can save whatever was collected up to that point
finally:
    if all_books:
        save_data(all_books)