import pytest
from books_collector import BooksCollector

@pytest.fixture
def collector():
    return BooksCollector()

def test_add_new_book(collector):
    collector.add_new_book('Мастер и Маргарита')
    collector.add_new_book('Мастер и Маргарита')
    assert len(collector.get_books_genre()) == 1