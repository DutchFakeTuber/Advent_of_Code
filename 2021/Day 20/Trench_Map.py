TEST_ALGORITHM: str = "..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#"
TEST_DATA: str = """
#..#.
#....
##..#
..#..
..###
"""

ALGORITHM: str = "##..#.####..#.#.##.#######.######.#####..#...##.###....#..#.##..#....#.#.##.#.#.#...###..###..#.#..#.#####.#.#.##..##.#.###.#..##.###.###...####.#####....#....#..#.#...#.#.#.#.#...#####...##..####.##.##...#.##.#####........#..#####..##.##..###########....#.##.#####.##..#####...#..#.#.##...#.#.#..#...####......#.#.####....##.#.##.####..##..##.#.......#...#.###########.....###.#######....##.#.#######..#.......###.##....#.#..#....##..#.###.#..#.###.###.##..##.#.#...#.#.....###.#.#....###..#.....##.#.#####....."
DATA: str = """
#.#.#.###...#####.#.###...#.#..##.#.#..#.#.#####.##......##..#.....#.#..#.##.#..##.##.#.#.#.##...#..
.#.##..#.##.#..#...##..##....##....###.##.#..##..............#####.#.###..#..####....##.##.#.#....#.
.##.##.###.##.#...#.#..#.###.##.####..#....#.#.####..##.####.###....##..###.#.#.....#..##.##.##.#...
..#.##.####.####..##..####.##.###..#.#..#..##.#..#..####.#.....####.#..#####...###.##...#.##...###..
###..##.#.#######.##....#.#.###..###..#..#####..#....##.##.###....#..#####.#..##.#...######.##..#.#.
....#.#.##..##.####..###..#####.#.#.##....#..#...##########..##.#...#..#.##.#####.#.###..#.#..######
.#....#.........##...#####.##.......#.###.#.###..###.#..##.###...####...........#..######...##..####
...#.#..###.###.#.#.##.#.###.#.######.#####.#...#.#...##..###.##.####.###..#..#.####.####..#.##.#.##
.#.#..####..#.#.#.##.......##..#..##..#..#.#.#..##..#..##.#.#.##..###....###.###.###..#....#.#..#.##
#......###.##.#..###.#.#.###.#...#..#.#.##.##...##..####..##.###..#...######...####..##.#####......#
.#...###.#.##.##...##......##..#.....###.###.#.#.####.###...#...#...#.##..#.##.###.#.#..#.....#####.
.##..#..#.#..#..#.##..#..###..##.##....#.#....#.####.##.###.#...###.#..###..###..#......##..#...##.#
..##..#..#..#..##.##...###.#.##.....#..###..##...##......#.#.#..#..#..#.#...#...#.........#.##.#...#
#.###.#..##..##...#.#...#......###.....##.######..#....#...##.###..#..####...##......#.##...##.##.#.
####....#.#..##.#.#.....##.##.#....#.##...###.#.#.#..##...#####.##.#.......##.#..#.##.....###.#.#..#
...#.#...#.......#.##.#...#####...##.##.#....###.......##...#.##.#.##...#.#.....#.#####.###.#####.#.
.###..#..##..####.##.#.###.###.###..#...###.#######...#...#.###..###..#..###.....##..#.###......##..
.#####.##.#..##....#.########..####.##...###..#.###..#..#.#####...#...##.#.##.#.....##.#..#####...##
...###......##.#.#.##...#....#.##..#.##.##..##.#.#.#####....#..##....##..##.#.##.....#..#.#..####..#
.#..###....#....##.#..#.##...#.#..#.#####.###.#.#..#.#..#.##.#....##.#.##...#####.#####...#...##.#..
#.#.#...#....#.#..#.##.#....#.#.###..##.##..#.#.#.....######.....#.#..#.###.#..##.##.#.###..#.###...
..#.#.#.#......###..##.#.##.##.###...###..#..####...#.#.##.###.#..#.#.#...##..##..##..#..####.##..##
...#.#.#...#..######.##.##.##...#..#..#..#..##.###.#....#..##..##.##.#......###.#.#..#....#.#...#...
...#.##...#.....###...#.##.###...####.#####....##.#....##.#...#.#..##..##.#..#####.......##.#...#.#.
##.#.#######.###...#.####..#..###.#.#..#.#.#.###..##.#.##.....#####..##.#...##...#....###.#.#...##..
##.#....##.##.#.###.......##..#.##..#.#......#..#.##.#..##.###..##...#...###...#..##.###...###....##
...#..#..#...##...#.###.#######.#.#....#..#.#####.#...#####....###.######....#.#..#.....##.#..##.##.
...#.##########..#.##..###....##.....####.##..###..#.#.####..###.###...###..##...#.#.###...#...#.#.#
.#...#.#.....#.##.#.#.##...#....#.....#.#.....#...##..##.#.##..#....#.##.#######.##.##....#...#..###
.#..#....#.#...##.##.##...#.#..##.##..#...#.###..#.##.###.#...###....####..#.##..####.#.#..#########
#.###.#..#####.##...##.##...#.#####...#..###....#.#..#..#.##..##.#..######..##.######.#..#.###..####
##..#.##.##..#.....#...#...#####.##...##.#.##.####..#.###.##.#.....##..#....#.#..###.#.##.#.#.###...
#.##..#.#.....#..#.##.###..###...##..#.#........##.###.#.........###.....#..#.##.##...###...#..###.#
#.....##.#.....#.#..###..#.#...#..#..###.#......###..#.######..#...##.#.#...#.#.#.#..##.##...##.##..
###...#....#..####.#..###..#.#.#..##.###..##.####...##.#..###.#.####.#..#....##...#.#...###..###..#.
..##..#..#...##.....##..#.##.##..#.#.####.##.###.#.#####......#.#..##.#...##.#.#.####..###....##...#
..##.#....#.####.....#.#.##....###..##..##..##....#...##...#.#.#.########...####....#..#.#.###.#.#..
###.#.##.###......####....##.##.#...###.#.....#....###.##.#######.##.####.##.#.###.####..#......#..#
...#..#..#.#....#.####...##.#..##.#####.###.#..#.##....#.##.#..####.#.#...######..###.#.######.##.#.
####.#....#....#...###....#.#.#.##.#..##.#.####..##..#...#......#######.#.#.#.##..#.....#..##.......
..##.#.#...#.##...#..#..##.#.##.......#.##.####..#.#.....#..#.....###.##.#.#...###..#..#...#.#.##.##
.#.########..####.#.###...##...#........#.####.####.#.#####.###..#####...##.##..#..#.#......#...###.
.#...#.###.#.#...#.#.#..####.##.#.####..#..#.##.....#####..#######.##....##...###..####.#.#####.....
###.#.######.#.#.#..#.#....##.....#...###.####.#.#..#.....##.##.###.#.####.....##.#....#...##..#.#..
##...#.....##.####.###.#.#.#.##.#.#.##.####....#.######....#....##......#....#..#.#..####.#.#.##.##.
..#.##.##...#.#.....#.##.##.######.####..#...#..###.##..##...#.####.##....##..#.###.#.####.###.#...#
#.##.##.##...#.....##.#.##.#.#####.#.#.....#..##...#.####...######..#....#.#.##..###.############..#
#.##.###...#..#.#.....####..#..#.#..#.#########...#..##.#.#...#...#.#.#...#...#.#..##.#.#..####.#..#
.##.##.##......##.#..###.#.##.####..#..##...###...##....#.##..#####.#.#.#...#.#.#..###..###..###..#.
.##.#####..#.#.#.####.#.#.##.##.....######.#..###..#####..##....#.#.#.##.##.#...#.#.#.#.####.##.##..
...#....#.##...#####.#.###.####...##.#...##.#.#..#.#...####......#####.#.##.#..#####.#...#..#...#...
#..#.##...#.#..#.###.#.#.#...#.##.##..#.##...###.######..#.##..###..#.#.###.##.#.###.....#..#.#..###
.###.#........##..##......##.#######.#.#..###...#..#.##..####.#.####..###...#..##.###.##.###.#...#..
###.###..##..##.#..#.##....#####.##.#....#..###..#..#.#...#.#.#......#.##..#####...###..##.#.....###
##.#..###...#.#..###.....###.###.#.#..#...#.#...###..#.....########.##......#...##..#.#.#.#..#.#.##.
#..##.#.#.##.####..##.###..#...#..#..###..##...#..#......#.#....##......####.#.###...##..###...#...#
..#..##..####..###..#####.#.#.##.##.##....##.#.#.##...#......#...#..###....####..#.##..#.###....#.##
###..#######...#...######.#######.##..##..###.....##..#...#..##..#######.....#..##..##..##..#.####..
..#.###.#.##...#.#.##.#.#.###..##.....###.###.#..####.#...##..##...#..#.###.##.##.####....#...##....
##.#.#...##.....#.#.#.##..##..####....#.#...#.#.#.#..#..###..###.#.#.###..#.###..#..###...##.......#
###...##..#.#.####..#..#...##..#..#.#.#.#...###.##.###.###.#####.#.....####..#####.###.##..###..#...
..###.#####.##...#.####....#.#...##...##....###......###...#.#.#.......###..#..#...#####.#..########
#.####....#.#.#.#.#.#.#..#.##...#.#.###.#.##.##..#..#.###.##.##....##.###...#..##.#.....##.###.##.#.
.#.#.##..#.#.##...##.####.#...#.#..##.#..##.#.##..##..#.####.##.#...##..###.###..###..#.#....###.##.
####.#...#....####.###.####...##.....#######.....###....##.#........#.###.....#.#.#.###.####.##.#.##
.#..#..#..####.#.##..##...###..###.###...######.###....##...#.##..#####.#.####.......#...#.##.#.....
.#..#....#...#####..#..#...#..#...##.#.##.#.##.#...#.##..##.####..#.###.###.#..##.###.......###.#...
.##.##.#..#...###.####.#.###.#...#..#.##.#..##.#.#.##..####.#####....##.###.###....#....#..##.###..#
..#..#..##.###...#.###.#.###...###....##.##.#.#..#..#.##.#.#.....#####..#.##.###.#.....#..#.#.######
#...##..###.###.#..#....#..#.##..##.###..#.#.#..##...#.##..#..#.#####.......#.##......##.#.#..#..#..
.#....####.##.###.##....#...###.#..#####.#..#..##....####.#...####.#..###...#....#.#..####..##....##
##..#####..#..#..#.#####.#.###..#....#..##.#...#.###..#..#####....##..##.#......##.###..#.#...#.###.
##.......#..##.#.#.##.#...#.########.#.#.##..##.#..###.....#.#..###...##..#......##.##.##......#..##
.##...##.#.#.....#.#.#.#....###..#..##...#.#.#.##.####.##.##.##.....##.#.....#.#.##..#.#.####.#..##.
..#..#....###.....#.###...###.###...##....##.#.#.##....#..######...#.##.#.#...##.#....##########.###
.....#.#.#.##.#.#.....#..#.#.#..####.##.#...#.#.....#####.###.#...#...#....###.#.......#.#..#...##..
.##..###.#....#..#.##.#.#.#..#..#.##.....#####..##.....##.##....#...#..##..#..#.....###..#...##.#..#
#.#.#..#.#...#.#.#.#...#..#.#.###.#.....#...#...#.###..######.#..###..####..####...##..#.....#.####.
#..##........#.#.##.#.##.#.#####..#....#####.####...#....#.#..####.#..###.#.###..##..#....##.#...#.#
..#....#....#....#.#.####......#.##...###..###.#.#..#.#.#.###..#.#.###.....#..###..##..#.##..#.#..##
#...#..#.###.#....#.#.#.#..#.####..#####..###.....##..#.###..#.##.#####.#.#....###.###..#.##.###..#.
#####.###.#.#.####..#.###.##..#.#.#..#........#########.##.#.#.#..##.#...#..#...#.##....#..##.##.#.#
#.##.....#.##.#..##.....####.##..#..#...#.#..#.#######..#.##.#..#.##...###.###....###..#.##.##.####.
.#....##########..#.#..###..#.#.#.#...#..#.#..###..##....######.###....#...##...#...#..###.#.#...###
#.#.#..#.##.....##..####.###.#.###.#..#....#.#...#..##.#.#.##...#..#.......#...#.....##.##.##...#...
#....#...#..##..............##.###.#.#####.##..#########..#.#..##.###..##.##..#.##.##..##..#...###.#
##...#.####...##.....##.##....##.######.##.#.##.####..##..#####..#..#.#.###.....#..##..#.#...####...
#..#.####.#....##..#.###.##.#.#.#.#...##.##.#.####......###.#.####.#####...##.#.#.##.#..######..#..#
..##...##.#.##.##.#.#..#....#.##.##.#..###...######.####.#......#..#.#..#.#####.....#.#.#..#......#.
#......#.###.#......###....##.##.#.#...#...##.#.#.######..#.##.####..#..#...#.##.###....#......####.
.#.#.#####.###.##.##......#......##.#.....##..#.###..#.##....##.#.##.#####..##.##..#####.#..#...##.#
##.#.#.#..#.###.##.#.#....##.#.##.....#.#.#.#..#...#.....#.#.#.#.#####....#######.#..#..##..##.###.#
..#.##..####.#.......#....######...####.#.#.###.#...######.#....##.#.##.##.###.#..#...##...##..#....
.#.##.###..###........##.##.####.####.#...#.##....#####.##..####...##.##..#.#.####.#####....##....#.
#.##.#.#.##......#.#####.#.#..###....#...#...#..##..##.#.#.####..###.#.#..######.###.......#..#.####
..##.#.#...##...#.....#......#..##.#.##.###.#.###..#..#.#.####.##.#.####.#.####.#.#..###.##.###..#.#
#........#.#..#.....##..#...##..##..##..#.##..##.#.####..####.#.#.#####..###.#.....#.#....#..#..###.
#..##..#.######.....##..#.##..#..###.####.#.#....#.#.........#####.####..##.####.##..#.#..#..#.###..
##.##..##.####..#.#...#..#..#..##.....##..#...#.###..#.............##.#...###....##.####.#.###..#..#
#..#.#.###..###....#####.#.#.#..#.##.#.##...##..###.##..###....#.###.##..#.#.#.#######.##.#.#.#..#..
"""