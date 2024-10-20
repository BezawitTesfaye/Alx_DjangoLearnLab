from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author_name = "J.K. Rowling"
books_by_author = Book.objects.filter(author__name=author_name)

# List all books in a library
library_name = "Main Library"
library_books = Library.objects.get(name=library_name).books.all()

# Retrieve the librarian for a library
library_name = "Main Library"
librarian = Librarian.objects.get(library__name=library_name)

# Output the results
for book in books_by_author:
    print(f"Books by {author_name}: {book.title}")

print(f"\nBooks in {library_name}:")
for book in library_books:
    print(book.title)

print(f"\nLibrarian for {library_name}: {librarian.name}")