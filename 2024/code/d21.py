"""Disclaimer for this day: Had a lot of trouble figuring this out. Got a lot of hints to get to the solution"""

from functools import cache

NUM_PAD = {
    "7": (0, 0),
    "8": (0, 1),
    "9": (0, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "1": (2, 0),
    "2": (2, 1),
    "3": (2, 2),
    "0": (3, 1),
    "A": (3, 2),
}
DIR_PAD = {
    "^": (0, 1),
    "A": (0, 2),
    "<": (1, 0),
    "v": (1, 1),
    ">": (1, 2),
}


def create_graph(keypad, invalid_coords):
    graph = {}
    for a, (x1, y1) in keypad.items():
        for b, (x2, y2) in keypad.items():
            path = "<" * (y1 - y2) + "v" * (x2 - x1) + "^" * (x1 - x2) + ">" * (y2 - y1)
            if invalid_coords == (x1, y2) or invalid_coords == (x2, y1):
                path = path[::-1]
            graph[(a, b)] = path + "A"
    return graph


NUMPAD_GRAPH = create_graph(NUM_PAD, (3, 0))
DIRPAD_GRAPH = create_graph(DIR_PAD, (0, 0))


def read_input():
    with open("/Users/kennethlee/workspace/aoc/2024/input/d21.txt") as f:
        return f.read().strip().split("\n")


def convert(sequence, graph):
    conversion = ""
    prev = "A"
    for char in sequence:
        conversion += graph[(prev, char)]
        prev = char
    return conversion


@cache
def shortest_sequence(sequence, depth, first=False):
    if depth == 0:
        return len(sequence)

    prev = "A"
    total_length = 0
    graph = NUMPAD_GRAPH if first else DIRPAD_GRAPH
    for char in sequence:
        total_length += shortest_sequence(graph[(prev, char)], depth - 1)
        prev = char

    return total_length


def complexity(code):
    num = int(code[:3])
    # Part 1
    # sequence = convert("8", NUMPAD_GRAPH)
    # print(sequence)
    # sequence = convert(sequence, DIRPAD_GRAPH)
    # print(sequence)
    # sequence = convert(sequence, DIRPAD_GRAPH)
    # print(sequence)
    # return num * len(sequence)

    # Part 2
    return num * shortest_sequence(code, 26, first=True)


if __name__ == "__main__":
    codes = read_input()
    print(codes)
    total_complexity = 0
    for code in codes:
        total_complexity += complexity(code)

    print("Total complexity:", total_complexity)
