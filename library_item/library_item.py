"""A class to manage LibraryItem objects."""

__author__ = "Sukhmani"
__version__ = "1.0.0"

from genre.genre import Genre

class LibraryItem:
    """
    Attributes:
        title: The title of the library item.
        author: The author of the library item.
        genre: The Genre of the library item.
        item_id: An id number to uniquely identify the library item.
        is_borrowed: Identifies whether the library item is borrowed (True) or available (False).
    """
    def __init__(self, item_id: int, title: str, author: str, genre: Genre, is_borrowed: bool):
        """
        Args:
        title: The title of the library item.
        author: The author of the library item.
        genre: The Genre of the library item.
        item_id: An id number to uniquely identify the library item.
        is_borrowed: Identifies whether the library item is borrowed (True) or available (False).
        """

# Title validation
        if len(title.strip()) > 0:
            self.__title = title
        else:
            raise ValueError("Title cannot be blank.")

# Author validation        
        if len(author.strip()) > 0:
            self.__author = author
        else:
            raise ValueError("Author cannot be blank.")

# Genre validation        
        if isinstance(genre, Genre):
            self.__genre = genre
        else:
            raise ValueError("Invalid Genre.")

# Item ID validation        
        if isinstance(item_id, int):
            self.__item_id = item_id
        else:
            raise ValueError("Item Id must be numeric.")

# Is borrowed validation        
        if isinstance(is_borrowed, bool):
            self.__is_borrowed = is_borrowed
        else:
            raise ValueError("Is Borrowed must be a boolean value.")
        