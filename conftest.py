import pytest
from Diplom_1.bun import Bun
from Diplom_1.database import Database
from Diplom_1.ingredient import Ingredient
from Diplom_1.burger import Burger
from Diplom_1.ingredient_types import INGREDIENT_TYPE_FILLING


@pytest.fixture
def bun():
    return Bun(name='Классическая с кунжутом', price=50.0)


@pytest.fixture
def ingredient():
    return Ingredient(ingredient_type=INGREDIENT_TYPE_FILLING, name='Огурец', price=15.0)


@pytest.fixture
def burger(bun):
    burger = Burger()
    burger.set_buns(bun)
    return burger

@pytest.fixture()
def database():
    database = Database()
    return database