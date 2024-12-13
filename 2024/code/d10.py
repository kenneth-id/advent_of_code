DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
SAMPLE = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

SAMPLE_2 = """..90..9
...1.98
...2..7
6543456
765.987
876....
987...."""

SAMPLE_3 = """...0...
...1...
...2...
6543456
7.....7
8.....8
9.....9"""


def dfs(grid, pos, peak_reached):
    cx, cy = pos
    cur_height = grid[cx][cy]

    if cur_height == 9:
        peak_reached.add(pos)
        return 1

    rows, cols = len(grid), len(grid[0])
    rating = 0
    for dx, dy in DIRECTIONS:
        nx, ny = cx + dx, cy + dy
        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == cur_height + 1:
            rating += dfs(grid, (nx, ny), peak_reached)

    return rating


with open("/Users/kennethlee/workspace/aoc/2024/input/d10.txt") as f:
    grid = []
    lines = f.read().splitlines()
    # lines = SAMPLE.splitlines()
    for line in lines:
        row = []
        for char in line:
            if char != ".":
                row.append(int(char))
            else:
                row.append(-1)
        grid.append(row)
    rows, cols = len(grid), len(grid[0])

    score_tot = 0
    rating_tot = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                peak_reached = set()
                rating = dfs(grid, (i, j), peak_reached)
                score_tot += len(peak_reached)
                rating_tot += rating

    print("Score:", score_tot)
    print("Rating:", rating_tot)
