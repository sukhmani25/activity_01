"""
Description: Unit tests for the Book class.
Usage: To execute all tests in the terminal execute 
the following command: python -m unittest tests/test_book.py
"""

__author__ = "Sukhmani"
__version__ = "1.0.0"

import unittest
from genre.genre import Genre
from library_item.library_item import LibraryItem


class TestGenre(unittest.TestCase):
    
    def test_init_valid_inputs_sets_attributes(self):
# Arrange & Act
        library_items = LibraryItem(1, "Steven Jobs", "Walter Isaacson", Genre.NON_FICTION, True)
# Assert
        self.assertEqual("Steven Jobs", library_items._LibraryItem__title)
        self.assertEqual("Walter Isaacson", library_items._LibraryItem__author)
        self.assertEqual(Genre.NON_FICTION, library_items._LibraryItem__genre)
        self.assertEqual(1, library_items._LibraryItem__item_id)
        self.assertEqual(True, library_items._LibraryItem__is_borrowed)
    
    def test_init_blank_title_raises_exception(self):
# Arrange & Act and Assert
        with self.assertRaises(ValueError):
            LibraryItem(1,"", "Walter Isaacson", Genre.NON_FICTION, True)

    def test_init_blank_author_raises_exception(self):
# Arrange & Act and Assert
        with self.assertRaises(ValueError):
            LibraryItem(1, "Steve Jobs", "", Genre.NON_FICTION, True)

    def test_init_invalid_genre_raises_exception(self):
# Arrange & Act and Assert
        with self.assertRaises(ValueError):
            LibraryItem(1, "Steve Jobs", "Walter Isaacson", "?", True)
    
    def test_init_invalid_item_id_raise_exception(self):
# Arrange & Act and Assert
        with self.assertRaises(ValueError):
            LibraryItem(1, "Steve Jobs", "Walter Isaacson", "?", True)
    
    def test_init_invalid_is_borrowed_raise_exception(self):
# Arrange & Act and Assert    
        with self.assertRaises(ValueError):
            LibraryItem(1, "Steve Jobs", "Walter Isaacson", "?", True)
    




    