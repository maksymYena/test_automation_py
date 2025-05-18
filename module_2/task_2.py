import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry

# 🔸 Задание 1. Попробуй timeout:

try:
    response = requests.get("https://httpbin.org/delay/5", timeout=2)
    print(response.status_code)
except requests.exceptions.Timeout:
    print("⚠️ Запрос превысил лимит времени")

# 🔸 Задание 2. Используй Session и params:
# Создай сессию
#
# Добавь заголовок Authorization: Bearer testtoken
#
# Сделай GET-запрос на: https://httpbin.org/get?param=test

URL = "https://httpbin.org/get?param=test"

session = requests.Session()

session.headers.update({"Authorization": "Bearer testtoken"})

response = requests.get(
    url=URL
)
print(response.json()["url"])
print(response.headers)

# 🔸 Задание 3. Подключи retries:
# Сделай 3 попытки запроса на https://httpbin.org/status/503
# → Убедись, что Retry сработал.

retry = Retry(
    total=3,
    backoff_factor=0.5,
    status_forcelist=[503],
    allowed_methods=["GET", "POST"]
)

adapter = HTTPAdapter(max_retries=retry)
session.mount("https://", adapter)
session.mount("http://", adapter)

response = session.get("https://httpbin.org/status/503")