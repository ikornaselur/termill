import shutil
import sys
from contextlib import contextmanager
from typing import Iterator, List


class Printer:
    width: int
    height: int
    _lines: List[str]
    _max_lines_flushed: int

    def __init__(self) -> None:
        if not sys.stdout.isatty():
            raise Exception("Not atty")

        size = shutil.get_terminal_size()
        self.width = size.columns
        self.height = size.lines

        self._lines = []
        self._max_lines_flushed = 0

    def print(self, line: str) -> None:  # noqa: A003
        self._lines.append(line)

    def flush(self) -> None:
        while len(self._lines) < self._max_lines_flushed:
            self._lines.append("")
        else:
            self._max_lines_flushed = len(self._lines)

        output = ""
        for line in self._lines:
            if len(line) > self.width:
                raise Exception("Overflow!")
            output += line.ljust(self.width)

        self._lines = []

        print("\b" * self.width * self._max_lines_flushed, end="")
        print(output, end="\r")


@contextmanager
def termill() -> Iterator[Printer]:
    yield Printer()
    print()
