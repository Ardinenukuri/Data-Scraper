import requests
import csv
import re 
from typing import List, Optional
from bs4 import BeautifulSoup
from .models import Book

def fetch_page(url: str) -> Optional[str]:

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching the URL: {e}")
        return None


def parse_books(html_content: str) -> List[Book]:
    """
    Parses the HTML content to extract book details.
    """
    soup = BeautifulSoup(html_content, 'lxml')
    books_found: List[Book] = []
    
    book_pods = soup.find_all('article', class_='product_pod')

    for pod in book_pods:
        try:
            title = pod.h3.a['title']

            price_text = pod.find('p', class_='price_color').text
            match = re.search(r'[\d.]+', price_text)
            if not match:
                raise ValueError("Price not found in text")
            price = float(match.group(0))
            
            rating_class = pod.find('p', class_='star-rating')['class'][1]
            rating = f"{rating_class}/Five"
            
            availability = pod.find('p', class_='instock availability').text.strip()
            
            books_found.append(Book(
                title=title,
                price=price,
                rating=rating,
                availability=availability
            ))
        except (AttributeError, ValueError, KeyError) as e:
            print(f"⚠️  Could not parse a book pod, skipping. Error: {e}")
            continue

    return books_found

def save_to_csv(books: List[Book], filepath: str):

    try:
        with open(filepath, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Title', 'Price (£)', 'Rating', 'Availability'])
            for book in books:
                writer.writerow([book.title, book.price, book.rating, book.availability])
    except IOError as e:
        print(f"❌ Error writing to CSV file: {e}")