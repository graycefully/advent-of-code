from typing import Dict, List, Set, Tuple

type Position = Tuple[int, int]


def process_input() -> List[str]:
    with open('input.txt', 'r') as file:
        return [line.strip() for line in file.readlines()]


def find_antennas(data: List[str]) -> Dict[str, List[Position]]:
    antennas = {}
    for x, row in enumerate(data):
        for y, char in enumerate(row):
            if char != '.':
                if char not in antennas:
                    antennas[char] = []
                antennas[char].append((x, y))
    return antennas


def find_antinodes(antennas: Dict[str, List[Position]], height: int, width: int) -> Set[Position]:
    def is_in_bounds(position: Position):
        return 0 <= position[0] < height and 0 <= position[1] < width

    antinodes = set()
    for frequency, positions in antennas.items():
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                dx = positions[i][0] - positions[j][0]
                dy = positions[i][1] - positions[j][1]
                new_positions = [(positions[i][0] + dx, positions[i][1] + dy),
                                 (positions[j][0] - dx, positions[j][1] - dy)]
                for new_position in new_positions:
                    if is_in_bounds(new_position):
                        antinodes.add(new_position)
    return antinodes


def find_antinodes_with_resonant_harmonics(antennas: Dict[str, List[Position]], height: int, width: int) -> Set[Position]:
    def is_in_bounds(position: Position):
        return 0 <= position[0] < height and 0 <= position[1] < width

    antinodes = set()
    for frequency, positions in antennas.items():
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                dx = positions[i][0] - positions[j][0]
                dy = positions[i][1] - positions[j][1]
                k = 0
                while is_in_bounds((positions[i][0] + k * dx, positions[i][1] + k * dy)):
                    antinodes.add((positions[i][0] + k * dx, positions[i][1] + k * dy))
                    k += 1
                k = 0
                while is_in_bounds((positions[j][0] - k * dx, positions[j][1] - k * dy)):
                    antinodes.add((positions[j][0] - k * dx, positions[j][1] - k * dy))
                    k += 1
    return antinodes


def part1() -> int:
    data = process_input()
    antennas = find_antennas(data)
    antinodes = find_antinodes(antennas, len(data), len(data[0]))
    return len(antinodes)


def part2() -> int:
    data = process_input()
    antennas = find_antennas(data)
    antinodes = find_antinodes_with_resonant_harmonics(antennas, len(data), len(data[0]))
    return len(antinodes)


if __name__ == '__main__':
    print("Part One answer: " + str(part1()))
    print("Part Two answer: " + str(part2()))
