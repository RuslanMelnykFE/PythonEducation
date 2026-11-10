# Завдання 1
# Напишіть програму для заповнення списку товарів.
# Назви товарів вводить користувач. Реалізуйте функціонал:
#  додати новий товар
#  вивести список товарів
#  зберегти дані через json
#  зберегти дані через pickle
#  завантажити дані через json
#  завантажити дані через pickle
import json
import pickle
from typing import Optional, List


def add_new_product(products: List[str]) -> None:
    product = input("Введіть назву товару")
    products.append(product)


def show_products(products: List[str]) -> None:
    print(f"Список продуктів: {', '.join(products)}")


def load_products_json() -> List[str]:
    try:
        with open("products.json", "r", encoding="utf-8") as f:
            return json.load(f)["products"]

    except FileNotFoundError:
        return []


def load_products_pickle() -> List[str]:
    try:
        with open("products.pickle", "rb") as f:
            return pickle.load(f)

    except FileNotFoundError:
        return []


def save_products_json(products: List[str]) -> None:
    data = {"products": products}

    with open("products.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        print("products.json saved")


def save_products_pickle(products: List[str]) -> None:
    with open("products.pickle", "wb") as f_in:
        pickle.dump(products, f_in)
        print("products.pickle saved")


def main():
    products = load_products_json()

    while True:
        print(
            "=============== МЕНЮ ====================\n"
            "Для додаваня продукту введіть 1\n"
            "Для виводу списку продуктів введіть 2\n"
            "Для виходу введіть 0\n"
            "=========================================\n"
        )

        action = int(input("Оберіть необхідну дію: "))

        if action < 0 or action > 2:
            print("Не вірно введено дію")
            continue

        if action == 1:
            add_new_product(products)
            save_products_json(products)
            save_products_pickle(products)
            products = load_products_json()

        elif action == 2:
            show_products(products)

        elif action == 0:
            print("Вихід")
            break


try:
    main()
except ValueError as e:
    print(e)


# Завдання 2
# Напишіть клас Student
# Атрибути:
#  name – ім’я
#  specialization – спеціалізація
#  grades – список оцінок
# Методи:
#  add_grade(grade) – додати нову оцінку
#  show_info() – вивести ім’я, спеціалізацію та середню
# оцінку
# Створіть список з трьох студентів. Збережіть цей список
# використовуючи pickle та json.
# Завантажте дані за допомогою pickle та json.


class Student:
    def __init__(
        self,
        name: str,
        specialization: str,
        grades: Optional[List[int]],
    ) -> None:
        self.name = name
        self.specialization = specialization

        if grades is None:
            self.grades = []
        else:
            self.grades = grades

    def add_grade(self, grade: int) -> None:
        self.grades.append(grade)

    def show_info(self) -> None:
        grades_str = ", ".join(str(grade) for grade in self.grades)
        print(
            f"Студент {self.name},\n"
            f"навчаєть на спеціалізації {self.specialization},\n"
            f"має оцінки: {grades_str}"
        )


def create_students() -> List[Student]:
    students = []

    for idx in range(3):
        student = Student(
            f"name_{idx + 1}",
            f"specialization {idx + 1}",
            [10, 2, 8],
        )
        students.append(student)

    return students


def save_students_json(students: List[Student]) -> None:
    data = {}

    for student in students:
        data[student.name] = {
            "specialization": student.specialization,
            "grades": student.grades,
        }

    with open("students.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        print("students.json saved")


def save_students_pickle(students: List[Student]) -> None:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
        print("students.pickle saved")


students = create_students()

save_students_json(students)
save_students_pickle(students)
