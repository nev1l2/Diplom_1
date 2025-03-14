import pytest
from unittest.mock import Mock
from Diplom_1.ingredient import Ingredient
from Diplom_1.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestForIngredient:

    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_FILLING, "Салат", 5.0),
        (INGREDIENT_TYPE_SAUCE, "Кетчуп", 3.5),
        (INGREDIENT_TYPE_FILLING, "Сыр", 10.0),
        (INGREDIENT_TYPE_SAUCE, "Тысяча островов", 2.0)
    ])
    def test_initialization(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price

    def test_get_price_mock(self):
        mock_get_price = Mock(return_value=10.0)
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "Курица", 5.0)
        ingredient.get_price = mock_get_price
        assert ingredient.get_price() == 10.0
        mock_get_price.assert_called_once()

    def test_get_name_mock(self):
        mock_get_name = Mock(return_value='Бекон')
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "Свинина", 8.0)
        ingredient.get_name = mock_get_name
        assert ingredient.get_name() == 'Бекон'
        mock_get_name.assert_called_once()

    def test_get_type_mock(self):
        mock_get_type = Mock(return_value=INGREDIENT_TYPE_SAUCE)
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "Майонез", 4.0)
        ingredient.get_type = mock_get_type
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE
        mock_get_type.assert_called_once()