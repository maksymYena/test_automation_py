from dataclasses import dataclass
from typing import List, Any

from pydantic import BaseModel


@dataclass
class Order:
    order_id: int
    customer: str
    items: List[str]
    total_price: float


orders = []
for i in range(0, 2):
    orders.append(Order(
        order_id=i,
        customer="Maksym",
        items=[
            f"item_{i}", f"item_{i + 1}", f"item_{i + 2}"
        ],
        total_price=i + 1.5
    ))

print(orders)


class ApiResponse(BaseModel):
    status: str
    code: int
    data: dict


api_call = ApiResponse(status="success", code="200", data={})

print(api_call)
