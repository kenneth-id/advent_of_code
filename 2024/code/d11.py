from functools import cache


@cache
def score(val, num_blinks):
    """
    If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
    If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
    If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
    """
    if num_blinks == 0:
        return 1

    num_digits = len(str(val))
    if val == 0:
        return score(1, num_blinks - 1)
    elif num_digits % 2 == 0:
        first_half = int(str(val)[: num_digits // 2])
        second_half = (
            0 if str(val)[num_digits // 2] == "0" else int(str(val)[num_digits // 2 :])
        )
        return score(first_half, num_blinks - 1) + score(second_half, num_blinks - 1)
    else:
        return score(val * 2024, num_blinks - 1)


with open("/Users/kennethlee/workspace/aoc/2024/input/d11.txt") as f:
    stones = f.read().strip()
    tot_score = 0
    for stone in stones.split():
        tot_score += score(int(stone), 75)

    print(tot_score)
