import re

SAMPLE_INPUT = """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0"""


class Computer:
    def __init__(self, reg_a, reg_b, reg_c, program):
        self.reg_a = reg_a
        self.reg_b = reg_b
        self.reg_c = reg_c
        self.i_pointer = 0
        self.program = program
        self.out_buffer = []

        self.COMBO_OPERAND = {
            0: 0,
            1: 1,
            2: 2,
            3: 3,
            4: lambda: self.reg_a,
            5: lambda: self.reg_b,
            6: lambda: self.reg_c,
        }

    def print_state(self):
        print(f"reg_a: {self.reg_a}, octal: {oct(self.reg_a)}")
        print(f"reg_b: {self.reg_b}, octal: {oct(self.reg_b)}")
        print(f"reg_c: {self.reg_c}, octal: {oct(self.reg_c)}")
        print(f"i_pointer: {self.i_pointer}")
        print(f"program: {self.program}")
        print(f"out_buffer: {self.out_buffer}")

    def run(self):
        while self.i_pointer < len(self.program):
            opcode = self.program[self.i_pointer]
            operand = self.program[self.i_pointer + 1]
            if opcode == 0:
                numerator = self.reg_a
                denominator = 2 ** self.get_operand(operand)
                self.reg_a = numerator // denominator
            elif opcode == 1:
                self.reg_b = self.reg_b ^ self.get_operand(operand, literal=True)
            elif opcode == 2:
                self.reg_b = self.get_operand(operand) & 7
            elif opcode == 3:
                if self.reg_a != 0:
                    self.i_pointer = self.get_operand(operand, literal=True)
                    continue
            elif opcode == 4:
                self.reg_b = self.reg_b ^ self.reg_c
            elif opcode == 5:
                output = self.get_operand(operand) & 7
                self.out_buffer.append(output)
            elif opcode == 6:
                numerator = self.reg_a
                denominator = 2 ** self.get_operand(operand)
                self.reg_b = numerator // denominator
            elif opcode == 7:
                numerator = self.reg_a
                denominator = 2 ** self.get_operand(operand)
                self.reg_c = numerator // denominator
            else:
                raise ValueError(f"Invalid opcode: {opcode}")

            self.i_pointer += 2

    def get_operand(self, key, literal=False):
        if literal:
            return int(key)

        operand = self.COMBO_OPERAND.get(key)
        return operand() if callable(operand) else operand


def parse_program(program_str):
    program_nums = list(map(int, program_str.split(",")))
    return program_nums


def read_input():
    with open("/Users/kennethlee/workspace/aoc/2024/input/d17.txt") as f:
        registers, program = f.read().split("\n\n")
        return registers, program.split()[1].strip()


def run_with_a(a, program):
    computer = Computer(a, 0, 0, program)
    computer.run()
    return computer.out_buffer.copy()


def find_quince(program):
    pot_solutions = []
    q = [(1, 0)]
    while q:
        match_n, a = q.pop()
        if run_with_a(a, program) == program:
            pot_solutions.append(a)
            continue
        if match_n <= len(program):
            q.extend(
                (match_n + 1, a << 3 | i)
                for i in range(8)
                if run_with_a(a << 3 | i, program)[-match_n:] == program[-match_n:]
            )

    return min(pot_solutions)


if __name__ == "__main__":
    registers, program_str = read_input()
    reg_a, reg_b, reg_c = map(int, re.findall(r"\d+", registers))
    program = parse_program(program_str)
    print("Program Input:")
    print(reg_a, reg_b, reg_c)
    print(program)
    computer = Computer(reg_a, reg_b, reg_c, program)
    computer.run()
    print("Program Output:")
    print("Part 1 answer:", ",".join(map(str, computer.out_buffer)))
    smallest_quince = find_quince(program)
    print("Part 2 answer:", smallest_quince)
