# Завдання 1
# Створіть клас Cart(кошик клієнта магазину) з атрибутами
# client(ім’я клієнта) та items(список товарів).
# Додайте метод який додає новий товар до кошика
# Додайте метод який видаляє товар з кошика
# Додайте метод для виведення інформації про кошик


class Cart:
    def __init__(self, client: str, items: list):
        self.client = client
        self.items = items

    def add_product(self, product):
        self.items.append(product.lower())
        print(f"{self.client}, Ви додалили {product} в кошик")

    def remove_product(self, product):
        if product.lower() not in self.items:
            print("Такого товару не має в кошику")
            return

        self.items.remove(product.lower())
        print(f"{self.client}, Ви видалили {product} із кошика")

    def show_card(self):
        print(f"{self.client} у Вас в кошику: {', '.join(self.items)}")


def action_cart():
    cart = Cart("Jon", ["хліб", "вода", "молоко"])
    cart.add_product("сир")
    cart.remove_product("sdasdf")
    cart.remove_product("Хліб")
    cart.show_card()


# action_cart()

# ======================================================================= #

# Завдання 2
# Створіть клас Phone з атрибутами number та battery_level.
# Додайте метод який зменшує заряд телефона(на скільки
# зменшити відсотків передається як параметр), якщо він
# опуститься нижче 20%, вивести повідомлення
# Додайте метод для виведення інформації про телефон.


class Phone:
    def __init__(self, number, battery_level: int):
        self.number = number
        self.battery_level = battery_level

    def drain_battery(self, percent: int):
        if self.battery_level == 0:
            print("Заряд телефону 0%")
            return

        if self.battery_level < percent:
            self.battery_level = 0
            print("Телефон повністю розряджено")
            return

        self.battery_level -= percent
        print(f"Рівень заряду: {self.battery_level}%")

        if self.battery_level < 20:
            print("Заряд телефону нижче 20%")

    def show_phone_info(self):
        print(
            f"Телефон: "
            f"номер: {self.number} "
            f"рівень заряду: {self.battery_level}%"
        )


def action_phone():
    phone = Phone("+380911234567", 30)
    phone.drain_battery(5)
    phone.show_phone_info()
    phone.drain_battery(10)
    phone.show_phone_info()
    phone.drain_battery(10)
    phone.show_phone_info()
    phone.drain_battery(10)
    phone.show_phone_info()


action_phone()
