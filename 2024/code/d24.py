from collections import deque

SAMPLE_INPUT = """x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj"""


def read_input():
    with open("/Users/kennethlee/workspace/aoc/2024/input/d24.txt") as f:
        return f.read()


if __name__ == "__main__":
    initial_values, logic_operations = read_input().split("\n\n")
    initial_values = initial_values.strip().split("\n")
    logic_operations = logic_operations.strip().split("\n")

    decided_values = {}
    for line in initial_values:
        id, value = line.split(": ")
        value = int(value)
        decided_values[id] = value

    pending_operations = deque(logic_operations)
    while pending_operations:
        raw_operation = pending_operations.popleft()
        operation, target_id = raw_operation.split(" -> ")
        source_a, op, source_b = operation.split(" ")
        if source_a in decided_values and source_b in decided_values:
            if op == "AND":
                decided_values[target_id] = (
                    decided_values[source_a] & decided_values[source_b]
                )
            elif op == "OR":
                decided_values[target_id] = (
                    decided_values[source_a] | decided_values[source_b]
                )
            elif op == "XOR":
                decided_values[target_id] = (
                    decided_values[source_a] ^ decided_values[source_b]
                )
        else:
            pending_operations.append(raw_operation)

    z_keys = filter(lambda k: k.startswith("z"), decided_values.keys())
    z_values = []
    for key in sorted(z_keys):
        print(key, decided_values[key])
        z_values.append(str(decided_values[key]))

    print("Decimal value:", int("".join(reversed(z_values)), 2))
