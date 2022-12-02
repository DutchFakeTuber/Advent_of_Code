import pandas
import numpy
from Probably_a_Fire_Hazard import INPUT

def getData() -> list:
    data: list[list] = [
        [l for l in line.split(' ') if l not in ['turn', 'through']] 
        for line in INPUT.splitlines() if len(line) != 0
    ]
    return [
        [command, list(map(int, start.split(','))), list(map(int, end.split(',')))]
        for command, start, end in data
    ]

def partOne() -> int:
    array: list[list] = numpy.array([[False for _ in range(1000)] for _ in range(1000)])
    for command, start, end in getData():
        if command == 'on':
            array[start[0]:end[0]+1,start[1]:end[1]+1] = True
        elif command == 'off':
            array[start[0]:end[0]+1,start[1]:end[1]+1] = False
        else:
            array[start[0]:end[0]+1,start[1]:end[1]+1] = ~array[start[0]:end[0]+1,start[1]:end[1]+1]
    return numpy.count_nonzero(array)

def partTwo() -> int:
    array: list[list] = numpy.array([[0 for _ in range(1000)] for _ in range(1000)], dtype=numpy.int64)
    for command, start, end in getData():
        for x in range(start[0], end[0] + 1):
            for y in range(start[1], end[1] + 1):
                if command == 'on':
                    array[x,y] += 1
                elif command == 'off':
                    array[x,y] -= 1 if array[x,y] != 0 else 0
                else:
                    array[x,y] += 2
    return sum([sum(col) for col in array])
    
def main() -> None:
    print(partOne())
    print(partTwo())

if __name__ == "__main__":
    main()
