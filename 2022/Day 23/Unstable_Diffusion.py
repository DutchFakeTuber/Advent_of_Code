INPUT: str = """
##...##......#.#.#..#####.##.#..#.#..#.###....##..#...#####...##.##..#
.#..##...##.....###.#.###..###.##.##.........###..#..#.#..##.#.#.#....
.###.#..#.#..##.##.#...##..#.#...###.#..##.#..#...#..####.##..##..#...
#..#..#.#....#.####......##.#.#.##..#.##.#.###..##.#...#..#..#.#..###.
.#.#....###.....###..##.###.#.###....##..#...#.####.#....#.#.###..##..
.##.#####...###..#...##...........#...##.#.###.#.....#...#...###.#....
.#.###.#..#.##.#...#....####...##..##.####..###.##......#..##..##...##
####..###.#..##...#..##.....###...######...##.....#..##..###.#.##.####
.#.##.###.#..#.#....######.#.####.##....#.#.#.#.###.###....#.######.#.
#####.#..####..######..##...#.####..####.....##..#.#.#.....##...#.###.
#..###.......##...#.###..#.##.####.....#...##.....#....#.#.##.#.##..#.
##..##.###.##.#....##.#.#..####..#.##.##..#.##....##.#.#..##.###...##.
.######..#..#..#####.###..####...#.#..#.##..####....#.###..#..#####...
#.#.###....##....##.#...#...###.##.##.##.##.#.#####.#####.......##.##.
....#.#.#.###.#...###.##.#..##.##..##.#.#....##.#.#.#####.#..##..###.#
.######...##..#..#...#..#.###.##.....#..##..#.##....#..####.##...##...
..#.#..#.###.#.#.##.#....##.###...#.#...##.#......#.######..##.#.#.#..
#...##..#..####.#.#...#.#.#...#....##..##..#.#..##.#..#.###....#.#...#
#..###...#.#.#.####.##..#.#..###.#..#...#..##..##.#....###.#...#.#..#.
.##....####.#.##.###.###..####..####.#.....##.#.#.####..##.##....####.
#.###.#...###....####......#...#..##...#.#.#..#.##.#.#.##..#....#...#.
##.#.#.####.##...###...#####......##..##.##.#..##..##...###..##.#.#.##
#.....#.##..#..##..#...###.###...#...#.#.##.....#..#.#.#.##.#..#.....#
#..#..###.#####..##.###.####...#.#####..##.....#.#.......#.#.#...###..
#.#.##.....###....#..#.###..###..#.#####..######..####.####...##..###.
#......#...#......#...##.#.##############.##......#..##.#.#.####.#.###
.####.#....#.###..##.#.##..######..#..#.###..#.......##.####.....#.#..
#..##..##.##..#..#..##...##.....##..#...##..#.###.#..###.##..#..#...##
###.##..#.#.####.####...#.#..#..##...###.....#...###..#..#...##..#.#..
#.##.#.###.....###.####.#.##.##.###.##..##.#..#.###...#....###.##..##.
##..###.#.##.##...##.##....#...#...#....###..#...#.#...#..##.#.#..#..#
##.#.###.#.#.######.#####.#..........##..#...##.#..#..#..##.##.#.#..##
.#..#####.##.##.#.#...#.##.....#..##.##..#.#..####.###..####.#..##..##
##.##.##.###.#..#.#..######.#.#.....#.#.#.#.#...#.##..#.#.###..#.#..#.
##...##.#...##.#..###..#..##......##...#............###.##.#.#.#.#.###
#..#..####..###.#.###.#.##..#####.##.####...##.##..#..##.#.###.#...###
.##.#.#.#...#..##..#...##...###.#...#.##.##..........##.##.###.#......
##..###.####.#....##.....#..##.#...#.##..#.#.#.##.#..#.#...#...##.##.#
#.#..#..#...##..#..###..#..#..#.#..#.#####.##..#...#..#..#..##.#.#.#..
.##..##..#..#.##.#..#.###..#.#...#######.#....#...####..##.#.##.#.#.##
.#####.....#....#.###...#########....#....#.##.#.##..####...#.##.#....
####..#..#.#....###.#...#.#.#####....#..#.###.#.#.#.##.########.##.#..
...#.######.#..##.##.#..##...###.#.#.#.#.#.#..#..###.####.##.##.#.##..
.#.#.##....###.#.#######.###...#.##.##.##.#..#######.#....##.....##..#
.#...##.#..#.##...#.####...#..#.##.#.##.#....##..##.###..##.##..#...#.
.###....#################..#.#.#..##.#.#..#.#.##..#.#.##.##.#....#..##
..#...#.#.###.#.#.#.####.#.##.#.#####..###..###....#####..##...##.#.##
.#...###..#.###..##.##.##.#......#.#..#.####.##.#.....#.....#.##.##.#.
###..##.#.##...##.#.....####.##.#.#.#...###..###.##.#..#####..#.#...##
.##.#.##...#.#...####.#.#..#...#.#.##..###.##..###.#.####..#.#..##..#.
####.##...###...##...########..#..##..#..#...#..#.#....##.#.#.#.##..#.
#..#...#.###..##.#..##..#.#.#.##.#..##.####..#.##.#.##..##...####..#..
...#.#........###.#####...###.#.###..#.....#####.####..########......#
.##..#....#.#...#..#####.#...###.#....#.##.##......##..#..#######....#
#..#####.##.##.##.##....#..#..#...#........##.#.#.##.##.####.###......
#.###..##.#....##....###..##.#.#.#.#####.##.##..##.##...####......###.
.##.....###.###..#####....##...##..#.#..#.#...##..#....#..#...#....##.
....##.##..##..#.#####.###.#..#.###.#..#..####..#.#.####...#.######.##
#.###...#.##.######.#..##.##.#..##...###.#.#..##...##....##..#...###.#
..#.##..#.#.###...####.#.#....##..##..##...#.##..#...#...#.....#..##.#
..##...#.#.#..#..###.###..#....##.#.#.#.#######.###.##....#..##.##.###
#......#######.#..#.######.##..#.#.###.###..###..##.####.....#....#.##
####..##..#.#....###.#..#...###..###.....######.##.#....####.#.#.####.
.##.###.###.###.###.#####.#.##.#.#..###..#.#..#.##...##.....##.#####.#
##..#.#.#.#.#.##.####.#.##...#.#.##......#....#.###.##....#...##..####
.######.#.###.#..........#######.#.#.##..#..##...#.####...#.##.....###
#..#..####.#.......#...#.#....####.#..#...#####..###.########..#...##.
#.....##.####.##.#.##.#..#.#.#.#..#.#...##.##.#.##.#..#..##..#.#.#.##.
..#....###.##.###.#..###.#.####.####.#.##...#######.##..####.##.......
.#.....#####...####..#.#..#..###.#...#..##...#..#..###.#.####...###.##
"""