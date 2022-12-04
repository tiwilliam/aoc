from helper import load_input

input = load_input("01", split="\n\n")

sorted_cals = [sum(map(int, user.split("\n"))) for user in input]
sorted_cals.sort()


def part_one():
    return sorted_cals[-1]


def part_two():
    return sum(sorted_cals[-3:])


print("Part one:", part_one())
print("Part two:", part_two())
