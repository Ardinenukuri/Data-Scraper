import unittest
from scraper.core import parse_books
from scraper.models import Book

class TestScraper(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Load the sample HTML file once for all tests."""
        try:
            with open('tests/sample_page.html', 'r', encoding='utf-8') as f:
                cls.sample_html = f.read()
        except FileNotFoundError:
            cls.sample_html = None

    def test_parse_books_from_sample_html(self):
        """Tests that books are correctly parsed from a local HTML file."""
        self.assertIsNotNone(self.sample_html, "Sample HTML file not found.")

        books = parse_books(self.sample_html)
        
        self.assertEqual(len(books), 20)

        first_book = books[0]
        self.assertIsInstance(first_book, Book)
        self.assertEqual(first_book.title, "A Light in the Attic")
        self.assertEqual(first_book.price, 51.77)
        self.assertEqual(first_book.rating, "Three/Five")
        self.assertEqual(first_book.availability, "In stock")
        
        last_book = books[-1]
        self.assertEqual(last_book.title, "It's Only the Himalayas")
        self.assertEqual(last_book.price, 45.17)
        self.assertEqual(last_book.rating, "Two/Five")
        