import heapq

def parse(inp):
    blocks = []
    for line in inp.splitlines():
        a,b = line.split(',')
        blocks.append((int(a), int(b)))
    return blocks


DIRS = [(1,0), (0,1), (-1,0), (0,-1)]

def solve(blocks):
    block = set(blocks)
    end = w, h = 70, 70

    visited = set()
    stack = [(0, (0,0))]

    while stack:
        path_len, curr = heapq.heappop(stack)
        if curr == end:
            return path_len
        if curr in visited:
            continue
        visited.add(curr)

        for dir in DIRS:
            nxt = x,y = tuple(p+d for p,d in zip(curr, dir))
            if nxt in blocks:
                continue
            if 0 <= x <= w and 0 <= y <= h:
                heapq.heappush(stack, (path_len+1, nxt))

    return None


def part1(blocks):
    blocks = blocks[:1024]
    return solve(blocks)


def part2(blocks):

    a, b = 0, len(blocks)
    while (b-a) > 1:
        m = (a+b) // 2
        check = solve(blocks[:m])
        if check is not None:
            a = m
        else:
            b = m

    block = blocks[b-1]
    return f'{block[0]},{block[1]}'
