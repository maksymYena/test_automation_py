# Задание 1 — List comprehension
# Создай список из квадратов всех чётных чисел от 0 до 20 включительно:
from typing import List

even_squares = [value for value in range(0, 20) if value % 2 == 0]
print(even_squares)

# 🔸 Задание 2 — Dict comprehension
# Сделай словарь {"user_1": 1, "user_2": 2, ..., "user_5": 5}:

users = {f"user_{user}": user for user in range(1, 6)}
print(users)

# 🔸 Задание 3 — zip в тесте
# Объедини списки имён и ролей в пары:

names = ["Alice", "Bob"]
roles = ["admin", "user"]

paired = [(name, role) for name, role in zip(names, roles)]
print(paired)


# 🔸 Задание 4 — Генератор
# Напиши генератор, который отдаёт строки "test_0", "test_1" ... "test_4":

def count_up_to(n: int):
    for i in range(0, n):
        yield f"test_{i}"


# Задание 5 — enumerate в логировании

steps = ["Open page", "Login", "Click submit"]

for id, step in enumerate(steps, start=1):
    print(id, step)


# Задание:
# Сделай генератор, который:
# принимает список имён (["Maksym", "Tanya"])
# возвращает строку вида: "Hello, Maksym!", "Hello, Tanya!"

def greeting_via_generator(names: List[str]):
    for name in names:
        yield f"Hello, {name}"


names = (["Maksym", "Tanya"])

for message in greeting_via_generator(names):
    print(message)

steps = ["Open login page", "Enter credentials", "Click login", "Verify dashboard"]

for id, item in enumerate(steps, start=1):
    print(f"Step {id}:", item)


def step_logger(steps: List[str]):
    for id, step in enumerate(steps, start=1):
        yield f"Step {id}: {step}"


for line in step_logger(steps):
    print(line)
