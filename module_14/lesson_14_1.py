import threading


# Користувач вводить з клавіатури значення у список.
# Після чого запускаються два потоки. Перший потік знаходить максимум у списку. Другий потік знаходить мінімум
# у списку. Результати обчислень виведіть на екран.
nums = list(map(int, input("Введіть числа через пробіл: ").split()))


def find_max(numbers):
    maximum = max(numbers)
    print(f"Максимум у списку: {maximum}")


def find_min(numbers):
    minimum = min(numbers)
    print(f"Мінімум у списку: {minimum}")


thread_max = threading.Thread(target=find_max, args=(nums,))
thread_min = threading.Thread(target=find_min, args=(nums,))

thread_max.start()
thread_min.start()

thread_max.join()
thread_min.join()

print("Обчислення завершено.")


# Завдання 2
# Користувач вводить з клавіатури значення у список.
# Після чого запускаються два потоки. Перший потік знаходить суму елементів у списку. Другий потік знаходить
# середнє арифметичне у списку. Результати обчислень
# виведіть на екран.


def find_sum(numbers):
    elements_sum = 0

    for num in numbers:
        elements_sum += num

    print(f"Sum: {elements_sum}")


def find_arithmetic_mean(numbers):
    elements_sum = 0
    for num in numbers:
        elements_sum += num

    arithmetic_mean = elements_sum / len(numbers)

    print(f"Arithmetic mean: {arithmetic_mean}")


thread_max = threading.Thread(target=find_sum, args=(nums,))

thread_arithmetic_mean = threading.Thread(target=find_arithmetic_mean, args=(nums,))

thread_max.start()
thread_arithmetic_mean.start()

thread_max.join()
thread_arithmetic_mean.join()

print("Обчислення заверщшено 2")

# Завдання 3
# Користувач вводить з клавіатури шлях до файлу, що
# містить набір чисел. Після чого запускаються два потоки.
# Перший потік створює новий файл, в який запише лише
# парні елементи списку. Другий потік створює новий файл,
# в який запише лише непарні елементи списку. Кількість
# парних і непарних елементів виводиться на екран.
