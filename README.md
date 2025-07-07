# Web Scraper for "Books to Scrape"

A Python-based web scraper designed to extract book information from [books.toscrape.com](http://books.toscrape.com/). The scraper fetches book titles, prices, star ratings, and availability, then saves the data into a clean CSV file.

This project is built with a focus on modern, professional Python practices, including a clean architecture, data modeling with `dataclasses`, robust error handling, and offline unit testing.

## Features

-   **Data Extraction**: Scrapes book titles, prices, ratings, and stock status.
-   **HTML Parsing**: Uses `requests` and `BeautifulSoup` for efficient web page fetching and parsing.
-   **CSV Export**: Saves all scraped data into a structured `scraped_books.csv` file.
-   **Robustness**: Includes error handling for network issues and HTML parsing failures.
-   **Testable Code**: The core logic is separated from I/O, allowing for reliable offline unit tests.

## Project Structure

```
data_scraper_project/
├── scraper/
│   ├── models.py           # Contains the 'Book' dataclass
│   └── core.py             # Core functions for fetching, parsing, and saving
├── tests/
│   ├── test_scraper.py     # Unit tests for the scraper's parsing logic
│   └── sample_page.html    # A local copy of the website for offline testing
├── main.py                 # The main script to run the scraper
├── requirements.txt        # Project dependencies
└── README.md               # This documentation file
```

## Getting Started

### Prerequisites

-   Python 3.7 or higher

### Installation

1.  Clone the repository to your local machine:
    ```bash
    git clone <your-repo-url>
    cd data_scraper_project
    ```
2.  Install the required Python packages using `pip`:
    ```bash
    pip install -r requirements.txt
    ```

### How to Run the Scraper

To run the scraper and generate the CSV file, execute the `main.py` script from the project's root directory:

```bash
python main.py
```

Upon successful execution, a file named `scraped_books.csv` will be created in the same directory, containing the data from the first page of the website.

### How to Run Tests

This project includes unit tests that verify the HTML parsing logic without making live web requests. The tests run against a saved local copy of the website (`tests/sample_page.html`).

To run the tests, use Python's built-in `unittest` module:
```bash
python -m unittest discover
```
A successful run will show an "OK" status, confirming that the core logic is working correctly.

---

### **Disclaimer**

This project is for educational purposes only. Always be respectful of the websites you scrape. Check the website's `robots.txt` file and terms of service before scraping, and avoid sending too many requests in a short period.