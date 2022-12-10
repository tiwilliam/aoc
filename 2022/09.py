from helper import load_input

input = load_input("09")


class RopeBridge:
    def __init__(self, tails: int):
        self.head = (0, 0)
        self.tails = [(0, 0)] * tails
        self.visited = {(0, 0)}

    def adjacent_coords(self, tail: tuple[int, int]):
        return {(tail[0] - 1 + x, tail[1] - 1 + y) for x in range(3) for y in range(3)}

    def take_a_step(self, head_x: int, head_y: int):
        self.head = (head_x, head_y)
        for i, t in enumerate(self.tails):
            h = self.head if i == 0 else self.tails[i - 1]

            if h in self.adjacent_coords(t):
                return

            if h[0] == t[0]:
                if h[1] > t[1]:
                    # move tail up
                    t = (t[0], t[1] + 1)
                else:
                    # move tail down
                    t = (t[0], t[1] - 1)
            elif h[1] == t[1]:
                if h[0] > t[0]:
                    # move tail right
                    t = (t[0] + 1, t[1])
                else:
                    # move tail left
                    t = (t[0] - 1, t[1])
            elif h[1] > t[1]:
                if h[0] > t[0]:
                    # move tail up right
                    t = (t[0] + 1, t[1] + 1)
                else:
                    # move tail up left
                    t = (t[0] - 1, t[1] + 1)
            else:
                if h[0] > t[0]:
                    # move tail down right
                    t = (t[0] + 1, t[1] - 1)
                else:
                    # move tail down left
                    t = (t[0] - 1, t[1] - 1)

            self.tails[i] = t
            if i == len(self.tails) - 1:
                self.visited.add(t)

            assert h in self.adjacent_coords(t), (h, t)

    def calculate(self, input):
        for instruction in input:
            direction, count = instruction.split(" ")
            iterator = range(int(count))

            if direction == "U":
                for _ in iterator:
                    self.take_a_step(self.head[0], self.head[1] + 1)
            elif direction == "D":
                for _ in iterator:
                    self.take_a_step(self.head[0], self.head[1] - 1)
            elif direction == "L":
                for _ in iterator:
                    self.take_a_step(self.head[0] - 1, self.head[1])
            elif direction == "R":
                for _ in iterator:
                    self.take_a_step(self.head[0] + 1, self.head[1])

        return self.visited


def part_one():
    bridge = RopeBridge(tails=1)
    return len(bridge.calculate(input))


def part_two():
    bridge = RopeBridge(tails=9)
    return len(bridge.calculate(input))


print("Part one:", part_one())
print("Part two:", part_two())
