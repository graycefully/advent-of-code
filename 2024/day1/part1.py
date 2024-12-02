with open('input.txt', 'r') as input:
    data = [line.split() for line in input.readlines()]
    left = sorted([int(row[1]) for row in data])
    right = sorted([int(row[0]) for row in data])

    print(sum(abs(left - right) for left, right in zip(left, right)))
