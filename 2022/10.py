from helper import load_input

input = load_input("10")

cycles = [20, 60, 100, 140, 180, 220]


class CRT:
    def __init__(self):
        self.display = ""

    def print(self, x):
        pos = len(self.display) % 40
        if pos >= x - 1 and pos <= x + 1:
            self.display += "#"
        else:
            self.display += "."

    def draw(self):
        for i in range(0, len(self.display), 40):
            print(self.display[i : i + 40])


class System:
    def __init__(self):
        self.x = 1
        self.cycle = 0
        self.signal_strength = 0
        self.crt = CRT()

    def tick(self):
        self.cycle += 1
        if self.cycle in cycles:
            self.signal_strength += self.x * self.cycle
        self.crt.print(self.x)

    def execute(self):
        for instruction in input:
            if instruction.startswith("addx"):
                value = int(instruction.split(" ")[1])
                self.tick()
                self.tick()
                self.x += value
            else:
                self.tick()

        return self.signal_strength


def part_one():
    system = System()
    return system.execute()


def part_two():
    system = System()
    system.execute()
    return system.crt.draw()


print("Part one:", part_one())
print("Part two:")
part_two()
