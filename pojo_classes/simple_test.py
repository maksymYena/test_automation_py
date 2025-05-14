import pytest
import requests

from pojo_classes.simple_pojo import UserData


@pytest.mark.parametrize(
    "user_id, expected_email",
    [
        (1, "george.bluth"),
        (2, "janet.weaver"),
        (3, "emma.wong"),
        (4, "eve.holt"),
        (5, "charles.morris")
    ]
)
def test_user_id(user_id, expected_email):
    url = f"https://reqres.in/api/users/{user_id}"
    response = requests.get(url)
    if 200 < response.status_code < 300:
        response = response.json()
        user = UserData(**response.get("data"))
        assert expected_email in user.email, f"Expected '{expected_email}' to be in '{user.email}'"
