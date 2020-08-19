import time
import datetime as dt
from typing import List

from termill import termill

representations = {
    "0": ("###", "# #", "# #", "# #", "###"),
    "1": ("  #", "  #", "  #", "  #", "  #"),
    "2": ("###", "  #", "###", "#  ", "###"),
    "3": ("###", "  #", "###", "  #", "###"),
    "4": ("# #", "# #", "###", "  #", "  #"),
    "5": ("###", "#  ", "###", "  #", "###"),
    "6": ("###", "#  ", "###", "# #", "###"),
    "7": ("###", "  #", "  #", "  #", "  #"),
    "8": ("###", "# #", "###", "# #", "###"),
    "9": ("###", "# #", "###", "  #", "###"),
    ":": ("   ", " # ", "   ", " # ", "   "),
}


def now() -> List[str]:
    timestamp = dt.datetime.now().strftime("%H:%M:%S")
    return [" ".join(row) for row in zip(*[representations[d] for d in timestamp])]


def run() -> None:
    seconds = 5
    with termill(initial_lines=8) as t:
        while seconds:
            for row in now():
                t.write(row)

            t.write(f"Demo will run for {seconds} more seconds...")

            if seconds == 4:
                t.write("Additional line")
            elif seconds == 3:
                t.write("Additional line")
                t.write("And a second one")
            elif seconds == 2:
                t.write("Back to just one")

            t.flush()
            time.sleep(1)
            seconds -= 1


if __name__ == "__main__":
    run()
