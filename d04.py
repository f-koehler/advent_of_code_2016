import re


def checksum(parsed_room):
    appearances = {}
    for char in parsed_room[0]:
        appearances[char] = appearances.get(char, 0) + 1
    appearances = list(
        sorted(
            [(char, appearances[char]) for char in appearances],
            key=lambda x: (-x[1], x[0])))[:5]
    return "".join([appearance[0] for appearance in appearances])


alphabet = [chr(i) for i in range(97, 123)]


def rotate_alphabet(shift):
    shift = shift % len(alphabet)
    return alphabet[shift:] + alphabet[:shift]


def decrypt_name(parsed_room):
    rotated_alphabet = rotate_alphabet(parsed_room[1])
    decrypted_name = ""
    for char in parsed_room[0]:
        decrypted_name += rotated_alphabet[alphabet.index(char)]
    return decrypted_name


if __name__ == "__main__":
    regex = re.compile(r"^((?:[a-z]+-)+)(\d+)\[([a-z]+)\]$")

    with open("input_04.txt") as fhandle:
        rooms = fhandle.read().splitlines()

    rooms = [(match.group(1).replace("-", ""), int(match.group(2)),
              match.group(3))
             for match in [regex.match(room) for room in rooms]
             if match is not None]

    total = 0
    valid_rooms = []
    for room in rooms:
        if checksum(room) == room[2]:
            total += room[1]
            valid_rooms.append(room)
    print(total)

    for room in valid_rooms:
        if decrypt_name(room) == "northpoleobjectstorage":
            print(room[1])
            break
