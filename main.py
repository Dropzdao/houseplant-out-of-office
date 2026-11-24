#!/usr/bin/env python3
"""The Houseplant Out-of-Office - make.fun program/v1 entry.

Writes one the funniest out-of-office auto-reply a houseplant would send, 120 characters or fewer. to /output/entry.txt.
"""

import os

LINE = "Out of office: last watered in March. I now run on sunlight, spite, and the hope someone reads this."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
