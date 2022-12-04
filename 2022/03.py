from helper import load_input

lines = load_input("03")


def score(letter: str):
    return ord(letter) - 96 if letter.islower() else ord(letter) - 38


def batch(lines: list[str], size: int = 3):
    for i in range(0, len(lines), size):
        yield lines[i : i + size]


def split_in_half(line: str):
    i = len(line) // 2
    return line[:i], line[i:]


def part_one(prio: int = 0):
    for line in lines:
        left, right = split_in_half(line)
        item_in_common = set(left).intersection(right).pop()
        prio += score(item_in_common)
    return prio


def part_two(prio: int = 0):
    for one, two, three in batch(lines):
        item_in_common = set(one).intersection(two, three).pop()
        prio += score(item_in_common)
    return prio


print("Sum of priorities, part 1:", part_one())
print("Sum of priorities, part 2:", part_two())
