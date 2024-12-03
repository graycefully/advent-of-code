def read_input():
    with open('input.txt', 'r') as input:
        return [list(map(int, line.split())) for line in input.readlines()]


def is_safe(levels):
    increasing = all(levels[i] < levels[i + 1] and 1 <= levels[i + 1] - levels[i] <= 3 for i in range(len(levels) - 1))
    decreasing = all(levels[i] > levels[i + 1] and 1 <= levels[i] - levels[i + 1] <= 3 for i in range(len(levels) - 1))
    return increasing or decreasing


def part1(reports):
    count = 0
    for report in reports:
        if is_safe(report):
            count += 1
    return count


def part2(reports):
    count = 0
    for report in reports:
        for i in range(len(report)):
            report_with_one_removal = report[:i] + report[i+1:]
            if is_safe(report_with_one_removal):
                count += 1
                break
    return count


reports = read_input()
print("Part One answer: " + str(part1(reports)))
print("Part Two answer: " + str(part2(reports)))
