from typing import Self
from enum import Enum
from helper import load_input

input = load_input("02")
rounds = [x.split(" ") for x in input.split("\n")]


class Alternative(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3

    @property
    def losing_response(self) -> Self:
        if self == self.Rock:
            return self.Paper
        if self == self.Paper:
            return self.Scissors
        if self == self.Scissors:
            return self.Rock

    @property
    def winning_response(self) -> Self:
        return (set(Alternative) - {self, self.losing_response}).pop()

    def __gt__(self, other):
        if self == other:
            return False
        return self.losing_response != other


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
            return other.winning_response
        if self.value == Outcome.Draw:
            return other
        return other.losing_response


def part_one(points=0):
    for op_alternative, my_alternative in rounds:
        op_enum = OpponentAlternatives[op_alternative]
        my_enum = MyAlternatives[my_alternative]

        points += my_enum.value.value
        if op_enum.value == my_enum.value:
            points += Outcome.Draw.value
        elif op_enum.value < my_enum.value:
            points += Outcome.Win.value

    return points


def part_two(points=0):
    for op_alternative, my_outcome in rounds:
        op_enum = OpponentAlternatives[op_alternative]
        my_enum = MyOutcome[my_outcome]

        points += my_enum.best_choice(op_enum.value).value
        points += my_enum.value.value

    return points


print("My points part 1:", part_one())
print("My points part 2:", part_two())
