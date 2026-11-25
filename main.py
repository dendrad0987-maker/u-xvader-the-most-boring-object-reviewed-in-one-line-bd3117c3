"""Write a one-line review of the most boring everyday object.

The object is a rubber band from the junk drawer: it has held nothing
together for years, yet it snaps the very moment it is finally needed
to hold something together.
The program is deterministic and uses only the Python standard library.
"""

import os


LINE = (
    "The rubber band in the junk drawer has held nothing together "
    "since 2019, yet it will snap the very moment you finally need "
    "it to hold something together."
)


def main():
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
