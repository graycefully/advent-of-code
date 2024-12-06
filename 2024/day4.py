def read_input():
    with open('input.txt', 'r') as input:
        return [line.strip() for line in input.readlines()]


def part1(data):
    n, m = len(data), len(data[0])
    directions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (1, 1),
        (-1, 1),
        (1, -1),
        (-1, -1)
    ]

    def is_xmas(r, c, dr, dc):
        for i in range(4):
            ir, ic = r + i * dr, c + i * dc
            if not (0 <= ir < n and 0 <= ic < m and data[ir][ic] == "XMAS"[i]):
                return False
        return True

    count = 0
    for r in range(n):
        for c in range(m):
            for dr, dc in directions:
                if is_xmas(r, c, dr, dc):
                    count += 1
    return count


def part2(data):
    n, m = len(data), len(data[0])

    def is_mas(pattern):
        return pattern == ['M', 'A', 'S'] or pattern == ['S', 'A', 'M']

    count = 0
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            top_left_to_bottom_right = [data[i - 1][j - 1], data[i][j], data[i + 1][j + 1]]
            top_right_to_bottom_left = [data[i - 1][j + 1], data[i][j], data[i + 1][j - 1]]
            if is_mas(top_left_to_bottom_right) and is_mas(top_right_to_bottom_left):
                count += 1
    return count


data = read_input()
print("Part One answer: " + str(part1(data)))
print("Part Two answer: " + str(part2(data)))
