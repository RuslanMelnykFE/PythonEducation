from abc import ABC, abstractmethod
from typing import List


# Завдання 1
# Створіть абстрактний клас Character, атрибути
#  name – ім’я
#  max_hp – максимальний рівень здоров’я
#  hp – нинішній рівень здоров’я
#  level – рівень персонажа(від 1 до 20)
#  intelligence – стат інтелекту
#  strength – стат сили
#  dexterity – стат спритності
#  mana – стат мани
#  defense – стат захисту
# Методи:
#  attack() – абстрактний метод
#  take_damage(damage) – отримує урон, зменшений на
# захист
#  level_up() – збільшує рівень
#  increase_stat(stat) – збільшує один з статів на 1
#  rest() – відпочинок(відновлює hp до максимального)
#  heal(heal_hp) – збільшує hp на heal_hp


class CharacterTextError(Exception):
    pass


class CharacterNumError(Exception):
    pass


class Character(ABC):
    def __init__(
        self,
        name: str,
        hp: int,
        intelligence: int,
        strength: int,
        dexterity: int,
        mana: int,
        defense: int,
        level: int = 1,
    ):
        self._check_text(name)
        self._check_num(hp)
        self._check_num(intelligence)
        self._check_num(strength)
        self._check_num(dexterity)
        self._check_num(mana)
        self._check_num(defense)
        self._check_num(level)

        self._name = name
        self._max_hp = hp
        self._hp = hp
        self._level = level
        self._intelligence = intelligence
        self._strength = strength
        self._dexterity = dexterity
        self._mana = mana
        self._defense = defense

    @staticmethod
    def _check_text(text: str):
        if text == "":
            raise CharacterTextError("text cannot be empty")

    @staticmethod
    def _check_num(num: int):
        if num < 0:
            raise CharacterNumError("Число має бути додатнє")

    @abstractmethod
    def attack(self) -> int:
        raise NotImplementedError()

    def take_damage(self, damage: int):
        damage -= self._defense

        if damage > 0:
            self._hp -= damage

    def level_up(self):
        if self._level < 20:
            self._level += 1

    def increase_stat(self, stat: str):
        if stat == "intelligence":
            self._intelligence += 1
        elif stat == "strength":
            self._strength += 1
        elif stat == "dexterity":
            self._dexterity += 1
        elif stat == "mana":
            self._mana += 1

    def rest(self):
        self._hp += self._max_hp

    def heal(self, heal_hp: int):
        self._hp += heal_hp

        if self._hp > self._max_hp:
            self._hp = self._max_hp


# Завдання 2
# Практичне завдання
# Створіть дочірній клас Paladin
# Методи:
#  attack() – наносить 4*strength урону та зменшує mana на
# 5, якщо недостатньо, то наносить strength урону
#  shield() – збільшує стат defense на 4+level
#  unshield() – зменшує стат defense на 4+level
#  heal_ally(ally) – лікує союзника на 5 + 2*level + 0.5*mana


class Paladin(Character):
    def attack(self) -> int:
        if self._mana >= 5:
            self._mana -= 5
            return 4 * self._strength

        return self._strength

    def shield(self):
        self._defense += 4 + self._level

    def unshield(self):
        self._defense -= 4 + self._level

        if self._defense < 0:
            self._defense = 0

    def heal_ally(self, ally: Character):
        heal_hp = 5 + 2 * self._level + 0.5 * self._mana
        ally.heal(int(heal_hp))


# Завдання 3
# Створіть дочірній клас Mage
# Методи:
#  attack() – наносить 3*intelligence+4 урону та зменшує
# mana на 3, якщо недостатньо, то не наносить урону
#  fireball() – наносить 2*intelligence+3 урону по області та
# зменшує mana на 5, якщо недостатньо, то не наносить
# урону
#  heal_ally(ally) – лікує союзника на 3 + level +
# 3*intelligence


class Mage(Character):
    def attack(self) -> int:
        if self._mana >= 3:
            self._mana -= 3
            return 3 * self._intelligence + 4

        return 0

    def fireball(self):
        if self._mana >= 5:
            self._mana -= 5
            return 2 * self._intelligence + 3

        return 0

    def heal_ally(self, ally: Character):
        heal_hp = 3 + self._level + 3 * self._intelligence
        ally.heal(heal_hp)


# Завдання 4
# Створіть дочірній клас Warrior
# Методи:
#  attack() – наносить 4*strength+3 урону
#  power_strike(enemies) – проходить по списку ворогів:
# якщо їхній рівень менший за рівень персонажа, то
# знищує його повністю


class Warrior(Character):
    def attack(self) -> int:
        return 4 * self._strength + 3

    def power_strike(self, enemies: List[Character]):
        for enemy in enemies:
            if enemy._hp < self._hp:
                enemy._hp = 0


# Завдання 5
# Створіть дочірній клас Rogue
# Методи:
#  attack() – наносить strength+level урону


class Rogue(Character):
    def attack(self) -> int:
        return self._strength + self._level
