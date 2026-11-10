# Напишіть гру вгадати число: комп’ютер загадує число
# від 1 до 100. Користувач вводить свої відповіді на що
# отримує підказки більше\менше.
# Якщо число вгадане менш ніж за 5 спроб, то переміг
# користувач, інакше комп’ютер.
# Реалізуйте такий функціонал:
#  почати нову гру – користувач вводить числа до
# правильної відповіді
#  вивести результат – кількість перемог та програшів
#  зберегти дані – зберегти кількості перемог та
# програшів у файл
#  завантажити дані – завантажити кількості перемог
# та програшів
# Реалізуйте все функціями
import json
import random
from typing import Optional


FILENAME = "game.json"
MAX_ATTEMPTS = 5


def get_random_number() -> int:
    return random.randint(1, 100)


def get_user_number() -> int:
    user_num = int(input("Вгадайте число від 1 до 100: "))
    return user_num


def check_number(random_num, user_num) -> bool:
    if user_num < random_num:
        print("менше")
        return False

    if user_num > random_num:
        print("більше")
        return False

    return True


def show_info(data_game: dict[str, str]) -> None:
    if data_game is None:
        return

    print(
        "\n============ Статистика гри ===================\n"
        f"Кількість перемог: {data_game['wins_count']}\n"
        f"Кількість поразок: {data_game['losses_count']}\n"
        "=================================================\n"
    )


def save_data(filename, data_game: dict[str, int]) -> None:
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data_game, file)


def load_data(filename) -> Optional[dict[str, int]] | None:
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        print("File not found")
        return None


def change_statistics(key: "str") -> None:
    data_game = load_data(FILENAME)

    if data_game is None:
        data_game = {"wins_count": 0, "losses_count": 0}

    data_game[key] += 1

    save_data(FILENAME, data_game)


def start_game(random_num) -> None:
    print("У вас є 5ть спроб")
    counter = 0

    while True:
        if counter == MAX_ATTEMPTS:
            change_statistics("losses_count")
            counter = 0
            print("\nВи програли\n")
            break

        counter += 1
        print(f"\nСпроба #{counter}")
        user_num = get_user_number()

        if not check_number(random_num, user_num):
            if counter < MAX_ATTEMPTS:
                print("Спробуйте ще раз")
            continue

        change_statistics("wins_count")
        print("ви вгадали")
        counter = 0
        break


def check_action(action: str) -> bool:
    menu = ["start", "exit", "show", "save"]
    return action in menu


def show_menu() -> None:
    print(
        "Меню:\n"
        "Для початку нової гри введіть start\n"
        "Для виходу з гри введіть exit\n"
        "Для перегляду статистики введіть show\n"
    )


def main():
    while True:
        show_menu()
        action = input("Оберіть необхідну дію: ").lower().strip()
        is_valid_action = check_action(action)

        if not is_valid_action:
            print("Не вірно введені дані.")
            continue

        if action == "start":
            secret_number = get_random_number()
            start_game(secret_number)

        elif action == "show":
            show_info(load_data(FILENAME))

        elif action == "exit":
            print("Вихід з меню")
            break


if __name__ == "__main__":
    main()
