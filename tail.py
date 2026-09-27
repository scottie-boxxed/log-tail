# language: Python 3, file: tail.py
import time
import sys
import argparse

RED = "\033[31m"
YELLOW = "\033[33m"
RESET = "\033[0m"


def colorize(line):
    low = line.lower()
    if "error" in low or "fatal" in low:
        return RED + line.rstrip() + RESET
    if "warn" in low:
        return YELLOW + line.rstrip() + RESET
    return line.rstrip()


def follow(path):
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        f.seek(0, 2)
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.3)
                continue
            print(colorize(line))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    args = parser.parse_args()
    try:
        follow(args.path)
    except KeyboardInterrupt:
        sys.exit(0)


if __name__ == "__main__":
    main()
