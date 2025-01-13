from Diplom_1.ingredient import Ingredient
from Diplom_1.ingredient_types import INGREDIENT_TYPE_FILLING


class TestForBurger:

    # Выбор булочки (установка)
    def test_set_buns(self, burger, bun):
        burger.set_buns(bun)
        assert burger.bun == bun

    # Добавление ингредиента
    def test_add_ingredient(self, burger, ingredient):
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient

    # Удаление ингредиента
    def test_remove_ingredient(self, burger, ingredient):
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    # Перемещение ингредиента
    def test_move_ingredient(self, burger, ingredient):
        burger.add_ingredient(ingredient)
        ingredient2 = Ingredient(ingredient_type=INGREDIENT_TYPE_FILLING, name='Помидор', price=20.0)
        burger.add_ingredient(ingredient2)

        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == ingredient2
        assert burger.ingredients[1] == ingredient

    # Расчет стоимости
    def test_get_price(self, burger, ingredient):
        burger.add_ingredient(ingredient)
        expected_price = (burger.bun.get_price() * 2) + ingredient.get_price()
        assert burger.get_price() == expected_price

    # Формирование чека
    def test_get_receipt(self, burger, ingredient):
        burger.add_ingredient(ingredient)
        expected_receipt = (
            f'(==== {burger.bun.get_name()} ====)\n'
            f'= {ingredient.get_type().lower()} {ingredient.get_name()} =\n'
            f'(==== {burger.bun.get_name()} ====)\n'
            '\n'
            f'Price: {burger.get_price()}'
        )

        actual_receipt = burger.get_receipt()
        assert actual_receipt == expected_receipt


