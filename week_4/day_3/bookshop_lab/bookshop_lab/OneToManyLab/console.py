import pdb
from models.authors import Author
from models.books import Book

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

book_repository.delete_all()
author_repository.delete_all()

author_1 = Author("Harper", "Lee", 59)
author_2 = Author("Agatha", "Christie", 67)
author_repository.save(author_1)
author_repository.save(author_2)

book_1 = Book("To Kill a Mockingbird", "Classics", author_1)
book_2 = Book("Go Set a Watchman", "Drama", author_1)
book_3 = Book("Murder on the Orient Express", "Crime", author_2)
book_4 = Book("Death on the Nile", "Crime", author_2)
book_repository.save(book_1)
book_repository.save(book_2)
book_repository.save(book_3)
book_repository.save(book_4)

pdb.set_trace()
