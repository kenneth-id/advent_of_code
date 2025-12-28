from heapq import heappop, heappush

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
SMALL_SAMPLE_GRID = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""

SAMPLE_GRID = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################"""


def print_grid_with_path(grid, path_tiles):
    """Helper function to visualize the path on the grid"""
    for i in range(len(grid)):
        row = ""
        for j in range(len(grid[0])):
            if (i, j) in path_tiles:
                row += "0"
            else:
                row += grid[i][j]
        print(row)


def read_input():
    with open("/Users/kennethlee/workspace/aoc/2024/input/d16.txt") as f:
        start = end = None
        grid = []
        for i, line in enumerate(f):
            row = []
            line = line.strip()
            for j, char in enumerate(line):
                row.append(char)
                if char == "S":
                    start = (i, j)
                if char == "E":
                    end = (i, j)
            grid.append(row)
    return grid, start, end


def djikstra(grid, start, end):
    """
    Modified Dijkstra's algorithm to find all tiles visited by at least one minimum path.
    Explores all paths with the same minimum cost.

    Args:
        grid (List[List[str]]): The grid representation where '.' is walkable and 'E' is end
        start (tuple): Starting position (x, y)
        end (tuple): End position (x, y)

    Returns:
        min_cost (int): The minimum cost to reach the end
        set: Set of all tiles that are part of any minimum cost path
    """
    DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    q = []
    rows, cols = len(grid), len(grid[0])
    min_cost = float("inf")
    heappush(q, (0, start, (0, 1), [start]))
    best_path_tiles = set()

    # Track all costs for each state, not just the minimum
    costs_at_state = {}
    costs_at_state[(start, (0, 1))] = 0

    while q:
        cost, pos, direction, path = heappop(q)

        if cost > min_cost:
            continue

        op_x, op_y = (-direction[0], -direction[1])
        cx, cy = pos

        # If we've reached the end with exactly min_cost, update path
        if pos == end:
            if cost < min_cost:
                min_cost = cost
                best_path_tiles = set(path)
            elif cost == min_cost:
                best_path_tiles.update(path)
            continue

        for dx, dy in DIRECTIONS:
            nx, ny = cx + dx, cy + dy
            new_pos = (nx, ny)

            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] not in ["#"]:
                # Calculate new cost based on direction change
                if (dx, dy) == direction:
                    new_cost = cost + 1  # Continue straight
                elif (dx, dy) == (op_x, op_y):
                    new_cost = cost + 2001  # Reverse direction
                else:
                    new_cost = cost + 1001  # Turn left/right

                if new_cost <= min_cost:
                    new_state = (new_pos, (dx, dy))

                    # Continue exploring if:
                    # 1. We haven't seen this state before, or
                    # 2. We've seen it with a cost ≥ new_cost
                    current_cost = costs_at_state.get(new_state, float("inf"))
                    if current_cost >= new_cost:
                        costs_at_state[new_state] = new_cost
                        new_path = path + [new_pos]
                        heappush(q, (new_cost, new_pos, (dx, dy), new_path))

    return min_cost, best_path_tiles


if __name__ == "__main__":
    grid, start, end = read_input()
    min_cost, path = djikstra(grid, start, end)
    print("Minimum cost:", min_cost)
    print(
        "Number of tiles visited by at least one minimum path:",
        len(path),
    )
