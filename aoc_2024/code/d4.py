# Part 1
WORD = "XMAS"
num_found = 0
DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

sample = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

with open("/Users/kennethlee/workspace/aoc/2024/input/d4.txt") as f:
    grid = f.read().splitlines()
    # grid = sample.splitlines()
    rows, cols = len(grid), len(grid[0])

    def backtrack(index, cur_pos, path, direction):
        global num_found
        cx, cy = cur_pos

        if index == len(WORD) - 1:
            num_found += 1
            path.append(cur_pos)
            path.pop()
            return

        path.append(cur_pos)
        dx, dy = direction
        nx, ny = cx + dx, cy + dy
        if (
            0 <= nx < rows
            and 0 <= ny < cols
            and grid[nx][ny] == WORD[index + 1]
            and (nx, ny) not in path
        ):
            backtrack(index + 1, (nx, ny), path, direction)
        path.pop()

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == WORD[0]:
                for direction in DIRECTIONS:
                    backtrack(0, (i, j), [], direction)

print(num_found)

# Part 2
x_count = 0
with open("/Users/kennethlee/workspace/aoc/2024/input/d4.txt") as f:
    grid = f.read().splitlines()
    rows, cols = len(grid), len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "A":
                diag = [(i - 1, j - 1), (i, j), (i + 1, j + 1)]
                antidiag = [(i - 1, j + 1), (i, j), (i + 1, j - 1)]
                diag_valid = True
                antidiag_valid = True

                diag_letters = [
                    grid[x][y] for x, y in diag if 0 <= x < rows and 0 <= y < cols
                ]
                antidiag_letters = [
                    grid[x][y] for x, y in antidiag if 0 <= x < rows and 0 <= y < cols
                ]
                formatted_diag = "".join(diag_letters)
                formatted_antidiag = "".join(antidiag_letters)
                if formatted_diag != "SAM" and formatted_diag != "MAS":
                    diag_valid = False
                if formatted_antidiag != "SAM" and formatted_antidiag != "MAS":
                    antidiag_valid = False
                if diag_valid and antidiag_valid:
                    x_count += 1
print(x_count)
