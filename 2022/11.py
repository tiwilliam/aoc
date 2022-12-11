import re
import math
from functools import cache
from helper import load_input

input = load_input("11", split="\n\n")

number_regex = re.compile(r"(\d+)")


def extract_numbers(input: str) -> list[int]:
    return list(map(int, number_regex.findall(input)))


class Operation:
    def __init__(self, operation: str):
        self.operation = operation
        self.tokens = self.operation.split(" ")

    def calculate(self, old: int) -> int:
        if "*" in self.tokens:
            if self.tokens.count("old") == 1:
                return old * int(self.tokens[-1])
            return old * old
        return old + int(self.tokens[-1])


class Monkey:
    def __init__(self, note: str):
        note_lines = note.split("\n")

        self.inspections = 0
        self.items = extract_numbers(note_lines[1])
        self.operation = Operation(note_lines[2])

        test_data = extract_numbers(note_lines[3] + note_lines[4] + note_lines[5])
        self.test_division = test_data[0]
        self.test_success_target = test_data[1]
        self.test_failure_target = test_data[2]

    def inspect(self, worried: bool, lcm: int):
        for item in self.items:
            new = self.operation.calculate(item)
            yield (new if worried else new // 3) % lcm
            self.inspections += 1

    def find_target(self, item):
        if item % self.test_division == 0:
            return self.test_success_target
        return self.test_failure_target


class ChaseManager:
    def __init__(self, notes: str):
        self.monkeys: list[Monkey] = []
        for note in notes:
            self.monkeys.append(Monkey(note))

    def start_round(self, worried: bool = False):
        for monkey in self.monkeys:
            items = monkey.inspect(worried, self.division_lcm)
            for item in items:
                target = monkey.find_target(item)
                self.monkeys[target].items.append(item)
            monkey.items.clear()

    @property
    @cache
    def division_lcm(self):
        return math.lcm(*[monkey.test_division for monkey in self.monkeys])

    @property
    def monkey_business(self):
        inspections = [monkey.inspections for monkey in self.monkeys]
        inspections.sort(reverse=True)
        return inspections[0] * inspections[1]


def part_one():
    manager = ChaseManager(input)
    for _ in range(20):
        manager.start_round()
    return manager.monkey_business


def part_two():
    manager = ChaseManager(input)
    for _ in range(10_000):
        manager.start_round(worried=True)
    return manager.monkey_business


print("Part one:", part_one())
print("Part two:", part_two())
