import numpy
from numba import njit

TEST: str = open("test.txt")
DATA: str = open("input.txt")

def partOne(data: list, minimum: int=None, maximum: int=None) -> int:
    if not minimum or not maximum:
        minimum: int = min(data) if not minimum else minimum
        maximum: int = max(data) if not maximum else maximum
    
    fuel_calc: dict = {}
    for endPoint in range(minimum, maximum + 1):
        fuel_calc[endPoint] = 0
        for startPoint in data:
            fuel_calc[endPoint] += abs(endPoint - startPoint)

    return min([position for position in fuel_calc.values()])

@njit
def partTwo(data: list, minimum: int=0, maximum: int=0) -> int:
    if not minimum or not maximum:
        minimum: int = min(data) if minimum == 0 else minimum
        maximum: int = max(data) if maximum == 0 else maximum
    
    fuel_calc: dict = {}
    for endPoint in numpy.arange(minimum, maximum + 1, dtype=numpy.int64):
        fuel_calc[endPoint] = 0
        for startPoint in data:
            difference: int = numpy.fabs(startPoint - endPoint)
            # Gauss Method: Sn = 1/2 * abs(begin-end) * (abs(begin-end) + 1)
            fuel_calc[endPoint] += int(0.5 * difference * (difference + 1))

    return min([position for position in fuel_calc.values()])

def main() -> None:
    print(partOne(DATA))
    
    partTwo(numpy.array([0], dtype=numpy.int64)) # partTwo Numba initialisation
    print(partTwo(numpy.array(DATA, dtype=numpy.int64)))

if __name__ == "__main__":
    main()