import shutil
import sys
from typing import List


class Termill:
    width: int
    height: int
    _lines: List[str]
    _max_lines_flushed: int

    def __init__(self, initial_lines: int = 0) -> None:
        if not sys.stdout.isatty():
            raise Exception("Not atty")

        size = shutil.get_terminal_size()
        self.width = size.columns
        self.height = size.lines

        self._lines = []
        self._max_lines_flushed = initial_lines

    def write(self, line: str) -> None:
        """ Add a single line to the internal lines buffer """
        self._lines.append(line)

    def writelines(self, lines: List[str]) -> None:
        """ Add multiple lines to the internal lines buffer """
        self._lines.extend(lines)

    def printlines(self, lines: List[str]) -> None:
        """ A shorthand to write multiple lines and flush immediately """
        self.writelines(lines)
        self.flush()

    def flush(self) -> None:
        """ Flush out the current internal lines buffer """
        missing_lines = max(0, self._max_lines_flushed - len(self._lines))
        if missing_lines:
            self._lines.extend([""] * missing_lines)
        self._max_lines_flushed = len(self._lines)

        output = ""
        for line in self._lines:
            if len(line) > self.width:
                raise Exception("Overflow!")
            output += line.ljust(self.width)

        self._lines = []

        sys.stdout.write("\b" * self.width * self._max_lines_flushed)
        sys.stdout.write(output)
        sys.stdout.flush()
