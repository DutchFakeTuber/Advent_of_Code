import numpy
from numba import njit

TEST: str = open("test.txt")
DATA: str = open("input.txt")

@njit
def partOne(data: list, days: int=1) -> int:
    for _ in numpy.arange(days, dtype=numpy.int64):
        zeros: int = 0
        for position in numpy.arange(len(data), dtype=numpy.int64):
            if data[position] == 0:
                zeros += 1
                data[position] = 6
            else:
                data[position] -= 1
        if zeros == 0: pass
        else: data = numpy.append(data, [8 for _ in range(zeros)])
    return len(data)

def partTwo(data: list, days: int=1) -> int:
    position: dict = {key: 0 for key in range(0, 9)}
    for number in data:
        position[number] += 1

    for _ in range(0, days):
        pos: list = [number for number in position.values()]
        for key in position.keys():
            if key < 6 or key == 7:
                position[key] = pos[key + 1]
            elif key == 6:
                position[key] = pos[key + 1] + pos[0]
            else:
                position[key] = pos[0]
    
    return sum([x for x in position.values()])

def main() -> None:
    partOne(numpy.array([1], dtype=numpy.int64), days=1) # Initialise Numba in this function
    print(partOne(numpy.array(DATA, dtype=numpy.int64), days=80)) # Calculation should be faster now
    
    print(partTwo(DATA, days=256)) # Using a different method than partOne

if __name__ == "__main__":
    main()