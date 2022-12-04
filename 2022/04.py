from helper import load_input

lines = load_input("04")


def expand_range(line: str):
    start, stop = line.split("-")
    return set(range(int(start), int(stop) + 1))


def get_ranges(line: str):
    left, right = line.split(",")
    return expand_range(left), expand_range(right)


def items_in_common(line: str):
    left_range, right_range = get_ranges(line)
    items_in_common = left_range.intersection(right_range)
    return len(items_in_common), left_range, right_range


def part_one(score: int = 0):
    for line in lines:
        num_in_common, left_range, right_range = items_in_common(line)
        if num_in_common == len(left_range) or num_in_common == len(right_range):
            score += 1
    return score


def part_two(score: int = 0):
    for line in lines:
        num_in_common, _, _ = items_in_common(line)
        if num_in_common:
            score += 1
    return score


print("Part one:", part_one())
print("Part two:", part_two())
