import pytest
import time
import source.my_functions as my_functions

def test_add():
    result = my_functions.add(1, 4)
    assert result == 5

def test_sub():
    result = my_functions.sub(3, 1)
    assert result == 2

def test_multiple():
    result = my_functions.multiple(3, 7)
    assert  result == 21

def test_division():
    result = my_functions.divide(10, 2)
    assert result == 5

def test_divide_by_zero_error():
    with pytest.raises(ZeroDivisionError):
        my_functions.divide(10, 0)

def test_add_strings():
    result = my_functions.add("I like burgers ", "in the morning")
    assert  result == "I like burgers in the morning"

@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    result = my_functions.divide(10, 2)
    assert result == 5

@pytest.mark.skip(reason = "This feature is broken")
def test_add():
    result = my_functions.add(1, "America")
    assert result == 5

@pytest.mark.xfail(reason = "We know that we cannot divide a number with zero")
def test_divide_by_zero():
    my_functions.divide(100, 0)