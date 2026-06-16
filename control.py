import random
from typing import List, Optional
from datetime import datetime

# 1. Напишіть програму, яка приймає два цілих числа від
# користувача і виводить суму діапазону чисел між ними.


def get_sum():
    sum_numbers = 0
    start_num = int(input("Enter start number: "))
    end_num = int(input("Enter end number: "))
    start = min(start_num, end_num)
    end = max(start_num, end_num)

    for num in range(start, end + 1):
        sum_numbers += num

    print(f"Сума чисел від {start_num} до {end_num} включно = {sum_numbers}")


# get_sum()


# 2. Напишіть програму, для знаходження суми всіх парних
# чисел від 1 до 100.


def get_sum_even():
    sum_numbers = 0

    for num in range(1, 100):
        if num % 2 == 0:
            sum_numbers += num

    print(f"Сума парних чисел від 1 до 100 = {sum_numbers}")


# get_sum_even()


# 3. Напишіть програму, яка приймає рядок від користувача і
# виводить кожну літеру рядка на окремому рядку.


def show_letter():
    text = input("Введіть текст: ")

    for letter in text:
        if letter.isalpha():
            print(letter)


# show_letter()

# 4. Напишіть програму, яка створює список цілих чисел та
# виводить новий список, який містить лише парні числа з
# вихідного списку.


def get_even_list():
    random_numbers = [random.randint(1, 100) for _ in range(10)]
    even_list = []

    for number in random_numbers:
        if number % 2 == 0:
            even_list.append(number)

    print(f"Список чисел: {random_numbers}")
    print(f"Список парних чисел:{even_list}")


# get_even_list()


# 5. Напишіть функцію, яка приймає список рядків від користувача і повертає новий список, що містить лише
# рядки, що починаються з великої літери.


def get_list_strings():
    list_strings = ["sadfas", "Dfdfs", "Dfafsaf", "asdffasf", "UYTUIYIUY"]
    result = []

    for row in list_strings:
        if row[0].istitle():
            result.append(row)

    return result


# print(f"Список рядків з великої: {get_list_strings()}")


# 6. Напишіть функцію, яка приймає список рядків від
# користувача і повертає новий список, що містить лише
# рядки, які містять слово "Python".


def filter_list(list_rows: List[str]) -> List:
    control_word = "python"
    result = []

    for item in list_rows:
        if control_word in item.lower():
            result.append(item)

    return result


test_list = ["I love Python", "Java is cool", "Python is great", "Hello world"]

# print(f"Result 6: {filter_list(test_list)}")


# 7. (додаткове на кристалики)Напишіть програму, яка
# створює словник, де ключами є слова, а значеннями - їхні
# визначення. Дозвольте користувачу додавати, видаляти
# та шукати слова у цьому словнику.
def create_dict():
    dictionary = {}

    while True:
        print(
            "\n============ Меню ===================\n"
            "1. Додати слово\n"
            "2. Видалити слово\n"
            "3. Знайти слово\n"
            "4. Показати весь словник\n"
            "0. Вийти\n"
        )

        action = input("Оберіть дію: ")

        if action == "1":
            word = input("Введіть слово: ")
            definition = input("Введіть визначення: ")
            dictionary[word] = definition
            print(f"Слово '{word}' додано.")

        elif action == "2":
            word = input("Введіть слово для видалення: ")
            if word in dictionary:
                del dictionary[word]
                print(f"Слово '{word}' видалено.")
            else:
                print("Слово не знайдено.")

        elif action == "3":
            word = input("Введіть слово для пошуку: ")
            if word in dictionary:
                print(f"{word} — {dictionary[word]}")
            else:
                print("Слово не знайдено.")

        elif action == "4":
            if not dictionary:
                print("Словник порожній.")
            else:
                print("\nСловник:")
                for word, definition in dictionary.items():
                    print(f"{word} — {definition}")

        elif action == "0":
            print("Вихід")
            break

        else:
            print("Невірний вибір. Спробуйте ще раз.")


