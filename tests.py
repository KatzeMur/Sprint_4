from main import BooksCollector
import pytest

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

    def test_add_new_book_valid_name_added(self):  #проверка, что новая книга с валидным названием добавляется
        collector = BooksCollector()
        collector.add_new_book('Ночной дозор')
        assert 'Ночной дозор' in collector.get_books_genre()

    def test_add_new_book_empty_name_dont_add(self): #проверка, что книга с пустым названием не добавляется
        collector = BooksCollector()
        collector.add_new_book('')
        assert ' ' not in collector.get_books_genre()

    def test_set_book_genre_sets_genre(self): #проверка установки жанра для книги
        collector = BooksCollector()
        collector.add_new_book('Ночной дозор')
        collector.set_book_genre('Ночной дозор', 'Фантастика')
        assert collector.get_book_genre('Ночной дозор') == 'Фантастика'

    def test_get_book_genre_gets_genre(self): #проверка получения жарнра существующей книги
        collector = BooksCollector()
        collector.add_new_book('Ночной дозор')
        collector.set_book_genre('Ночной дозор', 'Фантастика')
        assert collector.get_book_genre('Ночной дозор') == 'Фантастика'

    @pytest.mark.parametrize('book, genre', [
        ('Ночной дозор', 'Фантастика'),
        ('Кладбище домашних животных', 'Ужасы'),
        ('Кофточка', 'Комедии')
    ])
    def test_get_books_with_specific_genre_finds_books(self, book, genre): 
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        result = collector.get_books_with_specific_genre(genre)
        assert book in result

    def test_get_books_for_children_gets_books_without_age_rating(self): #проверка фильтра книг для детей
        collector = BooksCollector()
        collector.add_new_book('Кладбище домашних животных')
        collector.set_book_genre('Кладбище домашних животных', 'Ужасы')
        collector.add_new_book('Ну, погоди!')
        collector.set_book_genre('Ну, погоди!', 'Мультфильмы')
        result = collector.get_books_for_children()
        assert 'Ну, погоди!' in result and 'Кладбище домашних животных' not in result

    def test_add_book_in_favorites_adds_book(self): #проверка добавления книги в избранное
        collector = BooksCollector()
        collector.add_new_book('Ночной дозор')
        collector.add_book_in_favorites('Ночной дозор')
        assert 'Ночной дозор' in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_deletes_book(self): #проверка удаления книги из избранного
        collector = BooksCollector()
        collector.add_new_book('Ночной дозор')
        collector.add_book_in_favorites('Ночной дозор')
        collector.delete_book_from_favorites('Ночной дозор')
        assert 'Ночной дозор' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_shows_list(self): #проверка получения списка избранных книг
        collector = BooksCollector()
        collector.add_new_book('Ночной дозор')
        collector.add_book_in_favorites('Ночной дозор')
        collector.add_new_book('Ну, погоди!')
        collector.add_book_in_favorites('Ну, погоди!')
        assert collector.get_list_of_favorites_books() == ['Ночной дозор', 'Ну, погоди!']

    
        
    
    

    

    