from __future__ import annotations
from enum import Enum

from helper import load_input

lines = load_input("02")
rounds = [x.split(" ") for x in lines]


class Alternative(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3

    @property
    def lose_against(self):
        """
        Get the alternative that this alternative loses against.

        >>> Alternative.Rock.lose_against
        Alternative.Paper
        """
        return Alternative((self.value % 3) + 1)

    @property
    def wins_over(self):
        """
        Get the alternative that this alternative wins over.

        >>> Alternative.Rock.wins_over
        Alternative.Scissors
        """
        return Alternative((self.value - 2) % 3 + 1)

    def __gt__(self, other: Alternative):
        """
        Check if this alternative wins over the other alternative.
        """
        if self == other:
            return False
        return self.lose_against != other


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

    def best_choice(self, other: Alternative):
        """
        Get the alternative to achive outcome, given the other alternative.
        """
        if self.value == Outcome.Lose:
            return other.wins_over
        if self.value == Outcome.Draw:
            return other
        return other.lose_against


def part_one(points: int = 0):
    for op_alternative, my_alternative in rounds:
        op_enum = OpponentAlternatives[op_alternative]
        my_enum = MyAlternatives[my_alternative]

        points += my_enum.value.value
        if op_enum.value == my_enum.value:
            points += Outcome.Draw.value
        elif op_enum.value < my_enum.value:
            points += Outcome.Win.value

    return points


def part_two(points: int = 0):
    for op_alternative, my_outcome in rounds:
        op_enum = OpponentAlternatives[op_alternative]
        my_enum = MyOutcome[my_outcome]

        points += my_enum.best_choice(op_enum.value).value
        points += my_enum.value.value

    return points


print("Part one:", part_one())
print("Part two:", part_two())
