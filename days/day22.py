import collections

def parse(inp):
    buyers = []
    for n in map(int, inp.splitlines()):
        nums = [n]
        for _ in range(2000):
            n = monkey_rng(n)
            nums.append(n)
        buyers.append(nums)

    return buyers


def monkey_rng(n):
    n = (n*64 ^ n) % 16777216
    n = (n//32 ^ n) % 16777216
    n = (n*2048 ^ n) % 16777216
    return n


def part1(buyers):
    return sum(nums[-1] for nums in buyers)

def part2(buyers):
    patterns = collections.defaultdict(int)

    for nums in buyers:
        diffs = [b%10 - a%10 for a,b in zip(nums, nums[1:])]
        seen = set()
        for i in range(len(nums)-4):
            pattern = tuple(diffs[i:i+4])
            if pattern not in seen:
                patterns[pattern] += nums[i+4] % 10
                seen.add(pattern)

    return max(patterns.values())
