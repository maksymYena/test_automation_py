import pytest

from automation_project.utils.exceptions_and_context_managers import Item
from automation_project.utils.exceptions_and_context_managers import safe_divide
from automation_project.utils.greeting import say_hello
from automation_project.utils.task_type import length_or_negative


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
