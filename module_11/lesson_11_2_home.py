from typing import List, Dict, Any
import random

# Завдання 1
# Створіть клас Проект з атрибутами: назва, виділений кошторис, загальні витрати
#  чи завершений(за замовчуванням False)
#  час виконання(за замовчуванням 0 місяців)
#  список необхідних задач
# Додайте методи:
#  вивід інформації: назва, час виконання, необхідні задачі
#  добавити нову задачу
#  розбити задачу на під-задачі: передається назва задачі та список під-задач
#  виконати задачу, передається назва, час та ціна виконання
# поповнення кошторису


class Project:
    def __init__(self, name: str, estimation: float):
        self.name = name
        self.estimation = estimation

        self.total_expense: float = 0
        self.is_end: bool = False
        self.total_execution_time: int = 0
        self.tasks: Dict[str, Dict[str, Any]] = {}

    def show_info(self):
        print(
            f"Назва проєкту: {self.name}\n"
            f"\nЧас виконання: {self.total_expense} міс."
        )

        if self.tasks:
            print("\nНеобхідні задачі: ")

            for task in self.tasks:
                if not self.tasks[task]:
                    print(f"\t{task}")
                else:
                    print(f"\t{task['subtasks']}: {', '.join(self.tasks[task])}")
        else:
            print("Список задач порожній")

    def add_task(self, task_name: str):
        if task_name in self.tasks:
            print("Така задача вже є")
            return

        self.tasks[task_name] = {
            "subtasks": [],
            "expenses": 0,
            "execution_time": 0,
        }

    def add_subtask(self, task_name: str, subtasks: list):
        if task_name not in self.tasks:
            print("Такої задачі не має")
            return

        self.tasks[task_name]["subtasks"] = subtasks

    def complete_task(self, task_name: str, time: int, expenses: float):
        if task_name not in self.tasks:
            print("Такої задачі не має")
            return

        self.tasks[task_name]["expenses"] = expenses
        self.tasks[task_name]["execution_time"] = time

        self.total_expense += expenses
        self.total_execution_time += time

    def replenish_estimation(self, estimation: float):
        self.estimation += estimation


my_project = Project(name="New Project", estimation=10.23)

my_project.add_task(task_name="Task 1")
my_project.add_task(task_name="Task 2")
my_project.add_task(task_name="Task 3")
my_project.add_subtask(task_name="Task 4", subtasks=["Task 4.1", "Task 4.2"])
my_project.add_subtask(task_name="Task 3", subtasks=["Task 3.1", "Task 3.2"])
# my_project.show_info()

# ======================================================================= #

# Завдання 2
# Створіть клас Телефон з атрибутами:
#  максимальний обсяг пам’яті
#  зайнята пам’ять
#  чи включений(за замовчуванням False)
#  встановлені додатки у вигляді словника, де ключ – назва додатку, значення – обсяг пам’яті
# Додайте методи:
#  вивести інформацію про використання пам’яті
#  видалити додаток
#  встановити новий додаток, якщо пам’яті достатньо
#  оновити додаток(нова версія може займати іншу кількість пам’яті)
#  запустити додаток, якщо він є і якщо телефон вкючений
#  включити телефон
#  виключити телефон


class Phone:
    def __init__(self, max_memory: int = 128, memory_busy: int = 48):
        self.max_memory = max_memory
        self.memory_busy = memory_busy

        self.is_on: bool = False
        self.app: Dict[str, int] = {}

    def show_info(self):
        print(f"Максимальний обсяг пам’яті: {self.max_memory} Gb")
        print(f"Використано пам’яті: {self.memory_busy} Gb")

    def check_app(self, app_name):
        if app_name not in self.app:
            print("Такий додаток не встановлено")
            return

    def check_memory(self, memory_busy):
        if memory_busy > self.max_memory:
            print("Не достатньо памʼяті")
            return

    def delete_app(self, app_name: str):
        self.check_app(app_name)

        self.memory_busy -= self.app[app_name]
        del self.app[app_name]

    def add_app(self, app_name: str, app_memory: int):
        if app_name in self.app:
            print("Даний застосунок вже втсановлено")
            return

        memory_busy = self.memory_busy + app_memory

        self.check_memory(memory_busy)

        self.app[app_name] = app_memory
        self.memory_busy = memory_busy

    def update_app(self, app_name: str, app_memory: int):
        self.check_app(app_name)

        memory_busy = self.memory_busy + app_memory - self.app[app_name]

        self.check_memory(memory_busy)

        self.app[app_name] = app_memory
        self.memory_busy = memory_busy

    def start_app(self, app_name: str):
        if not self.is_on:
            print("Телефон вимкнено")
            return

        self.check_app(app_name)
        print(f"Додаток {app_name} запущено")

    def on_phone(self):
        self.is_on = True

    def off_phone(self):
        self.is_on = False


