SMALL_SAMPLE = """########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<"""

LARGER_SAMPLE = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""

SMALL_SAMPLE_2 = """#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^"""

SMALL_SAMPLE_3 = """#######
#...#.#
#.....#
#.....#
#.....#
#.....#
#.OOO@#
#.OOO.#
#..O..#
#.....#
#.....#
#######

v<vv<<^^^^^"""


def print_grid(grid):
    for row in grid:
        print("".join(row))
    print()


def read_input():
    with open("/Users/kennethlee/workspace/aoc/2024/input/d15.txt") as f:
        grid, moves = f.read().split("\n\n")
        grid = [list(row) for row in grid.split("\n")]
        double_grid = []
        for i in range(len(grid)):
            row = []
            for j in range(len(grid[0])):
                if grid[i][j] == "@":
                    row.extend(["@", "."])
                elif grid[i][j] == "O":
                    row.extend(["[", "]"])
                elif grid[i][j] == ".":
                    row.extend([".", "."])
                elif grid[i][j] == "#":
                    row.extend(["#", "#"])
            double_grid.append(row)

        moves = moves.replace("\n", "").strip()
    return double_grid, moves


def get_box_pair(grid, box_pos):
    """Get both positions for a box pair ([ and ])"""
    if grid[box_pos[0]][box_pos[1]] == "[":
        return box_pos, (box_pos[0], box_pos[1] + 1)
    return box_pos, (box_pos[0], box_pos[1] - 1)


def get_next_positions(grid, box_pos, direction):
    """Get the next positions for a box or box pair"""
    if direction[1] != 0:  # Horizontal
        next_pos = (box_pos[0] + direction[0], box_pos[1] + direction[1])
        return [next_pos]
    else:  # Vertical
        box_pos, closing_pos = get_box_pair(grid, box_pos)
        return [
            (box_pos[0] + direction[0], box_pos[1]),
            (closing_pos[0] + direction[0], closing_pos[1]),
        ]


def can_push_box(grid, box_pos, direction):
    """Check if push is possible without modifying grid"""
    next_positions = get_next_positions(grid, box_pos, direction)

    for next_pos in next_positions:
        # Check bounds
        if not (0 <= next_pos[0] < len(grid) and 0 <= next_pos[1] < len(grid[0])):
            return False

        terrain = grid[next_pos[0]][next_pos[1]]
        if terrain == "#":
            return False
        elif terrain in ["[", "]"]:
            if not can_push_box(grid, next_pos, direction):
                return False

    return True


def perform_push(grid, box_pos, direction):
    """Perform the push, assuming it's been validated"""
    next_positions = get_next_positions(grid, box_pos, direction)

    # First push any boxes in the way
    for next_pos in next_positions:
        if grid[next_pos[0]][next_pos[1]] in ["[", "]"]:
            perform_push(grid, next_pos, direction)

    # Then move current box(es)
    if direction[1] != 0:  # Horizontal
        next_pos = next_positions[0]
        grid[next_pos[0]][next_pos[1]] = grid[box_pos[0]][box_pos[1]]
        grid[box_pos[0]][box_pos[1]] = "."
    else:  # Vertical
        box_pos, closing_pos = get_box_pair(grid, box_pos)
        next_box, next_closing = next_positions
        grid[next_box[0]][next_box[1]] = grid[box_pos[0]][box_pos[1]]
        grid[next_closing[0]][next_closing[1]] = grid[closing_pos[0]][closing_pos[1]]
        grid[box_pos[0]][box_pos[1]] = "."
        grid[closing_pos[0]][closing_pos[1]] = "."


def push_box(grid, box_pos, direction):
    """Main function to validate and perform push"""
    if can_push_box(grid, box_pos, direction):
        perform_push(grid, box_pos, direction)
        return True
    return False


def move_robot(grid, cur_pos, direction):
    moves = {
        "^": (-1, 0),
        "v": (1, 0),
        ">": (0, 1),
        "<": (0, -1),
    }

    if direction not in moves:
        return cur_pos

    delta = moves[direction]
    next_pos = (cur_pos[0] + delta[0], cur_pos[1] + delta[1])
    next_pos_terrain = grid[next_pos[0]][next_pos[1]]

    if next_pos_terrain == "#":  # Wall, cannot move
        return cur_pos
    elif next_pos_terrain == ".":  # Free space
        grid[next_pos[0]][next_pos[1]] = "@"
        grid[cur_pos[0]][cur_pos[1]] = "."
        return next_pos
    elif next_pos_terrain == "[" or next_pos_terrain == "]":  # Box
        if push_box(grid, next_pos, delta):
            grid[next_pos[0]][next_pos[1]] = "@"
            grid[cur_pos[0]][cur_pos[1]] = "."
            return next_pos
    return cur_pos


def sum_box_coords(grid):
    sum = 0
    rows, cols = len(grid), len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "[":
                sum += 100 * i + j
    return sum


def simulate(grid, moves):
    rows, cols = len(grid), len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "@":
                cur_pos = (i, j)

    for move in moves:
        cur_pos = move_robot(grid, cur_pos, move)


if __name__ == "__main__":
    grid, moves = read_input()
    # print("Initial state:")
    # print_grid(grid)
    simulate(grid, moves)
    # print("Final state after simulation:")
    # print_grid(grid)
    print("Sum of box coordinates:", sum_box_coords(grid))
