from functools import cache

SAMPLE_INPUT = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""


@cache
def recurse(towels, design):
    count = 0

    if not design:
        return 1

    for towel in towels:
        if design.startswith(towel):
            remaining_design = design[len(towel) :]
            count += recurse(towels, remaining_design)

    return count


def read_input():
    with open("/Users/kennethlee/workspace/aoc/2024/input/d19.txt") as f:
        return f.read()


if __name__ == "__main__":
    towels, designs = read_input().split("\n\n")
    towels = [towel.strip() for towel in towels.split(",")]
    designs = designs.strip().split("\n")
    num_paths = 0
    for i, design in enumerate(designs):
        num_path = recurse(tuple(towels), design)
        num_paths += num_path

    print("Total number of paths:", num_paths)
