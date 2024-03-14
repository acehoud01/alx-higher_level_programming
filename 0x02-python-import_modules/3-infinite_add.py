#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    i = len(sys.argv)
    total = 0
    for y in range(1, i):
        total += int(sys.argv[y])
    print(total)
