import re
from functools import reduce


def print_positions(positions, width, height):
    for y in range(height):
        row = []
        for x in range(width):
            if (x, y) in positions:
                row.append("X")
            else:
                row.append(".")
        print("".join(row))


with open("/Users/kennethlee/workspace/aoc/2024/input/d14.txt") as f:
    width = 101
    height = 103
    mid_width = width // 2
    mid_height = height // 2

    line_numbers = []
    safety_scores = []
    for line in f:
        numbers = list(map(int, re.findall(r"-?\d+", line)))
        line_numbers.append(numbers)
    image_positions = set()
    for iteration in range(width * height):
        final_positions = set()
        quadrant_counts = [0, 0, 0, 0]
        duration = iteration
        for numbers in line_numbers:
            position = numbers[:2]
            vector = numbers[2:]
            final_position = [
                (position[0] + duration * vector[0]) % (width),
                (position[1] + duration * vector[1]) % (height),
            ]
            final_positions.add(tuple(final_position))
            if final_position[0] < mid_width and final_position[1] < mid_height:
                quadrant_counts[0] += 1
            elif final_position[0] > mid_width and final_position[1] < mid_height:
                quadrant_counts[1] += 1
            elif final_position[0] < mid_width and final_position[1] > mid_height:
                quadrant_counts[2] += 1
            elif final_position[0] > mid_width and final_position[1] > mid_height:
                quadrant_counts[3] += 1

        if iteration == 7344:  # My answer
            image_positions = final_positions

        safety_score = reduce(lambda x, y: x * y, quadrant_counts)
        safety_scores.append((safety_score, iteration))

    safety_scores.sort(key=lambda x: x[0])
    print(f"Lowest safety score iteration: {safety_scores[0][1]}")
    print_positions(image_positions, width, height)
