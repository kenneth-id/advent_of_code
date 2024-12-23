from collections import Counter, deque

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
SAMPLE_GRID = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############"""


class Racetrack:
    def __init__(self, grid):
        self.grid = grid
        self.rows, self.cols = len(grid), len(grid[0])
        self.distance_from_start = {}
        self.path = []

    def bfs(self, init_pos, end_pos):
        visited = set([init_pos])
        q = deque([(0, init_pos)])
        while q:
            distance, pos = q.popleft()
            cx, cy = pos
            self.path.append((cx, cy))
            self.distance_from_start[pos] = distance
            if (cx, cy) == end_pos:
                return distance
            for direction in DIRECTIONS:
                nx, ny = cx + direction[0], cy + direction[1]
                if (
                    0 <= nx < self.rows
                    and 0 <= ny < self.cols
                    and (nx, ny) not in visited
                    and self.grid[nx][ny] != "#"
                ):
                    visited.add((nx, ny))
                    q.append((distance + 1, (nx, ny)))
        return float("inf")

    def valid_cheat_end_pos(self, pos, x):
        cx, cy = pos
        positions = []
        for d in range(x + 1):  # Iterate over distances from 0 to x
            for dx in range(-d, d + 1):
                dy = d - abs(dx)

                nx, ny = cx + dx, cy + dy
                if (
                    0 <= nx < self.rows
                    and 0 <= ny < self.cols
                    and self.grid[nx][ny] != "#"
                    and self.distance_from_start[(nx, ny)]
                    > self.distance_from_start[pos]
                ):
                    positions.append((nx, ny))

                nx, ny = cx + dx, cy - dy
                if (
                    dy != 0
                    and 0 <= nx < self.rows
                    and 0 <= ny < self.cols
                    and self.grid[nx][ny] != "#"
                    and self.distance_from_start[(nx, ny)]
                    > self.distance_from_start[pos]
                ):
                    positions.append((nx, ny))

        return positions


def manhattan_distance(pos_a, pos_b):
    return abs(pos_a[0] - pos_b[0]) + abs(pos_a[1] - pos_b[1])


def read_input():
    with open("/Users/kennethlee/workspace/aoc/2024/input/d20.txt") as f:
        start = end = None
        grid = []
        track = []
        for i, line in enumerate(f):
            row = []
            line = line.strip()
            for j, char in enumerate(line):
                row.append(char)
                if char == "S":
                    start = (i, j)
                elif char == "E":
                    end = (i, j)
                    track.append((i, j))
                elif char == ".":
                    track.append((i, j))
            grid.append(row)
    return grid, track, start, end


if __name__ == "__main__":
    grid, track, start, end = read_input()
    rows, cols = len(grid), len(grid[0])
    print(f"Rows: {rows} Cols: {cols}")
    print(f"Start: {start} End: {end}")
    print("Number of track in grid:", len(track))

    racetrack = Racetrack(grid)
    time_with_no_shorcuts = racetrack.bfs(start, end)
    print("Time with no shortcuts:", time_with_no_shorcuts)
    print("Path:", racetrack.path)
    print("Distance from start:", racetrack.distance_from_start)

    CHEAT_DURATION = 20
    cheat_visited = set()
    time_saved_counter = Counter()
    for start_pos in racetrack.path:
        distance_to_start = racetrack.distance_from_start[start_pos]
        valid_cheat_end_positions = racetrack.valid_cheat_end_pos(
            start_pos, CHEAT_DURATION
        )
        for end_pos in valid_cheat_end_positions:
            if (start_pos, end_pos) in cheat_visited:
                continue
            cheat_visited.add((start_pos, end_pos))
            distance_to_end = (
                time_with_no_shorcuts - racetrack.distance_from_start[end_pos]
            )
            duration_phased = manhattan_distance(start_pos, end_pos)
            time_with_shortcut = distance_to_start + distance_to_end + duration_phased
            time_saved = time_with_no_shorcuts - time_with_shortcut

            if time_saved >= 100:
                time_saved_counter[time_saved] += 1

    print("Number of times saved more than 100:", sum(time_saved_counter.values()))
