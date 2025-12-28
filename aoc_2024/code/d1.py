from collections import Counter

list1 = []
list2 = []

with open("/Users/kennethlee/workspace/aoc/2024/input/d1.txt") as f:
    for line in f:
        a, b = line.split()
        list1.append(int(a))
        list2.append(int(b))

list1.sort()
list2.sort()

total_diff = 0

for a, b in zip(list1, list2):
    total_diff += abs(a - b)

print(total_diff)
similarity = 0

counter = Counter(list2)
for num in list1:
    if num in counter:
        similarity += num * counter[num]

print(similarity)
