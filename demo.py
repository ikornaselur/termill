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
    with termill() as t:
        while seconds:
            for row in now():
                t.print(row)

            t.print(f"Demo will run for {seconds} more seconds...")

            if seconds == 2:
                t.print("NEW LINE!!")

            t.flush()
            time.sleep(1)
            seconds -= 1


if __name__ == "__main__":
    run()
