# Створіть наступні класи:
#  CreditCardPayment – атрибути currency
#  PayPalPayment – атрибути currency
#  CryptoPayment – атрибути currency
# Методи:
#  pay(amount) – виводить повідомлення
# o CreditCardPayment – оплата карткою {amount}{currency}
# o PayPalPayment – оплата PayPal {amount}{currency}
# o CryptoPayment – оплата криптогаманцем {amount}{currency}
# Напишіть функцію create_payment() яка запитує у
# користувача тип рахунку та потрібні атрибути і повертає
# об’єкт.
# Створіть декілька рахунків, добавте їх у список та для
# кожної викличте відповідні методи.


class CreditCardPayment:
    def __init__(self, currency: str):
        self._currency = currency

    def pay(self, amount: float):
        print(f"Оплата карткою {amount} {self._currency}")


class PayPalPayment:
    def __init__(self, currency: str):
        self._currency = currency

    def pay(self, amount: float):
        print(f"Оплата PayPal {amount} {self._currency}")


class CryptoPayment:
    def __init__(self, currency: str):
        self._currency = currency

    def pay(self, amount: float):
        print(f"Оплата криптогаманцем {amount} {self._currency}")


def create_payment() -> CreditCardPayment | PayPalPayment | CryptoPayment | None:
    payment = input("Оберіть тип рахунку (Credit Card, PayPal, Crypto): ")
    currency = input("Введіть необхідну валюту: ")

    if payment.lower() == "credit card":
        return CreditCardPayment(currency)

    elif payment.lower() == "paypal":
        return PayPalPayment(currency)

    elif payment.lower() == "crypto":
        return CryptoPayment(currency)

    else:
        print("не вірно введено тип рахунку")
        return None


def create_payments() -> list:
    payments = []

    for _ in range(4):
        payment = create_payment()

        if payment:
            payments.append(payment)

    return payments


new_payments = create_payments()

for idx in range(len(new_payments)):
    new_payments[idx].pay(1000 * (idx + 1))
