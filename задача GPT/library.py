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
        return f"Книга {self.title} была взята"
    
    def return_book(self):
        if self.is_available:
            raise ValueError(f"Книга {self.title} и так доступна, ее не надо возвращать")
        self.is_available = True
        return f"Книга {self.title} возвращена"
        