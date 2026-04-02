# Завдання 1
# Створіть клас Student з атрибутами name та age. Додайте
# метод для виводу інформації у форматі «Ім’я: {name}, вік:
# {age}»


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


# ======================================================================= #

# Завдання 2
# Створіть список з 3-ма студентами, дані вводить
# користувач. Після чого для кожного студента виведіть
# інформацію про нього за допомогою метода.


def create_student():
    name = input("Введіть імʼя студента: ")
    age = int(input("Введіть вік студента: "))

    return Student(name, age)


def create_students():
    students = []

    print("Для виходу натисність 0")
    print("Для створення студента введіть 1")

    while True:
        action = int(input("Введіть неохідну дію: "))

        if action == 0:
            print("End")
            break

        if action != 1:
            print("Не вірно обрана дія: ")
            continue

        student = create_student()
        students.append(student)

    return students


students_test = create_students()

for student in students_test:
    student.show_info()

# ======================================================================= #

# Завдання 3
# Створіть клас Circle з атрибутом radius. Додайте метод для
# отримання площі кола


class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.14

    def get_area(self):
        return self.pi * self.radius**2


# ======================================================================= #

# Завдання 4
# Створіть клас BankAccount з атрибутами owner та balance.
# Додайте метод deposit для поповнення рахунку
# Додайте метод withdraw для зняття грошей з рахунку
# Додайте метод info для виведення інформації про баланс


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount < self.balance:
            print("Сума для зняття перевищує баланс")
        else:
            self.balance -= amount

    def show_info(self):
        print(f"У {self.owner} на рахунку {self.balance}")


# ======================================================================= #

# Завдання 5
# Створіть клас Car з атрибутами brand(марка), year(рік
# випуску), is_ready(чи готовий до поїздки, за замовчування
# False).
# Додайте метод start_engine який заводить двигун, і змінює
# атрибут is_ready
# Додайте метод move який виводить повідомлення, що
# автомобіль їде, або ж ще не готовий в залежності від is_ready.


class Car:
    def __init__(self, brand, year, is_ready=False):
        self.brand = brand
        self.year = year
        self.is_ready = is_ready

    def start_engine(self):
        self.is_ready = True

    def move(self, amount):
        if self.is_ready:
            print("Автомобіль їде")
        else:
            print("Автомобіль не готовий")


# ======================================================================= #

## Завдання 1 — Клас `BankCard` з лімітами та пін-кодом
# Створіть клас **BankCard** з атрибутами:
#
# *   `owner` — власник картки
# *   `balance` — поточний баланс
# *   `pin` — пін-код
# *   `daily_limit` — денний ліміт зняття грошей
# *   `withdrawn_today` — сума вже знятих за поточний день
# **Методи:**
# 1.  **Метод авторизації по пін-коду**
#     *   Логіка: перевіряє, чи співпадає введений код з піном картки. Якщо ні — доступ до операцій заборонено.
#     *   Параметри:
#         *   `self`
#         *   `entered_pin` — введений користувачем пін-код
# 2.  **
# **
#     *   Логіка: додає суму до балансу, але тільки якщо користувач уже авторизований.
#     *   Параметри:
#         *   `self`
#         *   `amount` — сума поповнення
# 3.  **Метод зняття грошей**
#     *   Логіка:
#         *   перевірити, чи авторизований користувач
#         *   перевірити, чи вистачає грошей на балансі
#         *   перевірити, чи не буде перевищено `daily_limit`
#         *   якщо все ок — зменшити баланс і збільшити `withdrawn_today`
#     *   Параметри:
#         *   `self`
#         *   `amount` — сума для зняття
# 4.  **Метод скидання денного ліміту** (наприклад, на початку нового дня)
#     *   Логіка: обнуляє `withdrawn_today`.
#     *   Параметри:
#         *   `self`


class BankCard:
    def __init__(self, owner, balance, pin, daily_limit, withdraw_today=10000):
        self.owner = owner
        self.balance = balance
        self.pin = pin
        self.daily_limit = daily_limit
        self.withdraw_today = withdraw_today
        self.is_authorized = False

    def authentication_pin(self, pin):
        if self.pin == pin:
            self.is_authorized = True
            print("Ви успішно авторизувались")
        else:
            print("Не вірно введено пін-код, спробуйте ще раз")

    def deposit(self, amount):
        if self.is_authorized:
            self.balance += amount
        else:
            print("Ви не авторизувались")

    def withdraw(self, amount):
        if not self.is_authorized:
            print("Ви не авторизувались")
            return

        if amount < self.balance:
            print("не вистачає грошей на балансі")
            return

        if self.withdraw_today > self.daily_limit:
            print("перевищено денний ліміт зняття грошей")
            return

        self.balance -= amount
        self.withdraw_today += amount

    def reset_withdraw_today(self, withdraw=10000):
        self.withdraw_today = withdraw
