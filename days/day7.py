import collections
import itertools
import math
import operator

Equation = collections.namedtuple('Equation', ['val', 'args'])

def parse(inp):
    equations = []
    for line in inp.splitlines():
        val, args = line.split(': ')
        args = [int(a) for a in args.split(' ')]
        equations.append(Equation(int(val), args))
    return equations


def check_equation(base_ops, equation):
    ops_it = itertools.product(base_ops, repeat=len(equation.args)-1)
    for ops in ops_it:
        val = equation.args[0]
        for op, n_arg in zip(ops, equation.args[1:]):
            val = op(val, n_arg)
            if val > equation.val:
                break
        if val == equation.val:
            return True
    return False


def part1(equations):
    total = 0
    base_ops = [operator.add, operator.mul]
    for equation in equations:
        if check_equation(base_ops, equation):
            total += equation.val
    return total


def concat(a, b):
    n = int(math.log(b,10)) + 1
    return a*10**n + b


def part2(equations):
    total = 0
    base_ops1 = [operator.add, operator.mul]
    base_ops2 = [operator.add, operator.mul, concat]
    for equation in equations:
        if (check_equation(base_ops1, equation) or
            check_equation(base_ops2, equation)):
            total += equation.val
    return total

