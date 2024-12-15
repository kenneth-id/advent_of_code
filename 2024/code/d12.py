from collections import deque

DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
DIAGONALS = [(1, 1), (-1, -1), (1, -1), (-1, 1)]

SAMPLE = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""


def count_corners(grid, pos):
    corner = 0
    x, y = pos
    cur_type = grid[x][y]
    for dx, dy in DIAGONALS:
        type_a = grid[x + dx][y] if x + dx < len(grid) else "$"
        type_b = grid[x][y + dy] if y + dy < len(grid[0]) else "$"
        type_diag = (
            grid[x + dx][y + dy]
            if x + dx < len(grid) and y + dy < len(grid[0])
            else "$"
        )

        if type_a != cur_type and type_b != cur_type:
            corner += 1

        elif type_a == cur_type and type_b == cur_type and type_diag != cur_type:
            corner += 1

    return corner


def bfs(grid, visited, initial_pos):
    area = corner = 0
    rows, cols = len(grid), len(grid[0])
    init_x, init_y = initial_pos
    plant_type = grid[init_x][init_y]
    q = deque([initial_pos])
    visited.add(initial_pos)

    while q:
        cx, cy = q.popleft()
        area += 1
        corner += count_corners(grid, (cx, cy))
        for dx, dy in DIRECTIONS:
            nx, ny = cx + dx, cy + dy

            if (
                0 <= nx < rows
                and 0 <= ny < cols
                and (nx, ny) not in visited
                and grid[nx][ny] == plant_type
            ):
                q.append((nx, ny))
                visited.add((nx, ny))

    return area, corner


with open("/Users/kennethlee/workspace/aoc/2024/input/d12.txt") as f:
    grid = f.read().splitlines()
    # grid = SAMPLE.splitlines()
    rows, cols = len(grid), len(grid[0])
    visited = set()
    tot_price = 0
    for i in range(rows):
        for j in range(cols):
            if (i, j) not in visited:
                area, corner = bfs(grid, visited, (i, j))
                tot_price += area * corner

    print("Total price:", tot_price)
