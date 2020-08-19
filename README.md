# Termill

A command line utility library to print out multiple lines of text and replace
them. It's simple to print out a single line and replace it by using a carriage
return:

```python
print("foo", end="\r")
print("bar")
```

but that doesn't work with multiple lines. But by utilising backspace
characters and the width of the terminal, you can actually replace multiple
lines.

This library is just to handle that, so that you can print out lines, flush
them, then print out new lines ontop of the old ones. A simple demo is included
(`demo.py`) that just prints out the current time for 5 seconds.

This was just thrown together as a proof of concept, so it's likely very buggy.
This has also only been tested on my MacOS machine, with ZSH. I have no idea if
this works anywhere else.

## Why not curses?
I wanted to be able to monitor certain things and print out regular updates to
the termina. As far as I could tell (based on very very limited research) I
could do that with curses, but it would have to take over the whole terminal.

I want to be able to print out few lines and update them, without having to
take over the terminal, the idea being that I can see the history in my
terminal right before running whatever is printing out updates.

## Usage

```python
import time

from termill import termill

with termill() as t:
    t.write("line one")
    t.write("line two")
    t.write("line three")
    t.flush()
    time.sleep(1)
    t.write_lines(["line one has changed", "there will be no line three"])
    t.flush()
```

## Demo

![demo.gif](https://raw.githubusercontent.com/ikornaselur/termill/master/.github/demo.gif)
