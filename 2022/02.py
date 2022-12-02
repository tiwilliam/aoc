from enum import Enum
from helper import load_input

input = load_input("02")


class Alternative(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3

    def __gt__(self, other):
        if self == other:
            return False
        if self == self.Rock:
            return other == self.Scissors
        if self == self.Paper:
            return other == self.Rock
        if self == self.Scissors:
            return other == self.Paper


class OpponentAlternatives(Enum):
    A = Alternative.Rock
    B = Alternative.Paper
    C = Alternative.Scissors


class MyAlternatives(Enum):
    X = Alternative.Rock
    Y = Alternative.Paper
    Z = Alternative.Scissors


class Outcome(Enum):
    Lose = 0
    Draw = 3
    Win = 6


class MyOutcome(Enum):
    X = Outcome.Lose
    Y = Outcome.Draw
    Z = Outcome.Win

    def best_choice(self, other: Alternative) -> Alternative:
        if self.value == Outcome.Lose:
            return lose_map[other]
        if self.value == Outcome.Draw:
            return other
        return win_map[other]


lose_map = {
    Alternative.Rock: Alternative.Scissors,
    Alternative.Paper: Alternative.Rock,
    Alternative.Scissors: Alternative.Paper,
}

win_map = dict(zip(lose_map.values(), lose_map.keys()))

rounds = input.split("\n")


def part_one():
    my_points = 0
    for round in rounds:
        op_alternative, my_alternative = round.split(" ")
        op_enum = OpponentAlternatives[op_alternative]
        my_enum = MyAlternatives[my_alternative]

        my_points += my_enum.value.value

        if op_enum.value == my_enum.value:
            my_points += 3
        elif op_enum.value < my_enum.value:
            my_points += 6

    print("My points part 1:", my_points)


def part_two():
    my_points = 0
    for round in rounds:
        op_alternative, my_outcome = round.split(" ")
        op_enum = OpponentAlternatives[op_alternative]
        my_enum = MyOutcome[my_outcome]

        my_points += my_enum.best_choice(op_enum.value).value
        my_points += my_enum.value.value

    print("My points part 2:", my_points)


part_one()
part_two()
