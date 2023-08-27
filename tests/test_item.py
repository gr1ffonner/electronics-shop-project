"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest


@pytest.fixture
def sample_item():
    return Item("Sample Item", 10.0, 5)


def test_calculate_total_price(sample_item):
    assert sample_item.calculate_total_price() == 50.0


def test_apply_discount(sample_item):
    sample_item.pay_rate = 0.8  # Applying a 20% discount
    sample_item.apply_discount()
    assert sample_item.price == 8.0


def test_apply_discount_with_default_pay_rate(sample_item):
    sample_item.apply_discount()
    assert sample_item.price == 10.0


def test_name_attribute(sample_item):
    assert sample_item.name == "Sample Item"


def test_price_attribute(sample_item):
    assert sample_item.price == 10.0


def test_quantity_attribute(sample_item):
    assert sample_item.quantity == 5


if __name__ == "__main__":
    pytest.main()
