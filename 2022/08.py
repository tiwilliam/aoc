from __future__ import annotations
import itertools
from helper import load_input

input = load_input("08")

GRID_X = 99
GRID_Y = 99


def grid_iterator():
    return itertools.product(range(GRID_X), range(GRID_Y))


def has_clear_view(distance, direction, height, x, y):
    visible = True
    for i in range(1, distance):
        match direction:
            case "east":
                h = input[y][x + i]
            case "west":
                h = input[y][x - i]
            case "south":
                h = input[y + i][x]
            case _:
                h = input[y - i][x]

        if h >= height:
            visible = False
            break

    return visible


def part_one(score=0):
    for x, y in grid_iterator():
        height = input[y][x]

        if has_clear_view(GRID_X - x, "east", height, x, y):
            score += 1
            continue

        if has_clear_view(x + 1, "west", height, x, y):
            score += 1
            continue

        if has_clear_view(y + 1, "north", height, x, y):
            score += 1
            continue

        if has_clear_view(GRID_Y - y, "south", height, x, y):
            score += 1
            continue

    return score


def viewing_distance(distance, direction, height, x, y):
    score = 0
    for i in range(1, distance):
        match direction:
            case "east":
                h = input[y][x + i]
            case "west":
                h = input[y][x - i]
            case "south":
                h = input[y + i][x]
            case _:
                h = input[y - i][x]

        if h < height:
            score += 1
        elif h == height:
            score += 1
            break

    return score


def part_two(highest=0):
    for x, y in grid_iterator():
        height = input[y][x]
        e = viewing_distance(GRID_X - x, "east", height, x, y)
        w = viewing_distance(x + 1, "west", height, x, y)
        n = viewing_distance(y + 1, "north", height, x, y)
        s = viewing_distance(GRID_Y - y, "south", height, x, y)
        score = e * w * n * s
        if score > highest:
            highest = score

    return highest


print("Part one:", part_one())
print("Part two:", part_two())
