# Retrieve the book you created
```python
from bookshelf.models import Book

retrieved_book = Book.objects.get(title='1984')