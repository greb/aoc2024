import math
import functools

def parse(inp):
    return [int(s) for s in inp.strip().split(' ')]


@functools.cache
def blink(stone, depth):
    if depth == 0:
        return 1

    if stone == 0:
        return blink(1, depth-1)

    l = int(math.log10(stone)) + 1
    if l % 2 == 0:
        a, b = divmod(stone, 10**(l//2))
        return blink(a, depth-1) + blink(b, depth-1)

    return blink(stone*2024, depth-1)


def part1(stones):
    return sum(blink(stone, 25) for stone in stones)

def part2(stones):
    return sum(blink(stone, 75) for stone in stones)
