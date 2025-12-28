from heapq import heappop, heappush

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def read_input():
    with open("/Users/kennethlee/workspace/aoc/2024/input/d18.txt") as f:
        for line in f:
            x, y = map(int, line.split(","))
            yield x, y


def min_steps(falling_bytes):
    visited = falling_bytes.copy()
    rows = cols = 71
    q = []
    heappush(q, (0, (0, 0)))

    while q:
        distance, pos = heappop(q)
        x, y = pos
        if (x, y) == (70, 70):
            return distance
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                visited.add((nx, ny))
                heappush(q, (distance + 1, (nx, ny)))

    return float("inf")


if __name__ == "__main__":
    falling_bytes = set()
    input_generator = read_input()

    while len(falling_bytes) < 1024:
        try:
            x, y = next(input_generator)
            falling_bytes.add((x, y))
        except StopIteration:
            break

    print("Minimum steps:", min_steps(falling_bytes))

    while True:
        try:
            x, y = next(input_generator)
            falling_bytes.add((x, y))
            if min_steps(falling_bytes) == float("inf"):
                print("First byte that makes it impossible to reach the end:", x, y)
                break
        except StopIteration:
            break
