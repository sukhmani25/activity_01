"""A client program written to verify correctness of 
the activity classes."""

__author__ = "COMP-2327 Faculty"
__version__ = "1.0.0"
__credits__ = ""

from genre.genre import Genre
from library_item.library_item import LibraryItem


def main():
    """Test the functionality of the methods encapsulated 
    in this project.
    """ 

# Code a statement which creates an instance of the LibraryItem class with valid inputs.

    try:
        book = LibraryItem(1, "Steve Jobs", "Walter Isaacson", Genre.NON_FICTION, True)
    except ValueError as e:
        print(e)

# Using the instance defined above, and the class Accessors, print each of the attributes of the LibraryItem instance.

    try:
        print(f"book item id: {book.item_id}")
        print(f"book title: {book.title}")
        print(f"book author: {book.author}")
        print(f"book genre: {book.genre}")
        print(f"is borrowed: {book.is_borrowed}")
        print()
    except Exception as e:
        print(e)

# Code a statement which creates an instance of the LibraryItem class with one or more invalid inputs.

    try:
        invalid = LibraryItem(1, "", "Walter Isaacson", Genre.NON_FICTION, True)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()