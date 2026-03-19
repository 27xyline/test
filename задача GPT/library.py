class Book:
    def __init__(self, title, author, year, is_available=True):
        self.title = title
        self.author = author
        self.year = year
        self.is_available = is_available
    
    def borrow(self):
        if not self.is_available:
            raise ValueError(f"Книга {self.title} уже взята")
        self.is_available = False
        print(f"Книга {self.title} была взята")
            