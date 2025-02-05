# Web Scraper for Books.toscrape.com

## Project Overview
This project is a Python-based web scraper that automates the extraction of book details from the Science category on [Books.toscrape.com](https://books.toscrape.com/). The script fetches book titles, prices, and ratings and stores them in a CSV file for further analysis.

## Features
- **Automated Web Scraping**: Extracts book details from simgle page.
- **Data Storage**: Saves the extracted data into a CSV file.
- **Error Handling**: Includes try/except blocks to manage network issues and HTML structure changes.
- **Modular Design**: Functions are divided into separate tasks for maintainability.
- **Graceful Failure**: Provides meaningful error messages and avoids crashes.

## Project Structure
```
web_scraper/
│-- web_scraping.py    # Main script to run the scraper
│-- README.md          # Documentation
│-- books_data.csv     # Output file containing scraped data
```

## Installation
### Prerequisites
Ensure you have Python installed (Python 3.7+ recommended). If not, download and install it from [python.org](https://www.python.org/downloads/).

### Step 1: Clone the Repository
```sh
 git clone
 cd web_scraper
```

### Step 2: Install Dependencies
```sh
pip install request beautifulsoup4
```

### Step 3: Run the Script
```sh
python web_scraping.py
```

## Dependencies
The script requires the following Python libraries:
- `requests` (for making HTTP requests)
- `beautifulsoup4` (for parsing HTML)
- `csv` (for saving data to CSV)

To install them, run:
```sh
pip install requests beautifulsoup4
```

## How It Works
1. The script starts scraping from the **Science category** page.
2. It iterates through all available pages and extracts:
   - **Title** of the book
   - **Price** in GBP
   - **Rating** (e.g., One, Two, Three stars)
3. It saves the extracted data into `books_data.csv`.

## Code Breakdown
- **`fetch_and_get_data(url)`**: Fetches and extracts book details from a given page.
- **`get_all_books()`**: Iterates through multiple pages until no more books are found.
- **`save_to_csv(data)`**: Writes the scraped data into a CSV file.

## Error Handling & Edge Cases
- Handles network errors with `try/except` blocks.
- Deals with unexpected changes in HTML structure.
- Stops scraping when no more pages are found.

## Example Output (books_data.csv)
```
Title,Price,Rating
"The Science Book","£20.99","Five"
"Astrophysics for Beginners","£15.99","Four"
...
```

## Testing & Validation
- **Manual Testing**: The script has been tested with different book categories.
- **Edge Cases**:
  - Tested when no books are available.
  - Checked handling of missing HTML elements.

## Future Enhancements
- Add **multithreading** for faster scraping.
- Store data in a **database** instead of a CSV file.
- Implement a **GUI** for user-friendly interaction.

## License
This project is open-source under the MIT License.

---
### Author
Created by **Muhammad Arsalan** - [GitHub](https://github.com/arsalan4work/)

