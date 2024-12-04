import re


def read_input():
    with open('input.txt', 'r') as input:
        return input.read()


def part1(data):
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    matches = re.findall(pattern, data)
    return sum(int(x) * int(y) for x, y in matches)


def part2(data):
    enabled, result, i, n = True, 0, 0, len(data)
    while i < n:
        mul_match = re.match(r'mul\((\d{1,3}),(\d{1,3})\)', data[i:])
        if mul_match:
            if enabled:
                x, y = map(int, mul_match.groups())
                result += x * y
            i += len(mul_match.group(0))
            continue

        do_match = re.match(r'do\(\)', data[i:])
        if do_match:
            enabled = True
            i += len(do_match.group(0))
            continue

        dont_match = re.match(r'don\'t\(\)', data[i:])
        if dont_match:
            enabled = False
            i += len(dont_match.group(0))
            continue
        i += 1
    return result


data = read_input()
print("Part One answer: " + str(part1(data)))
print("Part Two answer: " + str(part2(data)))
