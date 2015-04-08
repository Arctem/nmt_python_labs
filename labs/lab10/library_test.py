from library import Book, Library

def main():
    lib = Library()
    lib.add_book(Book('The Life and Lies of Albus Dumbledore', 'Rita Skeeter'))

    with open('library.txt', 'r') as lib_data:
        for line in lib_data:
            lib.add_book(line)

    print(lib)
    print(lib.get_authors())
    assert len(set(lib.get_authors())) == len(lib.get_authors())
    print(lib.get_books_per_author())
    assert len(lib.get_books_per_author()) == len(lib.get_authors())


if __name__ == '__main__':
    main()
