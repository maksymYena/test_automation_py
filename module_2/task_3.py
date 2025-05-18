import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry


class Timeout(requests.Session):

    def __init__(self, timeout: int = 3):
        super().__init__()
        self.timeout = timeout

    def request(self, method, url, **kwargs):
        if "timeout" not in kwargs:
            kwargs["timeout"] = self.timeout
        return super().request(method=method, url=url, **kwargs)


session = Timeout(timeout=2)

retry = Retry(
    total=3,
    backoff_factor=0.5,
    status_forcelist=[503],
    allowed_methods=["GET"]
)

adapter = HTTPAdapter(max_retries=retry)
session.mount("https://", adapter)
session.mount("http://", adapter)

try:
    response = session.get(url="https://httpbin.org/cookies/set/sessioncookie/abc123")
    print("[INFO] Установили куку:", response.status_code)

    response = session.get(url="https://httpbin.org/cookies")
    print("[INFO] Полученные куки:", response.json())

    response = session.get(url="https://httpbin.org/delay/5")
except requests.exceptions.Timeout:
    print("[WARNING] Таймаут сработал")
except requests.exceptions.RetryError:
    print("[WARNING] RetryError: сервер недоступен")
except requests.exceptions.ConnectionError:
    print("[WARNING] ConnectionError: ошибка соединения")
