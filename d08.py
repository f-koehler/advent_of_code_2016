import re
import numpy

if __name__ == "__main__":
    regex_rect = re.compile("^rect\s+(\d+)x(\d+)$")
    regex_rotate_row = re.compile("^rotate\s+row\s+y=(\d+)\s+by\s+(\d+)$")
    regex_rotate_column = re.compile(
        "^rotate\s+column\s+x=(\d+)\s+by\s+(\d+)$")

    with open("input_08.txt") as fhandle:
        instructions = fhandle.read().splitlines()

    screen = numpy.full((6, 50), False, dtype=bool)

    for instruction in instructions:
        m = regex_rect.match(instruction)
        if m:
            w = int(m.group(1))
            h = int(m.group(2))
            screen[0, 0:w] = True
            screen[h - 1, 0:w] = True
            screen[1:h - 1, 0] = True
            screen[1:h - 1, w - 1] = True

        m = regex_rotate_row.match(instruction)
        if m:
            row = int(m.group(1))
            screen[row] = numpy.roll(screen[row], int(m.group(2)))
            continue

        m = regex_rotate_column.match(instruction)
        if m:
            col = int(m.group(1))
            screen[:, col] = numpy.roll(screen[:, col], int(m.group(2)))
            continue

    print(numpy.sum(screen))
    print()

    for y in range(6):
        for x in range(50):
            if screen[y, x]:
                print("█", end="")
            else:
                print(" ", end="")
        print()
