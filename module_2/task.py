import requests

# 🔸 Задание 1. Сделай GET-запрос и распечатай:
# - статус-код,
# - заголовки ответа,
# - JSON тело.
# URL: https://jsonplaceholder.typicode.com/posts/5

URL = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(
    url=f"{URL}/5"
)

print(response.status_code)
print(response.headers)
print(response.json())

# 🔸 Задание 2. Отправь POST-запрос с json телом:

data = {
    "title": "QA Test",
    "body": "This is a test body",
    "userId": 99
}

response = requests.post(
    url=URL,
    data=data
)

print(response.json())
print(response.status_code)