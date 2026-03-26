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
# Завдання 4
# Створіть клас BankAccount з атрибутами owner та balance.
# Додайте метод deposit для поповнення рахунку
# Додайте метод withdraw для зняття грошей з рахунку
# Додайте метод info для виведення інформації про баланс
