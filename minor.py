from typing import Generator, Callable

def generator_numbers(text: str) -> Generator[float, None, None]:
    parts = text.split()
    for i, word in enumerate(parts):
        if i == 0 or i == len(parts) - 1:
            continue
        try:
            yield float(word)
        except ValueError:
            continue

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    return sum(func(text))


text = "Загальний дохід працівника складається з: 1000.01 як основний дохід, доповнений 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

