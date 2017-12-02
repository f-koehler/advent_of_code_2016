if __name__ == "__main__":
    with open("input_06.txt") as fhandle:
        lines = fhandle.read().splitlines()

    message1 = ""
    message2 = ""
    for i in range(len(lines[0])):
        appearances = {}
        for line in lines:
            appearances[line[i]] = appearances.get(line[i], 0) + 1
        appearances = sorted(
            [(value, key) for key, value in appearances.items()])
        message1 += appearances[-1][1]
        message2 += appearances[0][1]

    print(message1)
    print(message2)
