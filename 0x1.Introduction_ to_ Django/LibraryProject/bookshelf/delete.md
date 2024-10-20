from bookshelf.models import Book

# Delete the book you created
book_to_delete = Book.objects.get(title='Sample Book')
book_to_delete.delete()

# Confirm deletion by trying to retrieve all books
all_books = Book.objects.all()
