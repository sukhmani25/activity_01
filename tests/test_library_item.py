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




    