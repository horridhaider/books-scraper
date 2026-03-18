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
