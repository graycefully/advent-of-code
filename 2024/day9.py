from typing import List, Tuple, Union

type Disk = List[Union[str, int]]


def process_input() -> Tuple[List[int], List[int]]:
    with (open('input.txt', 'r') as file):
        disk_map = file.read()
        return [int(disk_map[i]) for i in range(0, len(disk_map), 2)], \
            [int(disk_map[i]) for i in range(1, len(disk_map), 2)]


def create_disk(files: List[int], free_space: List[int]) -> Disk:
    disk = []
    i = 0
    while i < len(files):
        disk.extend([i] * files[i])
        if i < len(free_space):
            disk.extend(['.'] * free_space[i])
        i += 1
    return disk


def compact_disk_by_file_blocks(disk: Disk) -> Disk:
    l, r = 0, len(disk) - 1
    while l < r:
        while l < r and disk[l] != '.':
            l += 1
        while l < r and disk[r] == '.':
            r -= 1
        disk[l], disk[r] = disk[r], disk[l]
        l += 1
        r -= 1
    return disk


def compact_disk_by_whole_files(disk: Disk) -> Disk:
    def disk_to_disk_sizes(disk: Disk) -> List[List[int]]:
        disk_sizes = []
        i = 0
        while i < len(disk):
            current = disk[i]
            count = 1
            while i + 1 < len(disk) and disk[i + 1] == current:
                i += 1
                count += 1
            disk_sizes.append([current, count])
            i += 1
        return disk_sizes

    disk_sizes = disk_to_disk_sizes(disk)

    l, r, ls, rs = 0, len(disk) - 1, 0, len(disk_sizes) - 1
    for disk_size in disk_sizes[::-1]:
        if disk_size[0] != '.':
            r_id = disk_size[0]
            break

    while r_id > 0:
        rs = next(i for i, disk_size in enumerate(disk_sizes) if disk_size[0] == r_id)
        i = len(disk_sizes) - 1
        while i > rs:
            r -= disk_sizes[i][1]
            i -= 1
        while ls < rs and (disk_sizes[ls][0] != '.' or disk_sizes[ls][1] < disk_sizes[rs][1]):
            l += disk_sizes[ls][1]
            ls += 1
        for _ in range(disk_sizes[rs][1]):
            disk[l], disk[r] = disk[r], disk[l]
            l += 1
            r -= 1
        disk_sizes = disk_to_disk_sizes(disk)
        l = 0
        ls = 0
        r = len(disk) - 1
        r_id -= 1
    return disk


def calculate_checksum(disk: Disk) -> int:
    checksum = 0
    for i in range(len(disk)):
        if disk[i] != '.':
            checksum += i * disk[i]
    return checksum


def part1() -> int:
    files, free_space = process_input()
    return calculate_checksum(compact_disk_by_file_blocks(create_disk(files, free_space)))


def part2() -> int:
    files, free_space = process_input()
    return calculate_checksum(compact_disk_by_whole_files(create_disk(files, free_space)))


if __name__ == '__main__':
    print("Part One answer: " + str(part1()))
    print("Part Two answer: " + str(part2()))
