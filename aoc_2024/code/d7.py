from collections import deque


def get_cur_val(values, op):
    vals_copy = values.copy()
    val_a = vals_copy.popleft()
    val_b = vals_copy.popleft()

    if op == "+":
        temp = val_a + val_b
    elif op == "*":
        temp = val_a * val_b
    elif op == "|":
        temp = int(str(val_a) + str(val_b))

    vals_copy.appendleft(temp)

    return vals_copy


def recurse(res, values):
    if len(values) == 1:
        return values[0] == res

    if values[0] > res:
        return False

    for op in ["+", "*", "|"]:
        processed = get_cur_val(values, op)
        if recurse(res, processed):
            return True

    return False


def is_valid(res, values):
    return recurse(res, deque(values))


SAMPLE = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

with open("/Users/kennethlee/workspace/aoc/2024/input/d7.txt") as f:
    tot_sum = 0

    for line in f:
        res, values = line.split(":")
        values = values.strip().split()
        res = int(res)
        values = [int(v) for v in values]

        if is_valid(res, values):
            tot_sum += res

    print(tot_sum)
