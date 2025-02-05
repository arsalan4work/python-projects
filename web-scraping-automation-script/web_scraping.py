import requests
from bs4 import BeautifulSoup
import csv
import time

# Base URL of the website
base_url = "https://books.toscrape.com/catalogue/category/books/science_22/"

# File to store the scraped data
csv_file = "books_data.csv"

# headers for CSV
headers = ["Title", "Price", "Rating"]

def fetch_and_get_data(url):
    # Scrape book details from a single page
    try:
        response = requests.get(url, timeout=10)  # Fetch the webpage
        response.raise_for_status()  # Raise an error if request fails
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")
    
    data = []
    for book in books:
        try:
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text
            rating = book.p["class"][1]  # Extracts rating (e.g., "Three", "Five")

            data.append([title, price, rating])
        except AttributeError:
            print("Error extracting book details")
    
    return data

def get_all_books():
    # Scrape multiple pages
    all_books = []
    page_num = 1

    while True:
        url = base_url + f"page-{page_num}.html" if page_num > 1 else base_url + "index.html"
        print(f"Scraping page {page_num}...")

        books = fetch_and_get_data(url)
        if not books:
            print("No more pages found.")
            break  # Stop when no more books are found

        all_books.extend(books)
        page_num += 1

    return all_books

def save_to_csv(data):
    # Save book data to a CSV file
    with open(csv_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)  # Write header row
        writer.writerows(data)  # Write book data
    
    print(f"Data saved to {csv_file} successfully!")

if __name__ == "__main__":
    books_data = get_all_books()
    if books_data:
        save_to_csv(books_data)
    else:
        print("No data scraped. Please check the website structure.")
