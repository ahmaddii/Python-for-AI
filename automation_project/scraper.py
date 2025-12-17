# scraper.py
import requests
import csv
from bs4 import BeautifulSoup
from config import SCRAPE_URL, RAW_DATA_FILE
from fileHandler import log_info, log_error

def scrape_quotes():
    try:
        response = requests.get(SCRAPE_URL, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.find_all("span", class_="text")

        with open(RAW_DATA_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["quote"])

            for q in quotes:
                writer.writerow([q.text])

        log_info(f"Scraped {len(quotes)} quotes")
        return [q.text for q in quotes]

    except Exception as e:
        log_error(f"Scraping failed: {e}")
        return []
