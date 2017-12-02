import re


def findall_overlapping(regex, string):
    results = []
    position = 0

    while True:
        result = regex.search(string, position)
        if result is None:
            break
        results.append(string[result.start():result.end()])
        position = result.start() + 1

    return results


if __name__ == "__main__":
    with open("input_07.txt") as fhandle:
        ipv7s = fhandle.read().splitlines()

    regex_hypernet_split = re.compile(r"\[|\]")
    regex_abba = re.compile(r"(?!(\w)\1\1\1)(\w)(\w)\3\2")
    regex_aba = re.compile(r"(?!(\w)\1)(\w)(\w)(\2)")

    ipv7s_parsed = []
    for ipv7 in ipv7s:
        split = regex_hypernet_split.split(ipv7)
        supernet = split[::2]
        hypernet = split[1::2]
        ipv7s_parsed.append((supernet, hypernet))

    # check for TLS support
    ipv7s_tls = []
    for ipv7 in ipv7s_parsed:
        found = False

        # check for a abba sequence in the non-hypernet part
        for supernet in ipv7[0]:
            if regex_abba.search(supernet):
                found = True
                break
        if not found:
            continue

        # check for a abba sequence in the hypernet part
        found = False
        for hypernet in ipv7[1]:
            if regex_abba.search(hypernet):
                found = True
                break
        if found:
            continue

        ipv7s_tls.append(ipv7)

    print(len(ipv7s_tls))

    # check for SSL support
    ipv7s_ssl = []
    for ipv7 in ipv7s_parsed:
        # find all aba sequences in the supernet part
        aba_matches = []
        for supernet in ipv7[0]:
            aba_matches += findall_overlapping(regex_aba, supernet)

        # look for a matching bab sequence in hypernet part
        found = False
        for hypernet in ipv7[1]:
            if found:
                break
            for aba in aba_matches:
                if (aba[1] + aba[0] + aba[1]) in hypernet:
                    ipv7s_ssl.append(ipv7)
                    found = True
                    break

    print(len(ipv7s_ssl))
