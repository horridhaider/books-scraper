# Books Scraper

## Description
This project scrapes book data from [books.toscrape.com](https://books.toscrape.com/), including titles, prices, ratings, stock availability, and book URLs. It demonstrates web scraping, data collection, and structured dataset creation using Python.

## Tools & Libraries
- Python 3
- requests
- BeautifulSoup4
- pandas
- urllib.parse (urljoin)

## Features
- Handles pagination across multiple pages
- Extracts book metadata (title, price, rating, stock, URL)
- Converts prices to numeric for analysis
- Outputs structured CSV and JSON datasets

## How to run
1. Install required libraries:
   ```bash
   pip install requests beautifulsoup4 pandas lxml

2. Run the scraper:
    ```bash
    python scraper.py

3. Check the generated Scraped Data.csv and Scraped Data.json

## Sample Output
				
			

| Title | Price | Rating | Stock | URL |
| -------------------- | ----- | ----- | -------- | ------------------------------------------------------------------------------------------- |
| A Light in the Attic | 51.77 |    3 | In stock | [https://books.toscrape.com/](https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html) |

## Notes

- Delay added between pages to avoid overloading the server

- Designed for learning and portfolio purposes
