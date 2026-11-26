from abc import ABC, abstractmethod
from datetime import date

# Abstract Base Class
class LibraryItem(ABC):
    def __init__(self, title, price):
        self.title = title
        self.__price = price  # private - Encapsulation
        self.__borrow_date = None

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            print("Price negative-a irukka koodathu!")
        else:
            self.__price = value

    @property
    def borrow_date(self):
        return self.__borrow_date

    @abstractmethod
    def calculate_fee(self, days):
        pass

    @abstractmethod
    def display_metadata(self):
        pass

    # Dunder methods
    def __str__(self):
        return f"{self.title} - Rs.{self.__price}"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.title}')"

    def __eq__(self, other):
        return isinstance(other, LibraryItem) and self.title == other.title

    def __len__(self):
        return len(self.title)

# Child Class 1 - Inheritance + Polymorphism
class Book(LibraryItem):
    def __init__(self, title, price, author, pages):
        super().__init__(title, price)
        self.author = author
        self.pages = pages

    def calculate_fee(self, days):
        return days * 10  # Rs.10 per day

    def display_metadata(self):
        return f"Book: {self.title} by {self.author}, {self.pages} pages"

# Child Class 2
class Magazine(LibraryItem):
    def __init__(self, title, price, issue):
        super().__init__(title, price)
        self.issue = issue

    def calculate_fee(self, days):
        return days * 5

    def display_metadata(self):
        return f"Magazine: {self.title} - Issue {self.issue}"

# Child Class 3
class DigitalMedia(LibraryItem):
    def __init__(self, title, price, file_size):
        super().__init__(title, price)
        self.file_size = file_size

    def calculate_fee(self, days):
        return days * 15

    def display_metadata(self):
        return f"Digital: {self.title} - {self.file_size} MB"

# Manager Class
class InventoryManager:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"Added: {item}")

    def checkout(self, title, days):
        for item in self.items:
            if item.title == title:
                print(f"Checked out {title} for {days} days. Fee: Rs.{item.calculate_fee(days)}")
                return
        print("Item not found!")

    def audit_report(self):
        print("\n--- Audit Report ---")
        for item in self.items:
            print(item.display_metadata(), "| Fee (7 days): Rs.", item.calculate_fee(7))
        print(f"Total Items: {len(self.items)}")

# Demo
if __name__ == "__main__":
    inv = InventoryManager()
    b1 = Book("Python Basics", 499, "Paru", 300)
    m1 = Magazine("Tech Weekly", 99, "Nov 2026")
    d1 = DigitalMedia("Python Video Course", 999, 1200)

    inv.add_item(b1)
    inv.add_item(m1)
    inv.add_item(d1)

    print("\n__str__:", str(b1))
    print("__repr__:", repr(b1))
    print("__len__ (title length):", len(b1))
    print("__eq__ test:", b1 == Book("Python Basics", 499, "Paru", 300))

    inv.checkout("Python Basics", 7)
    inv.audit_report()
