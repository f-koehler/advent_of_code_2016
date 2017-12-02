import numpy


def count_invalid_triangles(a, b, c):
    return numpy.sum(
        numpy.logical_and(
            numpy.logical_and((a + b) > c, (a + c) > b), (b + c) > a))


if __name__ == "__main__":
    # part 1
    a, b, c = numpy.loadtxt("input_03.txt", unpack=True, dtype=int)
    print(count_invalid_triangles(a, b, c))

    # part 2
    d = numpy.concatenate((a, b, c))
    print(count_invalid_triangles(d[::3], d[1::3], d[2::3]))
