"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item_2 import Item
import pytest


@pytest.fixture
def csv_file():
    return "/home/danya/code/profi/kate/electronics-shop-project/src/items.csv"


def test_instantiate_from_csv(csv_file):
    items = Item.instantiate_from_csv(csv_file)

    # Assert the properties of the instantiated items
    assert len(Item.all) == 4
    assert items[0].name == "Смартфон"
    assert items[0].price == 100
    assert items[0].quantity == 1
    assert items[1].name == "samsung"
    assert items[1].price == 1000
    assert items[1].quantity == 3


def test_string_to_number():
    assert Item.string_to_number("15.0") == 15
    assert Item.string_to_number("7") == 7


def test_set_name_property_with_valid_value():
    item = Item("Valid Item", 10.0, 5)
    item.name = "New Name"
    assert item.name == "New Name"
