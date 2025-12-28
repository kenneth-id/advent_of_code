import re

import numpy as np

SAMPLE = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""

REGEX_NUM = r"\d+"
with open("/Users/kennethlee/workspace/aoc/2024/input/d13.txt") as f:
    raw_equations = f.read().split("\n\n")
    # raw_equations = SAMPLE.split("\n\n")

    tot_token = 0
    for equation in raw_equations:
        matches = list(map(int, re.findall(REGEX_NUM, equation)))
        n = len(matches)
        for i in range(4, n):
            matches[i] = matches[i] + 10000000000000
        X = np.array([matches[:2], matches[2:4]]).T
        y = np.array(matches[4:])
        try:
            a, b = np.linalg.solve(X, y)
            diff_a = abs(a - round(a))
            diff_b = abs(b - round(b))
            if diff_a < 0.001 and diff_b < 0.001:
                a_int = int(round(a))
                b_int = int(round(b))
                tot_token += 3 * a_int + b_int
        except np.linalg.LinAlgError:
            print("No solution")

    print(tot_token)
