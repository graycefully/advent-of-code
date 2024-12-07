from collections import deque, defaultdict


def process_input():
    with open('input.txt', 'r') as input:
        rules, updates = [section.split('\n') for section in input.read().split('\n\n')]
        rules = [tuple(map(int, rule.split('|'))) for rule in rules]
        updates = [list(map(int, update.split(','))) for update in updates]
        return rules, updates


def is_ordered(update, rules):
    pages = {page: idx for idx, page in enumerate(update)}
    return all(pages[x] < pages[y] for x, y in rules if x in pages and y in pages)


def find_middle(update):
    return update[len(update) // 2]


def topological_sort(rules, update):
    graph, indegree = defaultdict(list), defaultdict(int)
    for x, y in rules:
        if x in update and y in update:
            graph[x].append(y)
            indegree[y] += 1
            indegree.setdefault(x, 0)

    queue = deque([page for page, deg in indegree.items() if deg == 0])
    sorted_update = []
    while queue:
        page = queue.popleft()
        sorted_update.append(page)
        for neighbor in graph[page]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    return sorted_update


def part1(rules, updates):
    return sum(find_middle(update) for update in updates if is_ordered(update, rules))


def part2(rules, updates):
    unordered_updates = [update for update in updates if not is_ordered(update, rules)]
    sorted_updates = [topological_sort(rules, update) for update in unordered_updates]
    return sum(find_middle(sorted_update) for sorted_update in sorted_updates)


rules, updates = process_input()
print("Part One answer: " + str(part1(rules, updates)))
print("Part Two answer: " + str(part2(rules, updates)))
