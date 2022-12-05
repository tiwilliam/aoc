import re
from helper import load_input

stacks, procedures = load_input("05", split="\n\n", strip=False)


class ProcedureReader:
    num_regexp = re.compile("[0-9]+")

    def __init__(self, procedure: str):
        self.procedures = procedure.split("\n")

    def read(self):
        for procedure in self.procedures:
            yield self.num_regexp.findall(procedure)


class CrateMover:
    def __init__(self):
        self.stacks: dict[int, list[str]] = {}

    @classmethod
    def load_stacks_from_string(cls, string: str) -> "CrateMover":
        instance = cls()
        for raw_string in string.split("\n")[:-1]:
            for stack in range(0, 1000):
                offset = 4 * stack
                if offset > len(raw_string):
                    break

                if stack not in instance.stacks:
                    instance.stacks[stack] = []

                value = raw_string[offset + 1 : offset + 2].strip()
                if not value:
                    continue

                instance.stacks[stack].append(value)
        return instance

    def move_with_crate_mover_9000(self, num: int, from_stack: int, to_stack: int):
        for _ in range(0, num):
            container = self.stacks[from_stack - 1].pop(0)
            self.stacks[to_stack - 1].insert(0, container)

    def move_with_crate_mover_9001(self, num: int, from_stack: int, to_stack: int):
        containers = self.stacks[from_stack - 1][0:num]
        for i, container in enumerate(containers):
            self.stacks[to_stack - 1].insert(i, container)
        del self.stacks[from_stack - 1][0:num]

    @property
    def top_containers(self) -> str:
        return "".join([v[0] for v in self.stacks.values()])


procedure_reader = ProcedureReader(procedures)


def part_one():
    crane = CrateMover.load_stacks_from_string(stacks)
    for num, from_stack, to_stack in procedure_reader.read():
        crane.move_with_crate_mover_9000(int(num), int(from_stack), int(to_stack))
    return crane.top_containers


def part_two():
    crane = CrateMover.load_stacks_from_string(stacks)
    for num, from_stack, to_stack in procedure_reader.read():
        crane.move_with_crate_mover_9001(int(num), int(from_stack), int(to_stack))
    return crane.top_containers


print("Part one:", part_one())
print("Part two:", part_two())
