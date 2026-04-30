import json
import threading


# Користувач вводить з клавіатури значення у список.
# Після чого запускаються два потоки. Перший потік знаходить максимум у списку. Другий потік знаходить мінімум
# у списку. Результати обчислень виведіть на екран.
nums = list(map(int, input("Введіть числа через пробіл: ").split()))


def find_max(numbers, results: dict[str, int]):
    results["maximum"] = max(numbers)


def find_min(numbers, results: dict[str, int]):
    results["minimum"] = min(numbers)


def start_task1():
    results: dict[str, int] = {}

    thread_max = threading.Thread(
        target=find_max,
        args=(
            nums,
            results,
        ),
    )
    thread_min = threading.Thread(
        target=find_min,
        args=(
            nums,
            results,
        ),
    )

    thread_max.start()
    thread_min.start()

    thread_max.join()
    thread_min.join()

    print(f"Максимум у списку: {results['maximum']}")
    print(f"Мінімум у списку: {results['minimum']}")
    print("Обчислення завершено.")


start_task1()


# Завдання 2
# Користувач вводить з клавіатури значення у список.
# Після чого запускаються два потоки. Перший потік знаходить суму елементів у списку. Другий потік знаходить
# середнє арифметичне у списку. Результати обчислень
# виведіть на екран.


def find_sum(numbers, results: dict[str, int]):
    elements_sum = 0

    for num in numbers:
        elements_sum += num

    results["sum"] = elements_sum


def find_arithmetic_mean(numbers, results: dict[str, float]):
    elements_sum = 0

    for num in numbers:
        elements_sum += num

    results["arithmetic_mean"] = elements_sum / len(numbers)


def start_task2():
    results: dict[str, int] = {}

    thread_max = threading.Thread(target=find_sum, args=(nums,))

    thread_arithmetic_mean = threading.Thread(target=find_arithmetic_mean, args=(nums,))

    thread_max.start()
    thread_arithmetic_mean.start()

    thread_max.join()
    thread_arithmetic_mean.join()

    print(f"Sum: {results['sum']}")
    print(f"Arithmetic mean: {results['arithmetic_mean']}")
    print("Обчислення заверщшено 2")


start_task2()


# Завдання 3
# Користувач вводить з клавіатури шлях до файлу, що
# містить набір чисел. Після чого запускаються два потоки.
# Перший потік створює новий файл, в який запише лише
# парні елементи списку. Другий потік створює новий файл,
# в який запише лише непарні елементи списку. Кількість
# парних і непарних елементів виводиться на екран.
def get_number(filepath: str) -> list[int]:
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.loads(f.read())["numbers"]

    except FileNotFoundError:
        print("Файл не знайдено!")
        return []


def find_even():
    numbers = get_number("numbers.json")
    evens = []

    for num in numbers:
        if num % 2 == 0:
            evens.append(num)

    print(f"Evens: {len(evens)}")

    return evens


def save_even():
    evens = find_even()

    with open("evens.json", "w", encoding="utf-8") as f:
        json.dump({"evens": evens}, f)


def find_odd():
    numbers = get_number("numbers.json")
    odds = []

    for num in numbers:
        if num % 2 == 1:
            odds.append(num)

    print(f"Odds: {len(odds)}")

    return odds


def save_odd():
    odds = find_odd()

    with open("odds.json", "w", encoding="utf-8") as f:
        json.dump({"odds": odds}, f)


def start_task3():
    thread_even = threading.Thread(target=save_even)
    thread_odd = threading.Thread(target=save_odd)

    thread_even.start()
    thread_odd.start()

    thread_even.join()
    thread_odd.join()

    print("Обчислення заверщшено 3")


# Завдання 4
# Користувач вводить з клавіатури шлях до файлу та
# слово для пошуку. Після чого запускається потік для
# пошуку цього слова у файлі. Результат пошуку виведіть
# на екран.


def search_word(filepath, word):
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()

        count = content.lower().count(word.lower())

        if count > 0:
            print(f"Слово '{word}' знайдено {count} раз(и).")
        else:
            print(f"Слово '{word}' не знайдено у файлі.")

    except FileNotFoundError:
        print("Файл не знайдено!")

    except Exception as e:
        print("Помилка:", e)


def start_task4():
    filepath = input("Введіть шлях до файлу: ")
    word = input("Введіть слово для пошуку: ")

    thread_search = threading.Thread(target=search_word, args=(filepath, word))

    thread_search.start()
    thread_search.join()

    print("Пошук заверщшено 4")


start_task4()
