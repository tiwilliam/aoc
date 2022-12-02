from helper import load_input

cals = []
input = load_input("01").split("\n\n")

for user in input:
    cals.append(sum(map(int, user.split("\n"))))

cals.sort()


def part_one():
    print("User with most cals:", cals[-1])


def part_two():
    print("Top 3 users with most cals:", sum(cals[-3:]))


part_one()
part_two()
