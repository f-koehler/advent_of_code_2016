from collections import deque


def convert_instruction(instruction):
    if instruction[0] == "L":
        return (1j, int(instruction[1:]))
    else:
        return (-1j, int(instruction[1:]))


def taxicab_distance(position):
    return int(abs(position.real) + abs(position.imag))


if __name__ == "__main__":

    with open("input_01.txt") as fhandle:
        instructions = [
            convert_instruction(instruction.strip())
            for instruction in fhandle.read().split(",")
        ]

    direction = 1j
    position = 0j
    visited = deque([position])
    distance2 = None

    for instruction in instructions:
        direction *= instruction[0]
        for _ in range(instruction[1]):
            position += direction

            if distance2 is None:
                if position in visited:
                    distance2 = taxicab_distance(position)
                    visited = None
                else:
                    visited.append(position)

    if distance2 is None:
        distance2 = taxicab_distance(position)

    print(taxicab_distance(position))
    print(distance2)
