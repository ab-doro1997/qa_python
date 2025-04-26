from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

@pytest.mark.parametrize(
    "book_name,expected_result",
    [
        ('Властелин Колец', True),
        ('Маленький принц', True),
        ('Мастер и Маргарита', True),
        ('Три товарища, путешествующие по морям приключений, преодолевающие бури судьбы и искавшие сокровища утраченной империи загадочных существ', False),
    ]
)
def test_add_new_book(book_name, expected_result):
    collector = BooksCollector()
    initial_length = len(collector.books_genre)
    collector.add_new_book(book_name)
    result = len(collector.books_genre) > initial_length
    assert result == expected_result

@pytest.mark.parametrize("genre", ["Фантастика", "Ужасы"])
def test_set_book_genre_valid(collector, genre):
    collector.add_new_book("Книга")
    collector.set_book_genre("Книга", genre)
    assert collector.books_genre["Книга"] == genre

def test_set_book_genre_invalid(collector):
    collector.add_new_book("Книга")
    collector.set_book_genre("Книга", "Роман")
    assert collector.books_genre["Книга"] == ""

def test_get_book_genre():
    collector = BooksCollector()
    collector.add_new_book("Дюна")
    collector.set_book_genre("Дюна", "Фантастика")
    assert collector.get_book_genre("Дюна") == "Фантастика"

def test_get_books_with_specific_genre():
    collector = BooksCollector()
    collector.add_new_book("Терминатор")
    collector.set_book_genre("Терминатор", "Ужасы")
    collector.add_new_book("Звездные войны")
    collector.set_book_genre("Звездные войны", "Фантастика")
    assert collector.get_books_with_specific_genre("Ужасы") == ["Терминатор"]

def test_get_books_genre():
    collector = BooksCollector()
    collector.add_new_book("Книга1")
    collector.set_book_genre("Книга1", "Фантастика")
    collector.add_new_book("Книга2")
    collector.set_book_genre("Книга2", "Ужасы")
    assert collector.get_books_genre() == {"Книга1": "Фантастика", "Книга2": "Ужасы"}

def test_get_books_for_children():
    collector = BooksCollector()
    collector.add_new_book("Сказки Пушкина")
    collector.set_book_genre("Сказки Пушкина", "Мультфильмы")
    collector.add_new_book("Война миров")
    collector.set_book_genre("Война миров", "Ужасы")
    assert collector.get_books_for_children() == ["Сказки Пушкина"]

def test_add_book_in_favorites():
    collector = BooksCollector()
    collector.add_new_book("Повелитель мух")
    collector.set_book_genre("Повелитель мух", "Ужасы")
    collector.add_book_in_favorites("Повелитель мух")
    assert "Повелитель мух" in collector.get_list_of_favorites_books()

def test_delete_book_from_favorites():
    collector = BooksCollector()
    collector.add_new_book("Мастер и Маргарита")
    collector.set_book_genre("Мастер и Маргарита", "Фантастика")
    collector.add_book_in_favorites("Мастер и Маргарита")
    collector.delete_book_from_favorites("Мастер и Маргарита")
    assert "Мастер и Маргарита" not in collector.get_list_of_favorites_books()

def test_get_list_of_favorites_books():
    collector = BooksCollector()
    collector.add_new_book("Гордость и предубеждение")
    collector.set_book_genre("Гордость и предубеждение", "Романтика")
    collector.add_book_in_favorites("Гордость и предубеждение")
    assert collector.get_list_of_favorites_books() == ["Гордость и предубеждение"]