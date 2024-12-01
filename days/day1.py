def parse(inp):
    pairs = [[int(n) for n in line.split()] for line in inp.splitlines()]
    return list(zip(*pairs))


def part1(inp):
    left, right = inp
    left = sorted(left)
    right = sorted(right)

    diffs = [abs(l-r) for l, r in zip(left, right)]
    return sum(diffs)


def part2(inp):
    cnt = 0
    left, right = inp
    for num in left:
        cnt += num * right.count(num)
    return cnt
