### Update the Title of "1984" to "Nineteen Eighty-Four"
```python
from bookshelf.models import Book

# Update the title of the book "1984" to "Nineteen Eighty-Four"
book = Book.objects.get(id=1) book.title= "Nineteen Eighty-Four" book.save()