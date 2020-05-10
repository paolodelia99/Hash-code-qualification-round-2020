from book import Book
from library import Library
from parsers.scenarioParser import ScenarioParser


def test_parse_hash_code_file():
    sample_books = [Book(0, 1), Book(1, 2), Book(2, 3), Book(3, 6), Book(4, 5), Book(5, 4)]
    sample_libraries = [Library(0, 5, 2, 2, [Book(0, 1), Book(1, 2), Book(2, 3), Book(3, 6), Book(4, 5)]),
                        Library(1, 4, 3, 1, [Book(5, 4), Book(2, 3), Book(3, 6), Book(0, 1)])]

    parser = ScenarioParser("a_example")
    d, books, libraries = parser.parse_hash_code_file()
    assert d == 7
    assert [a == b for a, b in zip(books, sample_books)]
    assert [a == b for a, b in zip(libraries, sample_libraries)]
