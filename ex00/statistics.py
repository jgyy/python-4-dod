from typing import Any, List, Union
import math

def ft_statistics(*args: Any, **kwargs: Any) -> None:
    def mean(numbers: List[Union[int, float]]) -> float:
        return sum(numbers) / len(numbers)

    def median(numbers: List[Union[int, float]]) -> float:
        sorted_numbers = sorted(numbers)
        n = len(sorted_numbers)
        if n % 2 == 0:
            return (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2
        else:
            return sorted_numbers[n//2]

    def quartile(numbers: List[Union[int, float]]) -> List[float]:
        sorted_numbers = sorted(numbers)
        n = len(sorted_numbers)
        return [sorted_numbers[n//4], sorted_numbers[(3*n)//4]]

    def std_dev(numbers: List[Union[int, float]]) -> float:
        avg = mean(numbers)
        variance = sum((x - avg) ** 2 for x in numbers) / len(numbers)
        return math.sqrt(variance)

    def variance(numbers: List[Union[int, float]]) -> float:
        avg = mean(numbers)
        return sum((x - avg) ** 2 for x in numbers) / len(numbers)

    if not args:
        for key in kwargs.values():
            print("ERROR")
        return

    numbers = [x for x in args if isinstance(x, (int, float))]

    if not numbers:
        for key in kwargs.values():
            print("ERROR")
        return

    for key, value in kwargs.items():
        if value == "mean":
            print(f"mean : {mean(numbers)}")
        elif value == "median":
            print(f"median : {median(numbers)}")
        elif value == "quartile":
            print(f"quartile : {quartile(numbers)}")
        elif value == "std":
            print(f"std : {std_dev(numbers)}")
        elif value == "var":
            print(f"var : {variance(numbers)}")
