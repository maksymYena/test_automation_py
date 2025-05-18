import pytest

from module_1.utils.exceptions_and_context_managers import Item
from module_1.utils.exceptions_and_context_managers import safe_divide
from module_1.utils.greeting import say_hello
from module_1.utils.task_type import length_or_negative


def test_greeting():
    assert say_hello("Tetiana") == "Hello, Tetiana!"


def test_str_length():
    assert length_or_negative("hello") == 5
    assert length_or_negative(None) == -1


def test_division():
    assert safe_divide(10, 2) == 5.0
    assert safe_divide(10, 0) == None


def test_price_validator():
    with pytest.raises(ValueError, match="Price cannot be less than 0"):
        Item(name="Phone", price=-1)
