DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def detect_loop(map, start):
    obstacle_set = set()
    dir_index = 0
    cx, cy = start

    while 0 <= cx < rows and 0 <= cy < cols:
        dx, dy = DIRECTIONS[dir_index]
        nx, ny = cx + dx, cy + dy
        if nx < 0 or ny < 0 or nx >= rows or ny >= cols:
            break
        while map[nx][ny] == "#":
            if (nx, ny, dir_index) in obstacle_set:
                return True
            obstacle_set.add((nx, ny, dir_index))
            dir_index = (dir_index + 1) % len(DIRECTIONS)
            dx, dy = DIRECTIONS[dir_index]
            nx, ny = cx + dx, cy + dy
        cx, cy = nx, ny

    return False


with open("/Users/kennethlee/workspace/aoc/2024/input/d6.txt") as f:
    map = f.read().splitlines()
    map = [list(line) for line in map]
    rows = len(map)
    cols = len(map[0])

    for i in range(rows):
        for j in range(cols):
            if map[i][j] == "^":
                start = (i, j)

    path = []
    dir_index = 0
    cx, cy = start
    while 0 <= cx < rows and 0 <= cy < cols:
        path.append((cx, cy))
        dx, dy = DIRECTIONS[dir_index]
        nx, ny = cx + dx, cy + dy
        if nx < 0 or ny < 0 or nx >= rows or ny >= cols:
            break
        while map[nx][ny] == "#":
            dir_index = (dir_index + 1) % len(DIRECTIONS)
            dx, dy = DIRECTIONS[dir_index]
            nx, ny = cx + dx, cy + dy
        cx, cy = nx, ny

    distinct_paths = set(path)
    print("total distinct paths:", len(distinct_paths))

    num_obs_loc = 0
    valid_obstacle = distinct_paths
    valid_obstacle.remove(start)
    for obstacle_loc in valid_obstacle:
        map[obstacle_loc[0]][obstacle_loc[1]] = "#"
        if detect_loop(map, start):
            num_obs_loc += 1
        map[obstacle_loc[0]][obstacle_loc[1]] = "."

    print("number of infinite loop obstacle location:", num_obs_loc)
