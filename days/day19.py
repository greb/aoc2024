import functools

def parse(inp):
    towels, designs = inp.split('\n\n')
    towels = towels.split(', ')
    designs = designs.splitlines()

    @functools.cache
    def count(design):
        if design == '':
            return 1
        cnt = 0
        for towel in towels:
            if design.startswith(towel):
                cnt += count(design[len(towel):])
        return cnt
    return [count(d) for d in designs]


def part1(counts):
    return sum(c>0 for c in counts)


def part2(counts):
    return sum(counts)

