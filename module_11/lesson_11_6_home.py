from abc import ABC
from typing import Optional, List


# Завдання 1
# Створіть клас Passenger з атрибутами
#  name – ім’я
#  destination – місце, куди прямує

# Завдання 2
# Створіть клас Transport з атрибутами
#  speed – швидкість
# Методи
#  move(destination, distance) – рухається до місця
# призначення, виводить інформацію як довго їхали

# Завдання 3
# Створіть клас Bus з атрибутами
#  passengers – список пасажирів(об’єкти класу Passenger)
#  capacity – максимальна можлива кількість пасажирів
# Методи
#  board_passenger(passenger) – якщо є місце, додає
# пасажира
#  move(destination, distance) – висаджує всіх пасажирів, які
# хочуть вийти в даному місці(виводить їхню загальну
# кількість) та викликає батьківський метод move()


class Passenger:
    def __init__(
        self,
        name: str,
        destination: str,
    ):
        self._name = name
        self.destination = destination


class Transport(ABC):
    def __init__(
        self,
        speed: int = 60,
    ):
        self._speed = speed

    def move(self, destination: str, distance: int):
        time = int(distance / self._speed)

        print(f"Рухається до: {destination}, час руху: {time}")


class Bus(Transport):
    def __init__(
        self,
        speed: int = 60,
        passengers: Optional[List[Passenger]] = None,
        capacity: int = 30,
    ):
        super().__init__(speed)

        if passengers is None:
            self._passengers = []
        else:
            self._passengers = passengers

        self._capacity = capacity

    def board_passenger(self, passenger: Passenger):
        if len(self._passengers) >= self._capacity:
            print("Вільних місць не має")
            return

        self._passengers.append(passenger)

    def move(self, destination: str, distance: int):
        passengers_leave = []
        remaining_passengers = []

        for passenger in self._passengers:
            if passenger.destination == destination:
                passengers_leave.append(passenger)
            else:
                remaining_passengers.append(passenger)

        print(f"В {destination} вийшло {len(passengers_leave)} пасажирів")

        self._passengers = remaining_passengers

        super().move(destination, distance)
