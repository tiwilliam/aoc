from __future__ import annotations
from typing import Generator
from helper import load_input

input = load_input("07")


class Directory:
    def __init__(self, name, parent: Directory | None = None):
        self.name = name
        self.files: list[tuple[str, int]] = []
        self.subdirs: list[Directory] = []
        self.parent: Directory | None = parent

    def add_file(self, size, name):
        self.files.append((name, size))

    def add_subdir(self, name):
        subdir = Directory(name, parent=self)
        self.subdirs.append(subdir)
        return subdir

    def size(self):
        return sum(int(size) for _, size in self.files)

    def subdirs_size(self):
        return sum(subdir.total_size() for subdir in self.subdirs)

    def total_size(self):
        return self.size() + self.subdirs_size()

    def iter(self, max_size=None) -> Generator[Directory, None, None]:
        for subdir in self.subdirs:
            if not max_size or subdir.total_size() <= max_size:
                yield subdir
            yield from subdir.iter(max_size)


class Shell:
    def __init__(self, output):
        self.output = output
        self.cursor = 0
        self.root = None

    def replay_history(self):
        while self.cursor < len(self.output):
            line = self.output[self.cursor]
            self.cursor += 1
            self.run(line[2:])

    def ls(self, _):
        while self.cursor < len(self.output):
            line = self.output[self.cursor]
            if line.startswith("$"):
                break
            self.cursor += 1
            if line.startswith("dir "):
                continue
            self.cwd.add_file(*line.split(" "))

    def cd(self, args):
        new_dir = args[0]

        if new_dir == "..":
            self.cwd = self.cwd.parent
            return

        if not self.root:
            self.root = Directory(new_dir, None)
            self.cwd = self.root
            return

        self.cwd = self.cwd.add_subdir(new_dir)

    def run(self, command):
        bin, *args = command.split(" ")
        getattr(self, bin)(args)


shell = Shell(input)
shell.replay_history()


def part_one(total=0):
    for dir in shell.root.iter(max_size=100_000):
        total += dir.total_size()
    return total


def part_two():
    disk_size = 70_000_000
    disk_needed = 30_000_000
    total_size = shell.root.total_size()
    free_size = disk_size - total_size

    sizes = [dir.total_size() for dir in shell.root.iter()]
    return min(filter(lambda x: x >= disk_needed - free_size, sizes))


print("Part one:", part_one())
print("Part two:", part_two())
