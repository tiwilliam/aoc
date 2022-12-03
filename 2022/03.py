from helper import load_input

input = load_input("03")
lines = input.split("\n")


def score(letter: str) -> int:
    return ord(letter) - 96 if letter.islower() else ord(letter) - 38


def part_one(priorities=0):
    for line in lines:
        first, second = line[: len(line) // 2], line[len(line) // 2 :]
        shared = set(first).intersection(second).pop()
        priorities += score(shared)
    return priorities


def part_two(priorities=0, batch_size=3):
    for i in range(0, len(lines), batch_size):
        one, two, three = lines[i : i + batch_size]
        item_in_common = set(one).intersection(two, three).pop()
        priorities += score(item_in_common)
    return priorities


print("Sum of priorities, part 1:", part_one())
print("Sum of priorities, part 2:", part_two())
