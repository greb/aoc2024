import re

num_pattern = re.compile(r'mul\((\d+),(\d+)\)')
instr_pattern = re.compile(r"(mul\((\d+),(\d+)\)|do\(\)|don't\(\))")

def part1(inp):
    muls = num_pattern.findall(inp)
    return sum(int(a)*int(b) for a,b in muls)

def part2(inp):
    total = 0
    enabled = True

    instrs = instr_pattern.findall(inp)
    for op,a,b in instrs:
        match op:
            case "don't()": enabled = False
            case 'do()': enabled = True
            case _: total += int(a)*int(b) if enabled else 0
    return total
