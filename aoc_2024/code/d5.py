from collections import defaultdict

SAMPLE = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""


def valid_report(report, rule_map):
    should_before = set()
    for num in report:
        if num in should_before:
            return False
        should_before.update(rule_map[num].before)
    return True


def sort_invalid(report, rule_map):
    n = len(report)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if report[j] in rule_map[report[j + 1]].after:
                report[j], report[j + 1] = report[j + 1], report[j]
                swapped = True
        if not swapped:
            break


class Rule:
    def __init__(self):
        self.before = set()
        self.after = set()

    def add_before(self, item):
        self.before.add(item)

    def add_after(self, item):
        self.after.add(item)


with open("/Users/kennethlee/workspace/aoc/2024/input/d5.txt") as f:
    contents = f.read()
    # contents = SAMPLE
    raw_rules, raw_reports = contents.split("\n\n")
    rules = raw_rules.split("\n")
    reports = raw_reports.split("\n")
    parsed_reports = [list(map(int, r.split(","))) for r in reports if r]
    rule_map = defaultdict(Rule)

    tot_mid_num = 0
    for rule in rules:
        before, after = map(int, rule.split("|"))
        rule_map[before].add_after(after)
        rule_map[after].add_before(before)

    invalid_reports = []
    for report in parsed_reports:
        if valid_report(report, rule_map):
            tot_mid_num += report[len(report) // 2]
        else:
            invalid_reports.append(report)

    print("total mid num", tot_mid_num)

    tot_mid_fixed = 0
    for report in invalid_reports:
        sort_invalid(report, rule_map)
        tot_mid_fixed += report[len(report) // 2]
    print("tot mid fixed", tot_mid_fixed)
