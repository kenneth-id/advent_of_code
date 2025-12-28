import re

mul_regex = r"mul\([1-9]\d*,[1-9]\d*\)"
num_regex = r"[1-9]\d*"
total_mul = 0

refined_regex = r"(mul\([1-9]\d*,[1-9]\d*\)|do\(\)|don't\(\))"

with open("/Users/kennethlee/workspace/aoc/2024/input/d3.txt") as f:
    content = f.read()
    do = True
    matches = re.findall(refined_regex, content)
    for match in matches:
        if match == "do()":
            do = True
        elif match == "don't()":
            do = False
        else:
            if do:
                nums = re.findall(num_regex, match)
                total_mul += int(nums[0]) * int(nums[1])

print(total_mul)
