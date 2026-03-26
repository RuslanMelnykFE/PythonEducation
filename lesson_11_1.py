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