# create_dict()


# 8. (додаткове на кристалики)Використовуючи лямбдафункцію, напишіть вираз, який сортує список кортежів
# за другим елементом кожного кортежу (наприклад, [(1,
# 3), (3, 2), (2, 1)]).


def sort_list():
    data_list = [(1, 3), (3, 2), (2, 1)]
    sorted_list = sorted(data_list, key=lambda x: x[1])
    print(sorted_list)


# sort_list()


# Симулятор роботи сайту
# WebSite: Основний клас, який представляє вебсайт.
# Атрибути: назва сайту, URL, список сторінок.
# Методи: додавання/видалення сторінок, відображення
# інформації про сайт.
# WebPage: Клас, який представляє окрему сторінку на сайті.
# Атрибути: заголовок сторінки, вміст, дата публікації.
# Методи: відображення деталей сторінки.


class WebPage:
    def __init__(
        self,
        title: str,
        content: str,
        date_publish: str = datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
    ):
        self._title = title
        self._content = content
        self._date_publish = date_publish

    def show_page_details(self):
        print(
            f"Cторінка - {self._title}, /n"
            f"Контент: {self._content}, /n"
            f"Дата публікації: {self._date_publish}"
        )


class WebSite:
    def __init__(self, site_name: str, url: str, pages: Optional[List[WebPage]] = None):
        self._site_name = site_name
        self._url = url

        if pages is None:
            self._pages = []
        else:
            self._pages = pages

    def add_page(self, new_page: WebPage):
        self._pages.append(new_page)

    def delete_page(self, old_page: str):
        if len(self._pages) == 0:
            print("Сторінок не має")
            return

        for page in self._pages:
            if page._title.lower() == old_page.lower():
                self._pages.remove(page)
                print(f"Сторінка '{old_page}' видалена")
                return

    def show_site_info(self):
        print(f"Сайт - {self._site_name}, /n" f"адреса: {self._url}, /n")

        if len(self._pages) == 0:
            print("Сторінок не має")
            return

        for page in self._pages:
            page.show_page_details()


# Реалізація функціональності:
# Дозвольте користувачеві створювати новий сайт з
# певною назвою та URL. Додайте можливість створювати нові
# сторінки для сайту, вводячи заголовок та вміст. Реалізуйте
# функцію для видалення сторінок з сайту. Включіть функцію
# для відображення всієї інформації про сайт, включаючи
# список усіх сторінок.
# Розробіть простий текстовий інтерфейс для взаємодії з
# користувачем. Користувач повинен мати змогу вибирати дії,
# такі як створення сайту, додавання/видалення сторінок,
# перегляд інформації про сайт.


def main():
    print(
        "\n============ Меню ===================\n"
        "Для створення сайту натисніть 1: \n"
        "Для створення сторінок на сайті натисніть 2: \n"
        "Для видалення сторінок на сайті натисніть 3: \n"
        "Для відображення всієї інформації про сайт натисні 4: \n"
        "Для виходу натисніть 0: \n"
        "=================================================\n"
    )

    while True:
        action = int(input("Оберіть необхідну дію"))
        site = None

        if action < 0 or action > 4:
            print("Не вірно введено дію")
            continue

        if action == 0:
            print("Вихід")
            break

        elif action == 1:
            name = input("Введіть назву сайту: ")
            url = input("Введіть адресу сайту: ")
            site = WebSite(name, url)
            print(f"Сайт {name} створено")

        elif action == 2:
            if site is None:
                print("Сайт не створено, створіть його")
                continue

            else:
                title = input("Введіть назву сторінки: ")
                content = input("Наповніть сайт: ")
                page = WebPage(title, content)
                site.add_page(page)

        elif action == 3:
            if site is None:
                print("Сайт не створено, створіть його")
                continue

            else:
                title = input("Введіть назву сторінки: ")
                site.delete_page(title)

        elif action == 4:
            if site is None:
                print("Сайт не створено, створіть його")
                continue

            else:
                site.show_site_info()
