from operator import add, mul
from typing import Callable, List


def process_input() -> List[List[int]]:
    with open('input.txt', 'r') as file:
        return [list(map(int, line.replace(':', '').split())) for line in file.readlines()]


def concat(a: int, b: int) -> int:
    return int(f"{a}{b}")


def solve(numbers: List[int], operators: List[Callable]) -> int:
    if len(numbers) == 2:
        return numbers[0] == numbers[1]

    total, a, b, *rest = numbers
    for operator in operators:
        if solve([total, operator(a, b)] + rest, operators):
            return total
    return 0


def part1() -> int:
    return sum(solve(numbers, [add, mul]) for numbers in process_input())


def part2() -> int:
    return sum(solve(numbers, [add, mul, concat]) for numbers in process_input())


if __name__ == '__main__':
    print("Part One answer: " + str(part1()))
    print("Part Two answer: " + str(part2()))
