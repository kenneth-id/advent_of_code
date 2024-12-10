def is_report_safe(report):
    increasing = True if report[1] > report[0] else False
    safe = True
    n = len(report)
    for i in range(1, n):
        if increasing:
            if report[i] > report[i - 1] and report[i] <= report[i - 1] + 3:
                continue
            else:
                return False
        else:
            if report[i] < report[i - 1] and report[i] >= report[i - 1] - 3:
                continue
            else:
                return False

    return safe


tot_safe = 0
unsafe_initial = []
with open("/Users/kennethlee/workspace/aoc/2024/input/d2.txt") as f:
    for report in f:
        parsed = list(map(int, report.split(" ")))
        safe = is_report_safe(parsed)
        tot_safe += safe

        if not safe:
            unsafe_initial.append(parsed)

print(f"safe_count: {tot_safe}")
print(f"unsafe_count: {len(unsafe_initial)}")
fixable_count = 0

for report in unsafe_initial:
    for i in range(len(report)):
        skipped_report = report[:i] + report[i + 1 :]
        if is_report_safe(skipped_report):
            fixable_count += 1
            break

print(f"Fixable count: {fixable_count}")
print(f"Safe after dampener: {tot_safe + fixable_count}")
