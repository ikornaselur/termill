import datetime as dt
import json
import time
from typing import List

from termill import Termill

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
    t = Termill(initial_lines=8)

    with open("./demo.json", "r") as f:
        frames = json.load(f)

    for frame in frames:
        for row in now():
            t.write(row)

        t.writelines(frame.split("\n"))
        t.write("Art from https://www.incredibleart.org/links/ascii.html")
        t.flush()

        time.sleep(0.15)


if __name__ == "__main__":
    run()
