# main.py (Final Clean Version)

from scraper.core import fetch_page, parse_books, save_to_csv

# --- Configuration ---
TARGET_URL = "http://books.toscrape.com/"
OUTPUT_FILE = "scraped_books.csv"

def main():
    """Main function to run the web scraper."""
    print(f"🚀 Starting scraper for {TARGET_URL}...")

    # 1. Fetch the web page content
    html_content = fetch_page(TARGET_URL)
    if not html_content:
        print("Scraping failed. Exiting.")
        return

    print("✅ Page fetched successfully.")

    # 2. Parse the HTML to extract book data
    books = parse_books(html_content)
    if not books:
        print("No books found or parsing failed. Exiting.")
        return

    print(f"✅ Parsed {len(books)} books.")

    # 3. Save the data to a CSV file
    save_to_csv(books, OUTPUT_FILE)
    print(f"💾 Data successfully saved to '{OUTPUT_FILE}'.")
    print("✨ Scraping complete!")


if __name__ == "__main__":
    main()