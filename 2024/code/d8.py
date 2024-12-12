from collections import defaultdict
from itertools import combinations

SAMPLE = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""


def get_antinodes(pair, rows, cols):
    antinodes = []
    a, b = sorted(pair)
    dy, dx = b[1] - a[1], b[0] - a[0]
    cur_a = a
    cur_b = b

    while 0 <= cur_a[0] < rows and 0 <= cur_a[1] < cols:
        anti_a = (cur_a[0] - dx, cur_a[1] - dy)
        antinodes.append(anti_a)
        cur_a = anti_a

    while 0 <= cur_b[0] < rows and 0 <= cur_b[1] < cols:
        anti_b = (cur_b[0] + dx, cur_b[1] + dy)
        antinodes.append(anti_b)
        cur_b = anti_b

    return antinodes


with open("/Users/kennethlee/workspace/aoc/2024/input/d8.txt") as f:
    grid = f.read().splitlines()
    # grid = SAMPLE.splitlines()
    rows, cols = len(grid), len(grid[0])

    antinodes = set()

    poi_map = defaultdict(list)
    for i in range(rows):
        for j in range(cols):
            char = grid[i][j]
            if char != ".":
                poi_map[char].append((i, j))

    for char, locations in poi_map.items():
        if len(locations) > 1:
            for point in locations:
                antinodes.add(point)

        pairs = combinations(locations, 2)
        for pair in pairs:
            new_antinodes = get_antinodes(pair, rows, cols)
            for point in new_antinodes:
                if 0 <= point[0] < rows and 0 <= point[1] < cols:
                    antinodes.add(point)

    print(len(antinodes))
