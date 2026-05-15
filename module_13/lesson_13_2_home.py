# Напишіть програму для збереження даних про музичні
# групи у вигляді словника, де ключ – назва групи, значення –
# список альбомів.
# Напишіть функціонал:
#  додати новий гурт
#  додати новий альбом
#  зберегти дані через json
#  зберегти дані через pickle
#  завантажити дані через json
#  завантажити дані через pickle
import json
import pickle
from typing import Dict


def add_new_group(groups: Dict[str, list]) -> None:
    group = input("Введіть назву групи: ")
    groups[group] = []


def add_new_album(groups: Dict[str, list]) -> None:
    group = input("Введіть назву групи")

    if group not in groups:
        print("Такої групи не має в передіку")
        return

    album = input("Введіть назву альбому")
    groups[group].append(album)


def save_json(groups: Dict[str, list]) -> None:
    with open("groups.json", "w", encoding="utf-8") as f:
        json.dump(groups, f, indent=2)


def save_pickle(groups: Dict[str, list]) -> None:
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)


def load_json() -> Dict[str, list]:
    try:
        with open("groups.json", "r", encoding="utf-8") as f:
            return json.load(f)

    except FileNotFoundError:
        print("File groups.json not found")
        return {}


def load_pickle() -> Dict[str, list]:
    try:
        with open("groups.pickle", "rb") as f:
            return pickle.load(f)

    except FileNotFoundError:
        print()
        return {}


def main():
    while True:
        print(
            "=============== МЕНЮ ====================\n"
            "Для додаваня нової груи введіть 1\n"
            "Для нового альбому групи введіть 2\n"
            "Для виходу введіть 0\n"
            "=========================================\n"
        )

        action = int(input("Оберіть необхідну дію: "))

        if action < 0 or action > 2:
            print("Не вірно введено дію")
            continue

        if action == 1:
            groups = load_json()

            add_new_group(groups)
            save_json(groups)
            save_pickle(groups)

        elif action == 2:
            groups = load_json()

            add_new_album(groups)
            save_json(groups)
            save_pickle(groups)

        elif action == 0:
            print("Вихід")
            break
