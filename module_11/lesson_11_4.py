import datetime
from typing import List

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


def create_messages() -> List[Message] | None:
    messages = []

    for _ in range(4):
        user = input("Введіть імʼя автора: ")
        text = input("Введіть текст повідомлення: ")
        time = input("Введіть час повідомлення в форматі '%H:%M': ")

        messages.append(Message(user, text, time))

    if len(messages) == 0:
        return messages

    return messages.sort()


# test_messages = create_messages()
#
# for message in test_messages:
#     print(message)

# Завдання 2
# Створіть клас Song з атрибутами
#  name – назва пісні
#  author – ім’я автора
# методи:
#  __eq__(self, other) – перевіряє чи дві пісні однакові
#  __str__(self, other) – повертає рядок з назвою та автором
# Створіть клас Playlist з атрибутами
#  songs – список пісень(об’єкти класу Song)
# методи:
#  __len__(self) – повертає кількість пісень
#  __contains__(self, item) – перевіряє чи є пісня в плейлисті
#  __iter__(self) – повертає літератор для циклу for
#  add_song(self, song) – додає пісню в плейлист
#  remove_song(self, song) – видаляє пісню з плейлиста
# Створіть порожній плейлист
# Створіть 3 пісні:
# "Imagine", "John Lennon"
# "Bohemian Rhapsody", "Queen"
# "Shape of You", "Ed Sheeran"
# Добавте їх в плейлист
# Пройдіться циклом for по плейлисту та виведіть кожну
# пісню на екран


class Song:
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __eq__(self, other):
        if isinstance(other, Song):
            return self._name == other._name and self._author == other._author

        return False

    def __str__(self):
        return f"Пісня {self._name} автор - {self._author}"


class PlayList:
    def __init__(self, songs: List[Song]):
        self._songs = songs

    def __len__(self):
        return len(self._songs)

    def contains(self, song: Song):
        return song in self._songs

    def __iter__(self):
        return iter(self._songs)

    def add_song(self, song: Song):
        self._songs.append(song)

    def remove_song(self, song: Song):
        self._songs.remove(song)


def create_playlist() -> PlayList:
    songs = [
        Song("Imagine", "John Lennon"),
        Song("Bohemian Rhapsody", "Queen"),
        Song("Shape of You", "Ed Sheeran"),
    ]

    return PlayList(songs)


for song in create_playlist():
    print(song)
