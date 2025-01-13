import pytest

from Diplom_1.bun import Bun


class TestForBun:

    # тест на проверку длинны имени булочки
    @pytest.mark.parametrize("name_bun, price", [('Я',50), ('Он', 50), ('Классная', 50), ('Супердлинноеназваниебулочки', 50)])
    def test_get_name(self, name_bun, price):
        bun = Bun(name_bun, price)
        assert bun.get_name() == name_bun

    # тест на проверку назначения цены
    @pytest.mark.parametrize('name_bun, price', [('Кунжутная №1', 50.0), ('Кунжутная №1', 0.5), ('Кунжутная №1', 999999.99)])
    def test_get_price(self, name_bun, price):
        bun = Bun(name_bun, price)
        assert bun.get_price() == price

    # тест на проверку типа переменной price
    def test_price_type(self):
        bun = Bun("Кунжутная №-1", 50.0)
        assert isinstance(bun.get_price(), float)

    # тест на проверку типа переменной name
    def test_name_type(self):
        bun = Bun("Кунжутная №-1", 50.0)
        assert isinstance(bun.get_name(), str)



