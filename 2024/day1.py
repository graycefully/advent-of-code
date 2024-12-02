def read_input():
    with open('input.txt', 'r') as input:
        data = [line.split() for line in input.readlines()]
        return sorted([int(row[1]) for row in data]), sorted([int(row[0]) for row in data])


def part1(left, right):
    return sum(abs(left - right) for left, right in zip(left, right))


def part2(left, right):
    similarity = 0
    for num in left:
        similarity += num * right.count(num)
    return similarity


left, right = read_input()
print("Part One answer: " + str(part1(left, right)))
print("Part Two answer: " + str(part2(left, right)))
