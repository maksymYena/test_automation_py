from typing import Dict, Optional, Union, List


def multiply(a: int, b: int) -> int:
    return a * b


def get_user_name(user: Dict[str, str]) -> str:
    return user.get("name", "").upper()


def length_or_negative(string: Optional[str]) -> Union[int, None]:
    if string is None:
        return -1
    else:
        return len(string)


class StringTools:
    def __init__(self, base: str):
        self.base = base

    def split_and_filter(self, separator: str) -> List[str]:
        return [x for x in self.base.split(separator) if x]
