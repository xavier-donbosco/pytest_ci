import source.my_functions as my_functions
import pytest

@pytest.mark.parametrize("actual_value1, actual_value2, expected_value", [(1, 2, 3), (4, 5, 9), (11, 12, 23)])
def test_multiple_additions(actual_value1, actual_value2, expected_value):
    assert my_functions.add(actual_value1, actual_value2) == expected_value

@pytest.mark.parametrize("actual_value1, actual_value2, expected_value", [(2, 1, 1), (3, 2, 1), (7, 2, 5)])
def test_multiple_subtractions(actual_value1, actual_value2, expected_value):
    assert my_functions.sub(actual_value1, actual_value2) == expected_value