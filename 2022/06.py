import queue
from helper import load_input

input = load_input("06", split=None)


class LifoQueue(queue.Queue):
    def __init__(self, maxsize=0):
        super().__init__(maxsize)
        self.total_items = 0

    def put(self, item):
        if len(self.queue) >= self.maxsize:
            self.queue.popleft()
        self.queue.append(item)
        self.total_items += 1

    @property
    def items_all_unique(self):
        return len(set(self.queue)) == self.maxsize


def find_marker(size: int) -> int | None:
    queue = LifoQueue(size)
    for c in input:
        queue.put(c)
        if queue.items_all_unique:
            return queue.total_items


def part_one():
    return find_marker(4)


def part_two():
    return find_marker(14)


print("Part one:", part_one())
print("Part two:", part_two())
