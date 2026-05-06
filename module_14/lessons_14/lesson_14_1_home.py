# Програма складається з трьох потоків. Перший
# просить в користувача вводити числа, поки не введено
# порожній рядок, та зберігає числа в список.
# Інші два потоки чекають поки перший завершить
# роботу, і вже потім запускаються. Один рахує суму чисел в
# списку, інший рахує середнє арифметичне.
# Список чисел, сума та середнє виводяться на екран
import threading


def get_list_numbers(list_numbers, done_event: threading.Event) -> None:
    while True:
        number = input("Введіть число (для виходу натисність Enter): ")

        if number == "":
            print("Вихід")
            break

        try:
            list_numbers.append(int(number))

        except ValueError:
            print("Значення має бути цілим числом")

    done_event.set()


def find_sum(
    nums: list[int], results: dict[str, int], done_event: threading.Event
) -> None:
    done_event.wait()

    elements_sum = 0

    for number in nums:
        elements_sum += number

    results["sum"] = elements_sum


def find_arithmetic_mean(
    nums: list[int], results: dict[str, float], done_event: threading.Event
) -> None:
    done_event.wait()

    elements_sum = 0

    if len(nums) == 0:
        results["arithmetic_mean"] = 0

    else:
        for num in nums:
            elements_sum += num

        results["arithmetic_mean"] = elements_sum / len(nums)


def start_task():
    list_numbers = []
    results: dict[str, int | float] = {}
    done_event = threading.Event()

    thread_list = threading.Thread(
        target=get_list_numbers,
        args=(
            list_numbers,
            done_event,
        ),
    )

    thread_sum = threading.Thread(
        target=find_sum,
        args=(
            list_numbers,
            results,
            done_event,
        ),
    )

    thread_arithmetic_mean = threading.Thread(
        target=find_arithmetic_mean,
        args=(
            list_numbers,
            results,
            done_event,
        ),
    )

    thread_list.start()
    thread_sum.start()
    thread_arithmetic_mean.start()

    thread_list.join()
    thread_sum.join()
    thread_arithmetic_mean.join()

    print("\nРезультат:")
    print(f"Sum: {results['sum']}")
    print(f"Arithmetic mean: {results['arithmetic_mean']}\n")

    print("Обчислення завершено.")


start_task()
