"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item_1 import Item
import pytest


@pytest.fixture
def sample_items():
    a = Item("Sample Item 1", 10.0, 5)
    b = Item("Sample Item 2", 20.0, 3)
    return a, b


def test_calculate_total_price(sample_items):
    item1, item2 = sample_items
    assert item1.calculate_total_price() == 50.0
    assert item2.calculate_total_price() == 60.0


def test_apply_discount(sample_items):
    item1, item2 = sample_items
    item1.pay_rate = 0.8  # Applying a 20% discount
    item1.apply_discount()
    assert item1.price == 8.0
    assert item2.price == 20.0  # Discount not applied to item2


def test_apply_discount_with_default_pay_rate(sample_items):
    item1, _ = sample_items
    item1.apply_discount()
    assert item1.price == 10.0


def test_name_attribute(sample_items):
    item1, _ = sample_items
    assert item1.name == "Sample Item 1"


def test_price_attribute(sample_items):
    _, item2 = sample_items
    assert item2.price == 20.0


def test_quantity_attribute(sample_items):
    _, item2 = sample_items
    assert item2.quantity == 3


def test_all_list_contains_created_items(sample_items):
    assert sample_items[0] in Item.all
    assert sample_items[1] in Item.all
    assert len(sample_items) == 2


if __name__ == "__main__":
    pytest.main()
