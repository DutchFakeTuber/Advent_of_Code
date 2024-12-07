from functools import reduce
from itertools import permutations
from math import floor, ceil

TEST: str = open("test.txt")
DATA: str = open("input.txt")

def getData(data: str) -> list:
    return [line.rstrip() for line in data.splitlines() if len(line) != 0]

def remove_brackets(lines: list) -> list[tuple]:
    """Take the puzzle input and return a list of tuples.
    Rather than have to deal with parsing brackets post-addition, instead record the number along with its depth.
    """
    final = []
    for line in lines:
        currLine, depth = [], 0
        for char in line:
            if char == '[':
                depth += 1
            elif char == "]":
                depth -= 1
            elif char.isdigit():
                currLine.append([int(char), depth])
        final.append(currLine)
    return final

def explode_reduction(number: list) -> tuple[bool, list]:
    """
    Figure out if snailfish number needs to explode. If it does, return it.
    We return both a boolean and the exploded snailfish number because we may need to do this a few times.
    """
    for index, ((n_one, d_one), (n_two, d_two)) in enumerate(zip(number, number[1:])):
        if d_one < 5 or d_one != d_two: # If the depth is not high enough or both numbers are at different levels
            continue
        if index > 0: # this is not the first number
            number[index - 1][0] += n_one
        if index < len(number) - 2:  # we're near the end of the number
            number[index + 2][0] += n_two
        return True, number[:index] + [[0, d_one - 1]] + number[index + 2:]
    return False, number

def split_reduction(number: list) -> tuple[bool, list]:
    """If snailfish number needs a split (has a number >= 10), do it and return the number."""
    # go through all your items (number, depth) and find any that are 10 or greater
    for index, (_number, depth) in enumerate(number):
        if _number < 10:  # go on the next tuple without doing anything
            continue
        down = floor(_number / 2.0)  # a departure from the solution I was following for clarity
        up = ceil(_number / 2.0)
        # now we need to add in a pair where we used to have a number
        return True, number[:index] + [[down, depth + 1], [up, depth + 1]] + number[index + 1:]
    return False, number

def add_numbers(one: list, two: list) -> list:
    """Add together 2 snailfish numbers"""
    _number = [[number, depth + 1] for number, depth in one + two]
    while True:
        reduction, _number = explode_reduction(_number)
        if reduction:
            # we just did an explosion, according to instructions we have to check for new explosions before reducing
            continue
        reduction, _number = split_reduction(_number)
        if not reduction:
            # if we didn't split, we're done with this step. Break out of the while loop
            break
    return _number

def magnitude(number: list) -> int:
    """Recursively calculate the magnitude."""
    if len(number) > 1:
        for index, ((number_one, depth_one), (number_two, depth_two)) in enumerate(zip(number, number[1:])):
            if depth_one != depth_two:
                continue  # we're not at the lowest level of recursion
            inner_magnitude = number_one * 3 + number_two * 2
            number = number[:index] + [[inner_magnitude, depth_one - 1]] + number[index + 2:]
            return magnitude(number)
    return number[0][0]

def partOne(data: str) -> int:
    simplified = remove_brackets(data)
    return magnitude(reduce(add_numbers, simplified))

def partTwo(data: str) -> int:
    simplified = remove_brackets(data)
    return max(magnitude(add_numbers(n_one, n_two)) for n_one, n_two in permutations(simplified, 2))

def main() -> None:
    data = getData(DATA)
    print(partOne(data))
    print(partTwo(data))

if __name__ == "__main__":
    main()