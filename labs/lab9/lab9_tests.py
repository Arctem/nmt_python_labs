import unittest

class BookTest(unittest.TestCase):
    def create_and_str_book(self):
        from library import Book
        tests = [('The Life and Lies of Albus Dumbledore', 'Rita Skeeter'),
            ('Some Other Book', 'Some Person'),
            ('Lab 9', 'Russell White')]
        for title, author in tests:
            book = Book(title, author)
            self.assertIn(title, str(book))
            self.assertIn(author, str(book))

class LibraryTest(unittest.TestCase):
    def test_get_authors(self):
        from library import Book, Library
        tests = [Book('The Life and Lies of Albus Dumbledore', 'Rita Skeeter'),
            ('Some Other Book by Someone'),
            Book('Lab 9', 'The Best TA'),
            Book('Yet Another Book', 'Someone')]
        lib = Library()
        for test in tests:
            lib.add_book(test)
        self.assertEquals(len(lib.get_authors()), 3)
        self.assertIn('Someone', lib.get_authors())
        self.assertNotIn('', lib.get_authors())





class TreeTest(unittest.TestCase):
    pass