from abc import ABC
from enum import Enum
from uuid import uuid4


# Завдання 1
# Створіть абстрактний клас Robot з атрибутами:
#  name – назва робота або id
#  battery_level – рівень заряду(за замовчуванням 100%)
#  status – поточний стан (один з on, off, working)
# Методи:
#  info() – виводить інформацію
#  charge() – відновлює заряд до 100%
#  turn_on() – змінює стан на on
#  turn_off() – змінює стан на off


class Status(Enum):
    on = "on"
    off = "off"
    working = "working"


class CleaningMode(Enum):
    dry = "dry"
    wet = "wet"


class CleaningRobotError(Exception):
    pass


class Robot(ABC):
    def __init__(
        self,
        name: str,
        battery_level: int = 100,
        status: Status = Status.off,
    ):
        if len(name) == 0:
            self._name = str(uuid4())
        else:
            self._name = name

        self._battery_level = battery_level
        self._status = status

    def show_info(self):
        print(
            f"Robot {self._name}, battery level: {self._battery_level}, status: {self._status}"
        )

    def charge(self):
        self._battery_level = 100

    def turn_on(self):
        self._status = Status.on

    def turn_off(self):
        self._status = Status.off


# Завдання 2
# Створіть дочірній клас CleaningRobot
# Додаткові атрибути:
#  dust_capacity – ємність контейнеру для пилу(за
# замовчуванням 0%)
#  water_capacity – ємність контейнеру для води(за
# замовчуванням 100%)
#  cleaning_mode – тип прибирання(вологе або сухе)
# Методи:
#  info() – додатково виводить інформацію про робота
#  turn_on() – якщо контейнер для пилу повний або
# контейнер для води порожній то виводить повідомлення,
# інакше запускається turn_on() з класу Robot
#  empty_dustbin() – очищає контейнер для пилу
#  fill_water() – заповнює контейнер для води
#  swap_mode() – змінює тип прибирання на протилежний
#  clean(energy, dust, water=None) – чистить поверхню,
# якщо прибирання сухе, то просто перенести пил у
# контейнер(якщо місця не достатньо вивести помилку),
# якщо прибирання вологе то додатково витратити воду.
# Також зменшує рівень заряду на energy


class CleaningRobot(Robot):
    def __init__(
        self,
        name: str,
        battery_level: int = 100,
        status: Status = Status.off,
        dust_capacity: int = 0,
        water_capacity: int = 100,
        cleaning_mode: CleaningMode = CleaningMode.dry,
    ):
        super().__init__(name, battery_level, status)

        self._dust_capacity = dust_capacity
        self._water_capacity = water_capacity
        self._cleaning_mode = cleaning_mode

    def show_info(self):
        super().show_info()

        print(
            f"Cleaning mode: {self._cleaning_mode.name},"
            f"dust capacity: {self._dust_capacity},"
            f"water capacity: {self._water_capacity}"
        )

    def turn_on(self):
        if self._dust_capacity == 100:
            print("Dust capacity is 100")
            return

        if self._water_capacity == 0:
            print("Water capacity is 0")
            return

        super().turn_on()

    def empty_dustbin(self):
        self._dust_capacity = 0

    def fill_water(self):
        self._water_capacity = 100

    def swap_mode(self):
        if self._cleaning_mode == CleaningMode.dry:
            self._cleaning_mode = CleaningMode.wet
        else:
            self._cleaning_mode = CleaningMode.dry

    def clean(self, energy, dust, water=None):
        self._battery_level -= energy

        if self._battery_level <= 0:
            self._battery_level = 0
            self.turn_off()
            print("Battery level is 0, robot turned off")
            return

        if self._cleaning_mode == CleaningMode.wet:
            if water is None:
                self._water_capacity -= 2
            else:
                self._water_capacity -= water

            if self._water_capacity <= 0:
                self._water_capacity = 0
                raise CleaningRobotError("Water capacity is 0")

            return

        self._dust_capacity += dust

        if self._dust_capacity >= 100:
            self._dust_capacity = 100
            raise CleaningRobotError("Dust capacity is 100")
