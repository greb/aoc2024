import math

def parse(inp):
    equations = []
    for line in inp.splitlines():
        val, args = line.split(': ')
        args = [int(a) for a in args.split(' ')]
        equations.append((int(val), args))
    return equations


def check_equation(target, args, concat=False):
    *front, n = args
    if not front:
        return n == target

    n_target, rest = divmod(target, n)
    if rest == 0 and check_equation(n_target, front, concat):
        return True
    if concat:
        e = int(math.log10(n)) + 1
        n_target, rest = divmod(target, 10**e)
        if n == rest and check_equation(n_target, front, concat):
            return True
    return check_equation(target-n, front, concat)


def part1(equations):
    total = 0
    for val, args in equations:
        if check_equation(val, args):
            total += val
    return total


def part2(equations):
    total = 0
    for val, args in equations:
        if check_equation(val, args, True):
            total += val
    return total
