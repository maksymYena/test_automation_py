from typing import Optional

from pydantic import BaseModel, field_validator


def safe_divide(a: float, b: float) -> Optional[float]:
    result = 0.0
    try:
        result = a / b
    except ZeroDivisionError:
        print("Division by zero!")
        return None
    else:
        return result


class Item(BaseModel):
    name: str
    price: float

    @field_validator("price")
    def price_must_be_positive(cls, price_value):
        if price_value < 0:
            raise ValueError("Price cannot be less than 0")
        return price_value


with open("test_file", "w") as file_to_write:
    file_to_write.write("Hello, automation")

with open("test_file", "r") as file_to_read:
    content = file_to_read.read()
    print(content)
