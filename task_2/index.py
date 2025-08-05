import re
from typing import Callable, Generator


def generator_numbers(txt: str) -> Generator[float, None, None]:

    float_pattern = r'-?\d+(?:\.\d+)?'
    matches = re.finditer(float_pattern, txt)
    for match in matches:
        yield float(match.group())


def sum_profit(txt: str, number_extractor: Callable[[str], Generator[float, None, None]]) -> float:

    return sum(number_extractor(txt))


# Тестовий текст
text = (
    "Загальний дохід працівника складається з декількох частин: 1000.01 "
    "як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 "
    "доларів."
)
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
