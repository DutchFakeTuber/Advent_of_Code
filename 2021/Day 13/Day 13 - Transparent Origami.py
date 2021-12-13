from Transparent_Origami import FOLDS, DATA
from Transparent_Origami import TEST_FOLDS, TEST_DATA

def getData(data: str, folds: str) -> tuple:
    coordinates: list = []
    for line in data.splitlines():
        if len(line) == 0: continue
        coords = line.split(',')
        coordinates.append([int(coords[1]), int(coords[0])])
    foldlines: dict = {
        number: ['X', int(fold.strip('fold along x='))] if str.__contains__(fold, 'fold along x=')
        else ['Y', int(fold.strip('fold along y='))]
        for number, fold in enumerate(folds.splitlines())
        if len(fold) != 0
    }
    return coordinates, foldlines

def origamiSetup(data: list) -> list:
    return [
        ['.' for _ in range(0, max([current[1] for current in data]) + 1)]
             for _ in range(0, max([current[0] for current in data]) + 1)
        ]
    
def foldOrigami(origami: list, fold_loc: int, fold_type: str) -> list:
    if fold_type == 'Y':
        newOrigami: list = [['.' for _ in range(len(origami[0]))] for _ in range(len(origami[0:fold_loc]))]
        for n_line, l_original, l_mirror in zip(range(len(origami[0:fold_loc])), origami[0:fold_loc], reversed(origami[fold_loc+1:len(origami)])):
            for n_col, c_original, c_mirror in zip(range(len(l_original)), l_original, l_mirror):
                if c_original == '#' or c_mirror == '#':
                    newOrigami[n_line][n_col] = '#'
    
    elif fold_type == 'X':
        newOrigami: list = [['.' for _ in range(len(origami[0][0:fold_loc]))] for _ in range(len(origami))]
        original_half: list = [origami[line][0:fold_loc] for line in range(len(origami))]
        mirrored_half: list = [[col for col in reversed(origami[line][fold_loc+1:len(origami[0])])] for line in range(len(origami))]

        for n_line, l_original, l_mirror in zip(range(len(newOrigami)), original_half, mirrored_half):
            for n_col, c_original, c_mirror in zip(range(len(l_original)), l_original, l_mirror):
                if c_original == '#' or c_mirror == '#':
                    newOrigami[n_line][n_col] = '#'

    return newOrigami

def partOne(data: list, fold_loc: int, fold_type: str) -> int:
    origami: list = origamiSetup(data)
    for line in data:
        origami[line[0]][line[1]] = '#'

    newOrigami = foldOrigami(origami, fold_loc, fold_type)
    total: int = 0
    for line in newOrigami:
        total += sum([1 if col == '#' else 0 for col in line])
    return total

def partTwo(data: list, folds: dict) -> int:
    origami: list = origamiSetup(data)
    for line in data:
        origami[line[0]][line[1]] = '#'
    
    fold_locs = [loc[1] for loc in folds.values()]
    fold_types = [loc[0] for loc in folds.values()]
    for fold_loc, fold_type in zip(fold_locs, fold_types):
        origami = foldOrigami(origami, fold_loc, fold_type)

    return origami

def main() -> None:
    data, folds = getData(DATA, FOLDS)
    print(partOne(data, folds[1][1], folds[1][0]))
    [print(''.join(' ' if col == '.' else '#' for col in line)) for line in partTwo(data, folds)]

if __name__ == "__main__":
    main()