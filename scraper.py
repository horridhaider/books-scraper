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

try:
    for page in range(1,101):   # Scraping 10 pages (running a loop through maximum pages)
        url = f"https://books.toscrape.com/catalogue/page-{page}.html"     # urls for each page
        response = requests.get(url, headers=headers)    # the actual request that obtains the content from that webpage
        response.encoding = "utf-8"     # sets the encoding for windoes to read special symbols easily

        # By doing this, loop will stop if the pages do not exist further
        if response.status_code != 200:
            print(f"Pages Ended! No Pages after Page {page-1}")
            break
        
        # Parsing the html
        soup = BeautifulSoup(response.text, "lxml")
        
        # 1. Targetting the 'article' tag
        books = soup.find_all("article", class_= "product_pod")

        for book in books:
            # Gets titles and prices of the books
            title = book.h3.a.get("title")
            price = book.find("p", class_="price_color").text
            price = float(price.replace("£", ""))       # this removes the currency symbol so that it's easier to analyze data in future

            # Gets the rating (Eg. Three)
            rating = book.find("p", class_="star-rating")["class"][1]

            # Gets stock availability with whitespace cleanup
            stock = book.find("p", class_="instock availability").text.strip()
            
            # Gets the URL of the books and create clickable links
            url = book.h3.a.get('href')
            full_url = urljoin("https://books.toscrape.com/catalogue/", url)
            
            # Append data as a dictionary to our list
            all_books.append({
                "Title": title,
                "Price": price,
                "Rating": rating,
                "Stock": stock,
                "URL": full_url
            })

        time.sleep(1)       # prevents sudden load of requests

    # Create a DataFrame using Pandas
    df = pd.DataFrame(all_books)

    # Export to csv (index=False prevents extra row numbers)
    df.to_csv("books_dataset.csv", index=False, encoding="utf-8-sig")
    df.to_json("books_dataset.json", index=False)
    print("Successfully Exported as .csv and .json!")
    print(df.head())    # displays some initital books data

except Exception as e:      # in case any exception occurs, an error message will display
    print("An Error has occured!", e)