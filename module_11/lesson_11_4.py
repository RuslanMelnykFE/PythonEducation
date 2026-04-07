import datetime

# Завдання 1
# Створіть клас Message з атрибутами
#  user – ім’я автора повідомлення
#  text – текст повідомлення
#  time – час повідомлення(використайте модуль datetime)
# приклад datetime.strptime('10:23', '%H:%M')
# методи:
#  __str__(self) – повертає текст повідомлення та час
#  __len__(self) – повертає довжину повідомлення
#  __gt__(self, other) – перевіряє чи є повідомлення self
# старішим за other
# Створіть список з декількома повідомленнями та виведіть
# його. Відсортуйте список і знову виведіть


class Message:
    def __init__(self, user: str, text: str, time: str):
        self._user = user
        self._text = text
        self._time = datetime.datetime.strptime(time, "%H:%M")

    def __str__(self):
        return f"{self._user}: {self._text} at {self._time}"

    def __len__(self):
        return len(self._text)

    def __gt__(self, other):
        return self._time < other._time


def create_messages():
    messages = []

    for __ in range(4):
        user = input("Введіть імʼя автора: ")
        text = input("Введіть текст повідомлення: ")
        time = input("Введіть час повідомлення в форматі '%H:%M': ")

        messages.append(Message(user, text, time))

    return messages.sort()


test_messages = create_messages()

for message in test_messages:
    print(message)
