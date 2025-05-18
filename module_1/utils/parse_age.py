from typing import Optional, Union


def parse_age(age_str: Optional[str]) -> Union[int, None]:
    if age_str is None:
        return None
    return int(age_str)



