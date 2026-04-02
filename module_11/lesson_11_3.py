import math

# Завдання 1
# Створіть наступні класи:
#  Rectangle – атрибути width, height
#  Circle – атрибути radius
#  Triangle – атрибути a, b, c
# Методи:
#  get_perimeter()
#  display_info()
# Напишіть функцію create_figure() яка запитує у користувача
# тип фігури та потрібні атрибути і повертає об’єкт.
# Створіть декілька фігур, добавте їх у список та для кожної
# викличте відповідні методи.


class Rectangle:
    def __init__(self, width: float, height: float):
        self._width = width
        self._height = height

    def get_perimeter(self) -> float:
        return (self._width + self._height) * 2

    def display_info(self):
        print(f"Ширина: {self._width}\n" f"Висота: {self._height}")


class Circle:
    def __init__(self, radius: float):
        self._radius = radius

    def get_perimeter(self) -> float:
        return self._radius * math.pi * 2

    def display_info(self):
        print(f"Радіус: {self._radius}")


class Triangle:
    def __init__(self, a: float, b: float, c: float):
        self._a = a
        self._b = b
        self._c = c

    def get_perimeter(self) -> float:
        return self._a + self._b + self._c

    def display_info(self):
        print(
            f"Сторона a: {self._a}\n" f"Сторона b: {self._b}\n" f"Сторона c: {self._c}"
        )


def create_figure() -> Rectangle | Circle | Triangle | None:
    figure = input("Оберіть тип фігури (rectangle, circle, triangle): ")

    if figure == "rectangle":
        width = float(input("Введіть значення ширини прямокутника: "))
        height = float(input("Введіть значення висоти прямокутника: "))

        return Rectangle(width, height)

    if figure == "circle":
        radius = float(input("Введіть значення радіуса кола: "))

        return Circle(radius)

    if figure == "triangle":
        a = float(input("Введіть значення довжини сторони a трикутника: "))
        b = float(input("Введіть значення довжини сторони b трикутника: "))
        c = float(input("Введіть значення довжини сторони c трикутника: "))

        return Triangle(a, b, c)

    print("не вірно введено назву фігури")
    return None


def create_figures():
    figures = []

    for _ in range(4):
        figure = create_figure()

        if figure:
            figures.append(figure)

    return figures


# figures = create_figures()

# ======================================================================= #

# Завдання 2
# Створіть наступні класи:
#  Manager – атрибути name, base_salary
#  Developer – атрибути name, base_salary, work_experience
#  Inter – атрибути name, base_salary
# Методи:
#  get_salary() – менеджер отримує базову ставку,
# розробник отримує на 20% більше якщо стаж більше 4
# років, інтерн отримує половину базової ставки
# Напишіть функцію create_worker() яка запитує у
# користувача тип працівника та потрібні атрибути і повертає
# об’єкт.
# Створіть декілька співробітників, добавте їх у список та для
# кожного викличте відповідні методи.


class Manager:
    def __init__(self, name: str, base_salary: float):
        self._name = name
        self._base_salary = base_salary

    def get_salary(self) -> float:
        return self._base_salary


class Developer:
    def __init__(self, name: str, base_salary: float, work_experience: float):
        self._name = name
        self._base_salary = base_salary
        self._work_experience = work_experience
        self._base_year = 4
        self._percent = 1.2

    def get_salary(self) -> float:
        if self._work_experience > self._base_year:
            return round(self._base_salary * self._percent, 2)

        return self._base_salary


class Intern:
    def __init__(self, name: str, base_salary: float):
        self._name = name
        self._base_salary = base_salary

    def get_salary(self) -> float:
        return round(self._base_salary / 2, 2)


def create_worker():
    worker = input("Оберіть тип працівника (Manager, Developer, Intern): ")
    name = input("Введіть імʼя працівника: ")
    base_salary = float(input("введіть базову ставку працівника: "))

    if worker.lower() == "manager":
        return Manager(name, base_salary)

    if worker.lower() == "developer":
        work_experience = float(input("Введіть досвід роботи користувача: "))

        return Developer(name, base_salary, work_experience)

    if worker.lower() == "intern":
        return Intern(name, base_salary)

    print("не вірно введено тип працівника")
    return None


def create_workers():
    workers = []

    for _ in range(4):
        worker = create_worker()

        if worker:
            workers.append(worker)

    return workers


# workers = workers()
