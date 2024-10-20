from bookshelf.models import Book

# Update the title of the book "1984" to "Nineteen Eighty-Four"
book_to_update = Book.objects.get(title="1984")
book_to_update.title = "Nineteen Eighty-Four"
book_to_update.save()