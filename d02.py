if __name__ == "__main__":
    with open("input_02.txt") as fhandle:
        instructions = fhandle.readlines()

    def get_digit(pos):
        return digits[pos[0]][pos[1]]

    def apply_command(pos, command):
        if command == "L":
            candidate = (pos[0], pos[1] - 1)
        elif command == "R":
            candidate = (pos[0], pos[1] + 1)
        elif command == "U":
            candidate = (pos[0] - 1, pos[1])
        elif command == "D":
            candidate = (pos[0] + 1, pos[1])
        else:
            raise RuntimeError("Invalid input: \"{}\"".format(command))

        if get_digit(candidate) == 0:
            return pos
        return candidate

    def apply_command_series(pos, series):
        for command in series:
            pos = apply_command(pos, command)
        return pos

    # part 1
    digits = [[0, 0, 0, 0, 0], [0, "1", "2", "3", 0], [0, "4", "5", "6", 0],
              [0, "7", "8", "9", 0], [0, 0, 0, 0, 0]]
    position = (2, 2)
    password = ""
    for instruction in instructions:
        position = apply_command_series(position, instruction.strip())
        password += get_digit(position)
    print(password)

    # part 2
    digits = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, "1", 0, 0, 0],
              [0, 0, "2", "3", "4", 0, 0], [0, "5", "6", "7", "8", "9", 0],
              [0, 0, "A", "B", "C", 0, 0], [0, 0, 0, "D", 0, 0,
                                            0], [0, 0, 0, 0, 0, 0, 0]]
    position = (3, 1)
    password = ""
    for instruction in instructions:
        position = apply_command_series(position, instruction.strip())
        password += get_digit(position)
    print(password)
