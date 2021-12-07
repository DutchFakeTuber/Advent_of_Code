import numpy
# from numba import jit
from Lanternfish import DATA

# @jit(nopython=True)
def parts(data: list, days: int=1) -> int:
    for _ in range(days):
        zeros: int = 0
        for position in range(len(data)):
            if data[position] == 0:
                zeros += 1
                data[position] = 6
            else:
                data[position] -= 1
        if zeros == 0: pass
        else: data = numpy.append(data, [8 for _ in range(zeros)])
    return len(data)

def main() -> None:
    # Only one loop is necessary to initialise Numba:
    print(parts(numpy.array([x for x in range(1000)])))

    # Initialisation is done, now for the real work:
    data: list = [numpy.array(DATA), numpy.array(DATA)]
    print(parts(data[0], days=numpy.int16(80)))
    print(parts(data[1], days=numpy.int16(256)))

if __name__ == "__main__":
    main()