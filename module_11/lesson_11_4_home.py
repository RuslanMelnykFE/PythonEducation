# Завдання 1
# Створіть клас Recipe з атрибутами
#  name – назва страви
#  ingredients – список продуктів
#  text – текст рецепту
#  time – час приготування
# методи:
#  __str__(self) – повертає назву страви
#  __contains__(self, item) – перевіряє чи є інгредієнт в
# рецепті
#  __gt__(self, other) – перевіряє чи є час приготування self
# більшим за other
#  display_info(self) – виводить всю інформацію про рецепт
# Створіть декілька рецептів та добавте їх у список.
# Виведіть назви тих рецептів, які містять інгредієнт томат
# Виведіть повну інформацію рецепта з найменшим часом
# приготування, скористайтесь функцією min


class Recipe:
    def __init__(self, name: str, ingredients: list, text: str, time: int):
        self._name = name
        self._ingredients = ingredients
        self._text = text
        self._time = time

    def __str__(self):
        return f"Старава {self._name}"

    def __contains__(self, item):
        return item in self._ingredients

    def __gt__(self, other):
        return self._time > other._time

    def display_info(self):
        print(
            f"Страва - {self._name}.\n"
            f"До неї входять: {', '.join(self._ingredients)}.\n"
            f"Рецепт: \n{self._text}.\n"
            f"Час приготування - {self._time}."
        )


def create_recipes():
    recipe1 = Recipe(
        "Піца",
        ["борошно", "вода", "дріжджі", "томат", "сир"],
        "Готуємо тісто, додаємо інгредієнти та запікаємо",
        30,
    )

    recipe2 = Recipe(
        "Салат",
        ["томат", "огірок", "зелень", "олія"],
        "Нарізаємо овочі, додаємо зелень та поливаємо олією",
        10,
    )

    recipe3 = Recipe(
        "Суп",
        ["вода", "картопля", "морква", "м'ясо"],
        "Варимо всі інгредієнти до готовності",
        45,
    )

    return [recipe1, recipe2, recipe3]


def show_recipes():
    recipes = create_recipes()

    print("Страви із томатами:")
    for recipe in recipes:
        if "томат" in recipe:
            print(recipe)

    fast = min(recipes, key=lambda self: self._time)
    print("\n#========================================#\n")
    print("Страви із найменшим часом приготування:")
    fast.display_info()


show_recipes()
