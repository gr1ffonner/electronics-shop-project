import pytest


@pytest.fixture
def sample_data():
    data = [1, 2, 3, 4, 5]
    return data


def test_sum(sample_data):
    total = sum(sample_data)
    assert total == 15
