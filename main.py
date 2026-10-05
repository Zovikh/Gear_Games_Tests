from typing import List, TypeVar, Sequence

T = TypeVar('T')

def compress_numbers(numbers: Sequence[T]) -> List[T]:
    if not numbers:
        return []

    result = [numbers[0]]
    for i in range(1, len(numbers)):
        if numbers[i] != numbers[i - 1]:
            result.append(numbers[i])
    return result