from helper import load_input

input = load_input("12", split="\n")


class NoGoodRouteError(Exception):
    ...


mem_map: dict[int, dict[int, str]] = {}
for y, row in enumerate(input):
    mem_map[y] = {}
    for x, column in enumerate(row):
        mem_map[y][x] = column


next_step_map: dict[str, list[str]] = {}
for c in "Sabcdefghijklmnopqrstuvwxyz":
    if c == "S":
        next_step_map[c] = ["a", "b"]
        continue
    next_step_map[c] = [chr(x) for x in range(97, ord(c) + 2)]
    if "z" in next_step_map[c]:
        next_step_map[c].append("E")


def find_cord(char: str):
    for y, row in mem_map.items():
        for x, column in row.items():
            if column != char:
                continue
            return (x, y)


def find_next_possible_steps(cord: tuple[int, int]):
    x, y = cord
    possible_steps = []
    next_values = next_step_map[mem_map[y][x]]

    if y != 0 and mem_map[y - 1][x] in next_values:
        possible_steps.append((x, y - 1))  # up
    if y != len(mem_map) - 1 and mem_map[y + 1][x] in next_values:
        possible_steps.append((x, y + 1))  # down
    if x != 0 and mem_map[y][x - 1] in next_values:
        possible_steps.append((x - 1, y))  # left
    if x != len(mem_map[y]) - 1 and mem_map[y][x + 1] in next_values:
        possible_steps.append((x + 1, y))  # right

    return possible_steps


def find_quickest_path(current_cord: tuple[int, int], steps=0):
    visited_cords = []
    valid_cords = [current_cord]
    end_cord = find_cord("E")

    while end_cord not in valid_cords:
        steps += 1
        if len(valid_cords) == 0:
            raise NoGoodRouteError("We did not find a way to the end")
        next_valid_cords = []
        for cord in valid_cords:
            next = find_next_possible_steps(cord)
            next = [n for n in next if n not in visited_cords]
            visited_cords.extend(next)
            next_valid_cords.extend(next)
        valid_cords = next_valid_cords

    return steps


def surrounded_by(x, y, char):
    return (
        mem_map[max(0, y - 1)][x] == char
        and mem_map[min(len(mem_map) - 1, y + 1)][x] == char
        and mem_map[y][max(0, x - 1)] == char
        and mem_map[y][min(len(mem_map[y]) - 1, x + 1)] == char
    )


def part_one():
    return find_quickest_path(find_cord("S"))


def part_two():
    steps = []
    for y, row in mem_map.items():
        for x, c in row.items():
            if c != "a" or surrounded_by(x, y, "a"):
                continue
            try:
                steps.append(find_quickest_path((x, y)))
            except NoGoodRouteError:
                continue
    return min(steps)


print("Part one:", part_one())
print("Part two:", part_two())
