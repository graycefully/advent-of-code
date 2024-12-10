from typing import List, Tuple
import copy

type Direction = Tuple[int, int]


def process_input() -> List[str]:
    with open('input.txt', 'r') as file:
        return [line.strip() for line in file.readlines()]


def initialize_seen(map: List[str]) -> Tuple[List[List[int]], int, int, Direction]:
    n, m = len(map), len(map[0])
    seen = [[0 for _ in range(m)] for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if map[x][y] == '#':
                seen[x][y] = 2
            elif map[x][y] == '^':
                seen[x][y] = 1
                cur_x, cur_y = x, y
                cur_dir = (-1, 0)
    return seen, cur_x, cur_y, cur_dir


def turn_right(cur_dir: Direction) -> Direction:
    return {
        (-1, 0): (0, 1),
        (0, 1): (1, 0),
        (1, 0): (0, -1),
        (0, -1): (-1, 0)
    }[cur_dir]


def traverse_seen(seen: List[List[int]], cur_x: int, cur_y: int, cur_dir: Direction) -> List[List[int]]:
    n, m = len(seen), len(seen[0])
    while 0 <= cur_x < n and 0 <= cur_y < m:
        if 0 <= cur_x + cur_dir[0] < n and 0 <= cur_y + cur_dir[1] < m:
            if seen[cur_x + cur_dir[0]][cur_y + cur_dir[1]] == 2:
                cur_dir = turn_right(cur_dir)
            cur_x += cur_dir[0]
            cur_y += cur_dir[1]
            seen[cur_x][cur_y] = 1
        else:
            break
    return seen


def gets_stuck(seen: List[List[int]], cur_x: int, cur_y: int, cur_dir: Direction) -> bool:
    visited = set()
    n, m = len(seen), len(seen[0])
    while 0 <= cur_x < n and 0 <= cur_y < m:
        next_x, next_y = cur_x + cur_dir[0], cur_y + cur_dir[1]
        if 0 <= next_x < n and 0 <= next_y < m:
            if seen[next_x][next_y] == 2:
                cur_dir = turn_right(cur_dir)
            else:
                cur_x, cur_y = next_x, next_y
                seen[cur_x][cur_y] = 1
        else:
            return False
        if (cur_x, cur_y, cur_dir) in visited:
            return True
        visited.add((cur_x, cur_y, cur_dir))
    return False


def part1() -> int:
    seen, cur_x, cur_y, cur_dir = initialize_seen(process_input())
    seen = traverse_seen(seen, cur_x, cur_y, cur_dir)
    return sum(num == 1 for row in seen for num in row)


def part2() -> int:
    obstructions = 0
    seen, cur_x, cur_y, cur_dir = initialize_seen(process_input())
    traversed = traverse_seen(seen, cur_x, cur_y, cur_dir)
    for x in range(len(traversed)):
        for y in range(len(traversed[0])):
            if traversed[x][y] == 1:
                seen_with_new_obstruction = copy.deepcopy(seen)
                seen_with_new_obstruction[x][y] = 2
                if gets_stuck(seen_with_new_obstruction, cur_x, cur_y, cur_dir):
                    obstructions += 1
    return obstructions


if __name__ == '__main__':
    print("Part One answer: " + str(part1()))
    print("Part Two answer: " + str(part2()))
