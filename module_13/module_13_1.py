import json
from typing import Optional, List


# Завдання 1
# Є словник з логінами(ключ) та паролями(значення)
# користувачів. Реалізуйте програму яка дозволяє:
#  завантажити дані з файлу
#  зберегти дані у файл
#  додати нового користувача
#  видалити користувача
#  зміна паролю
#  вхід у систему(якщо логін і пароль правильні)
# Реалізуйте все через функції.

FILENAME = "users.json"


def get_data_users(filename: str = FILENAME) -> dict[str, str] | None:
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return None


def save_users(
    data: dict[str, str],
    filename: str = FILENAME,
) -> None:
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file)


def add_user() -> None:
    users = get_data_users(FILENAME)

    if users is None:
        print("No users file")
        return

    name = input("Enter name: ")

    if name in users:
        print("Користувач вже існує")
        return

    password = input("Enter password: ")

    users[name] = password
    save_users(users, FILENAME)


def remove_user():
    users = get_data_users(FILENAME)

    if users is None:
        print("No users file")
        return

    name = input("Enter name: ")

    if name not in users:
        print("Такого користувача не існує")

    del users[name]
    save_users(users, FILENAME)


def change_password():
    users = get_data_users(FILENAME)

    if users is None:
        print("No users file")
        return

    name = input("Enter name: ")

    if name not in users:
        print("Такого користувача не існує")
        return

    password = input("Enter password: ")

    users[name] = password
    save_users(users, FILENAME)


def login():
    users = get_data_users(FILENAME)

    if users is None:
        print("No users file")
        return

    name = input("Enter name: ")
    password = input("Enter password: ")

    if name not in users or users[name] != password:
        print("Не вірно введено логін та пароль")
        return

    print("Ви увійшли")


def main():
    print(
        "МЕНЮ:\n"
        "1 - Додати користувача\n"
        "2 - Видалити користувача\n"
        "3 - Змінити пароль\n"
        "4 - Вхід у систем\n"
        "0 - Вихід"
    )

    while True:
        choice = int(input("Оберіть дію: "))

        if choice == 1:
            add_user()
        elif choice == 2:
            remove_user()
        elif choice == 3:
            change_password()
        elif choice == 4:
            login()
        elif choice == 0:
            break
        else:
            print("Невірний вибір!")


# Завдання 2
# Створіть клас Cart
# Атрибути:
#  user – ім’я користувача
#  items – список товарів
#  total – загальна ціна
# Методи:
#  add(item, price) – добавити товар у кошик
#  delete(item, price) – видалити товар з кошика
#  info() – вивести інформацію про кошик
#  save(fiename) – зберегти дані у файл(за
# замовчуванням cart.json)
#  load(fiename) – завантажити дані з файла(за
# замовчуванням cart.json)


class Cart:
    def __init__(
        self, user: str, items: Optional[List[str]] = None, total: float = 0
    ) -> None:
        self._user = user
        self._total = total

        if items is None:
            items = []
        else:
            self._items = items

    def add_item(self, item: str, price: float) -> None:
        if item not in self._items:
            self._items.append(item)

        self._total += price

    def delete_item(self, item: str, price: float) -> None:
        if item not in self._items:
            print("Такого товару не має в кошику")
            return

        self._items.remove(item)
        self._total -= price

    def show_info(self) -> None:
        print(
            f"В кошику є товари:\n"
            f"{', '.join(self._items)}\n"
            f"на суму: {self._total}"
        )

    def save(self, filename: str = "cart.json") -> None:
        data = {
            "user": self._user,
            "products": self._items,
            "total": self._total,
        }

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file)

    def load(self, filename: str = "cart.json") -> None:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        self._user = data["user"]
        self._items = data["products"]
        self._total = data["total"]


# Завдання 3
# Створіть файл settings.json з базовими налаштуваннями
# програми, наприклад графічного інтерфейсу:
#  розмір зображення – 500х600
#  колір фону – сірий
#  колір кнопок – світлосірий
#  розміщення кнопок – [100, 50]
#  інструкція користувачу
# Напишіть код, де завантажується налаштування і
# створюються відповідні змінні size, background_color, …


def get_values():
    with open("settings.json", "r", encoding="utf-8") as file:
        settings = json.load(file)

    for key, value in settings.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
