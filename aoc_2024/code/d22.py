from collections import Counter, deque


def mix(value, secret_num):
    return value ^ secret_num


def prune(secret_num):
    return secret_num & 16777215


def secret_number(number, depth, counter):
    if depth == 0:
        return number

    seen = set()
    q = deque()
    prev_last_digit = number % 10

    for i in range(depth):
        number = prune(mix(number * 64, number))
        number = prune(mix(number // 32, number))
        number = prune(mix(number * 2048, number))

        last_digit = number % 10
        diff = last_digit - prev_last_digit
        q.append(diff)

        if len(q) == 4:
            tup = tuple(q)
            if tup not in seen:
                seen.add(tup)
                counter[tup] += last_digit
            q.popleft()

        prev_last_digit = last_digit
    return number


def read_input():
    with open("/Users/kennethlee/workspace/aoc/2024/input/d22.txt") as f:
        initial_numbers = []
        for line in f:
            initial_numbers.append(int(line.strip()))
        return initial_numbers


if __name__ == "__main__":
    initial_numbers = read_input()
    total = 0
    counter = Counter()
    for number in initial_numbers:
        total += secret_number(number, 2000, counter)

    print(counter.most_common(1))
