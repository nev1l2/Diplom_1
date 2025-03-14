
class TestForDatabase:

    def test_available_buns_length(self, database):
        assert len(database.available_buns()) == 3


    def test_available_ingredients_length(self, database):
        assert len(database.available_ingredients()) == 6