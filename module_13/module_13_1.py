import json


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
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)
        return data


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


if __name__ == "__main__":
    main()
