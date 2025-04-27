import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    return BooksCollector()

def test_add_new_book(self, collector):
    collector.add_new_book('Мастер и Маргарита')
    collector.add_new_book('Мастер и Маргарита')
    assert len(collector.get_books_genre()) == 1