# ======================================================================= #

# Завдання 3
# Створіть клас Автомобіль з атрибутами:
#  марка
#  пробіг
#  рівень пального
#  витрата пального(л/км)
#  чи є справним(за замовчуванням True)
# Реалізуйте методи:
#  проїхати певну відстань, має змінитись пробіг та рівень
# пального, якщо автомобіль справний та достатньо
# пального
# З ймовірністю 40% автомобіль може зламатись
#  ремонт
#  поповнення пального


class Car:
    def __init__(self, model: str, run: int, fuel_consumption: float):
        self.model = model
        self.run = run
        self.fuel_consumption = fuel_consumption

        self.fuel: int = 0
        self.is_working: bool = False
        self.probability_breaking = 40

    def drive(self, distance: int):
        if not self.is_working:
            print("Автомобіль не справний")
            return

        fuel = int(distance * self.fuel_consumption)

        if fuel > self.fuel:
            print("Не достатньо пального")
            return

        self.fuel -= fuel
        self.run += distance

        probability = random.randint(0, 100)

        if probability < self.probability_breaking:
            self.is_working = False
            print("Автомобіль зламався")

    def repair(self):
        self.is_working = True

    def refuel(self, fuel: int):
        self.fuel += fuel


# ======================================================================= #

# Завдання 4
# Створіть клас Студент з атрибутами:
#  ім’я
#  словник з предметами, де ключ – назва предмету, значення – список оцінок
# Додайте методи:
#  додати новий предмет
#  видалити предмет
#  вчити предмет(якщо отримана оцінка, то додати про це інформацію)
#  отримати середню оцінку за конкретним предметом
#  вивести загальну інформацію: ім’я та список предметів з середніми оцінками


class Student:
    def __init__(self, name: str):
        self.name = name

        self.subjects: Dict[str, List[int]] = {}

    def check_subject(self, subject):
        if subject not in self.subjects:
            print(f"Предмету {subject} не має в списку")
            return

    def add_subject(self, subject: str):
        if subject in self.subjects:
            print("Такий предмет вже є")
            return

        self.subjects[subject] = []

    def delete_subject(self, subject: str):
        self.check_subject(subject)

        del self.subjects[subject]

    def study_subject(self, subject: str, grade: int | None = None):
        self.check_subject(subject)

        if grade:
            self.subjects[subject].append(grade)

    def get_averege_grde(self, subject: str):
        self.check_subject(subject)

        sum_grades = 0

        for grade in self.subjects[subject]:
            sum_grades += grade

        if sum_grades == 0:
            return sum_grades

        return round(sum_grades / len(self.subjects[subject]), 2)

    def show_info(self):
        print(f"Імʼя студента: {self.name}\n")
        print("Список предметів:")

        for subject in self.subjects:
            print(
                f"\t{subject}: середня оцінка за предмет - {self.get_averege_grde(subject)}"
            )


student = Student("Jon")
student.add_subject("AI")
student.add_subject("Phyton")
student.study_subject("AI")
student.study_subject("AI", 2)
student.study_subject("Phyton")
student.study_subject("kjhkj")
student.show_info()

# ======================================================================= #

# Завдання 5
# Створіть клас Магазин з атрибутами:
#  назва
#  заробіток
#  словник з товарами, де ключ – назва товару, значення – кількість на складі
#  словник з товарами, де ключ – назва товару, значення – ціна
# Додайте методи:
#  вивід інформації: назва та список доступних товарів
#  поповнення складу певним товаром(може бути новий)
#  оформлення замовлення, якщо товар у достатній кількості доступний


class Shop:
    def __init__(self, name: str):
        self.name = name

        self.profit: float = 0
        self.products: Dict[str, int] = {}
        self.products_price: Dict[str, float] = {}

    def show_info(self):
        print(f"В магазині {self.name} доступні наступні товари:")

        for product in self.products:
            print(
                f"\t{product} у кількості - {self.products[product]}, за ціною {self.products_price[product]} грн"
            )

    def add_product(self, product: str, quantity: int, price: float | None = None):
        if product in self.products:
            self.products[product] += quantity

            if price:
                self.products_price[product] = price

            return

        self.products[product] = quantity

        if price is None:
            raise ValueError("Для нового товару необхідно вказати ціну")

        self.products_price[product] = price

    def make_order(self, product: str, quantity: int):
        if product not in self.products:
            print("Такого товару не має в магазині")
            return

        if quantity > self.products[product]:
            print(f"Магазині товару {product} не має в необхідній кількості")
            return

        self.products[product] -= quantity
        self.profit += self.products_price[product] * quantity
