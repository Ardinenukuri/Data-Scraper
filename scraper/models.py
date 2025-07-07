from dataclasses import dataclass

@dataclass
class Book:
    """A dataclass to hold the details of a scraped book."""
    title: str
    price: float
    rating: str
    availability: str